import base64
import hashlib
import textwrap
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path
from string import Template

from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from loguru import logger

from src.chrome_utils import HTML_to_PDF, init_browser
from src.config import Config
from src.job_analyzer import JobDescriptionAnalyzer
from src.llm import get_llm
from src.resume import load_curriculum_vitae
from src.resume_prompts import (
    education_experience_prompt,
    header_prompt,
    interest_prompt,
    personal_advantage_prompt,
    project_experience_prompt,
    work_experience_prompt,
)


class ResumeGenerator:
    def __init__(self, config: Config):
        self.config = config
        self.resume = load_curriculum_vitae(config)
        self.llm = get_llm(config)
        self.driver = init_browser()
        self.jd_description_analyzer = JobDescriptionAnalyzer(self.llm, self.driver)

    @staticmethod
    def _preprocess_template_string(template: str) -> str:
        """
        Preprocess the template string by removing leading whitespace and indentation.
        Args:
            template (str): The template string to preprocess.
        Returns:
            str: The preprocessed template string.
        """
        return textwrap.dedent(template)

    def generate_header_section(self) -> str:
        chain = (
            ChatPromptTemplate.from_template(
                self._preprocess_template_string(header_prompt)
            )
            | self.llm
            | StrOutputParser()
        )
        return chain.invoke(
            {
                "job_description": self.jd_description_analyzer.job_description,
                "resume_profile": self.resume.resume_profile,
            }
        )

    def generate_personal_advantage_section(self) -> str:
        chain = (
            ChatPromptTemplate.from_template(
                self._preprocess_template_string(personal_advantage_prompt)
            )
            | self.llm
            | StrOutputParser()
        )
        return chain.invoke(
            {
                "job_description": self.jd_description_analyzer.job_description,
                "job_key_points": self.jd_description_analyzer.key_points,
                "personal_advantage": self.resume.personal_advantage,
            }
        )

    def generate_work_experience_section(self) -> str:
        chain = (
            ChatPromptTemplate.from_template(
                self._preprocess_template_string(work_experience_prompt)
            )
            | self.llm
            | StrOutputParser()
        )
        return chain.invoke(
            {
                "job_description": self.jd_description_analyzer.job_description,
                "job_key_points": self.jd_description_analyzer.key_points,
                "work_experience": self.resume.work_experience,
            }
        )

    def generate_education_section(self) -> str:
        chain = (
            ChatPromptTemplate.from_template(
                self._preprocess_template_string(education_experience_prompt)
            )
            | self.llm
            | StrOutputParser()
        )
        return chain.invoke(
            {
                "job_description": self.jd_description_analyzer.job_description,
                "job_key_points": self.jd_description_analyzer.key_points,
                "education_experience": self.resume.education_details,
            }
        )

    def generate_project_experience_section(self) -> str:
        chain = (
            ChatPromptTemplate.from_template(
                self._preprocess_template_string(project_experience_prompt)
            )
            | self.llm
            | StrOutputParser()
        )
        return chain.invoke(
            {
                "job_description": self.jd_description_analyzer.job_description,
                "job_key_points": self.jd_description_analyzer.key_points,
                "project_experience": self.resume.project_experience,
            }
        )

    def generate_interest_section(self) -> str:
        chain = (
            ChatPromptTemplate.from_template(
                self._preprocess_template_string(interest_prompt)
            )
            | self.llm
            | StrOutputParser()
        )
        return chain.invoke(
            {
                "interest": self.resume.hobbies_and_interests,
            }
        )

    @staticmethod
    def generate_digest(job_link: str) -> str:
        return hashlib.md5(job_link.encode()).hexdigest()[:10]

    def generate_html_resume(self, digest: str, resume_html: str) -> Path:
        output_dir = Path(self.config.task_path) / "output" / digest
        output_dir.mkdir(parents=True, exist_ok=True)
        output_path = output_dir / "resume.html"
        with open(output_path, "wb") as f:
            f.write(resume_html.encode("utf-8"))
        logger.info(f"导出HTML简历完成... 路径: {output_path}")
        return output_path

    def generate_pdf_resume(self, html_path: Path):
        output_dir = html_path.parent
        output_path = output_dir / "resume.pdf"
        try:
            schema = "file://" + str(html_path.absolute())
            b64 = HTML_to_PDF(schema, self.driver)
            try:
                pdf_data = base64.b64decode(b64)
            except base64.binascii.Error as e:
                logger.error("Error decoding Base64: %s", e)
                raise

            with open(output_path, "wb") as f:
                f.write(pdf_data)
            logger.info(f"导出PDF简历完成... 路径: {output_path}")

        except Exception as e:
            logger.error(f"导出PDF简历失败: {e}")
            raise e

    def driver_quit(self):
        self.driver.quit()

    def _load_resume_template(self) -> str:
        tpl_path = (
            Path(self.config.task_path) / "resume_templates" / "resume_template.tpl"
        )
        with open(tpl_path, "r", encoding="utf-8") as f:
            return f.read()

    def generate_resume(self, job_link: str) -> str:
        self.jd_description_analyzer.analyze_job_description(job_link)
        tpl = Template(self._load_resume_template())

        def generate_header_content():
            if self.resume.resume_profile:
                logger.info("简历头信息生成中...")
                return self.generate_header_section()
            logger.info("无简历头信息，请仔细检查info.yml简历文件，跳过生成...")
            return ""

        def generate_personal_advantage_content():
            if self.resume.personal_advantage:
                logger.info("个人优势信息生成中...")
                return self.generate_personal_advantage_section()
            logger.info("无个人优势信息，请仔细检查info.yml简历文件，跳过生成...")
            return ""

        def generate_work_experience_content():
            if self.resume.work_experience:
                logger.info("工作经验信息生成中...")
                return self.generate_work_experience_section()
            logger.info("无工作经验信息,请仔细检查info.yml简历文件，跳过生成...")
            return ""

        def generate_education_content():
            if self.resume.education_details:
                logger.info("教育经历信息生成中...")
                return self.generate_education_section()
            logger.info("无教育经历信息,请仔细检查info.yml简历文件，跳过生成...")
            return ""

        def generate_project_experience_content():
            if self.resume.project_experience:
                logger.info("项目经验信息生成中...")
                return self.generate_project_experience_section()
            logger.info("无项目经验信息,请仔细检查info.yml简历文件，跳过生成...")
            return ""

        def generate_interest_content():
            if self.resume.hobbies_and_interests:
                logger.info("兴趣爱好信息生成中...")
                return self.generate_interest_section()
            logger.info("无兴趣爱好信息,非必须，跳过生成...")
            return ""

        functions = {
            "header": generate_header_content,
            "personal_advantage": generate_personal_advantage_content,
            "work_experience": generate_work_experience_content,
            "education": generate_education_content,
            "project_experience": generate_project_experience_content,
            "interest": generate_interest_content,
        }
        with ThreadPoolExecutor() as executor:
            future_to_section = {
                executor.submit(fn): section for section, fn in functions.items()
            }
            results = {}
            for future in as_completed(future_to_section):
                section = future_to_section[future]
                try:
                    result = future.result()
                    if result:
                        results[section] = result
                except Exception as exc:
                    logger.error(f"{section} raised an exception: {exc}")

        full_resume = "\n"
        full_resume += f"  {results.get('header', '')}\n"
        full_resume += f"  {results.get('personal_advantage', '')}\n"
        full_resume += f"  {results.get('work_experience', '')}\n"
        full_resume += f"  {results.get('project_experience', '')}\n"
        full_resume += f"  {results.get('education', '')}\n"
        full_resume += f"  {results.get('interest', '')}\n"
        return tpl.substitute(
            name=self.resume.resume_profile.name,
            body=full_resume,
        )

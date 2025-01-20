from typing import Dict

from langchain.output_parsers import PydanticOutputParser
from langchain_core.language_models.chat_models import BaseChatModel
from langchain_core.prompts import ChatPromptTemplate
from loguru import logger
from selenium import webdriver
from selenium.webdriver.common.by import By

from src.job_analysis_prompts import jd_analyze_prompt, parse_web_page_prompt
from src.job_description import JobDescription, JobKeyPoints


class JobDescriptionAnalyzer:
    def __init__(self, llm: BaseChatModel, driver: webdriver.Chrome):
        self.jd_key_points: JobKeyPoints | None
        self.job_info: JobDescription | None
        self.llm = llm
        self.driver = driver
        self.jd_parser = PydanticOutputParser(pydantic_object=JobDescription)
        self.key_points_parser = PydanticOutputParser(pydantic_object=JobKeyPoints)
        logger.debug("招聘岗位分析器初始化成功")

    def extract_job_description_html(self, jd_link: str) -> str:
        try:
            self.driver.get(jd_link)
            self.driver.implicitly_wait(10)
            body_element = self.driver.find_element(By.TAG_NAME, "body")
            body_element = body_element.get_attribute("outerHTML")
        except Exception as e:
            logger.error(f"解析招聘岗位HTML失败: {e}")
            raise e
        return body_element

    def analyze_job_description(self, jd_link: str):
        """分析步骤：
        1. 获取招聘岗位HTML
        2. 分析页面中岗位名称、岗位职责、招聘公司等信息
        3. 通过AI给出岗位职责的三大关键点
        """
        body = self.extract_job_description_html(jd_link)

        web_page_chain = (
            ChatPromptTemplate.from_template(parse_web_page_prompt)
            | self.llm
            | self.jd_parser
        )

        key_points_chain = (
            ChatPromptTemplate.from_template(jd_analyze_prompt)
            | self.llm
            | self.key_points_parser
        )

        logger.info("开始分析招聘岗位...")
        self.job_info = web_page_chain.invoke(
            {
                "html_content": body,
                "format_instructions": self.jd_parser.get_format_instructions(),
            }
        )

        logger.info("招聘岗位分析完成... 开始分析岗位关键点...")

        self.jd_key_points = key_points_chain.invoke(
            self.prepare_key_points_input(self.job_info)
        )
        logger.info("招聘岗位关键点分析完成...")

    def prepare_key_points_input(self, jd: JobDescription) -> Dict:
        return {
            "job_name": jd.job_name,
            "job_description": jd.job_description,
            "format_instructions": self.key_points_parser.get_format_instructions(),
        }

    @property
    def job_name(self) -> str:
        if not self.job_info:
            raise ValueError("Job info is not available")
        return self.job_info.job_name

    @property
    def job_description(self) -> str:
        if not self.job_info:
            raise ValueError("Job info is not available")
        return self.job_info.job_description

    @property
    def job_requirements(self) -> str:
        if not self.job_info:
            raise ValueError("Job info is not available")
        return self.job_info.job_requirements

    @property
    def job_location(self) -> str:
        if not self.job_info:
            raise ValueError("Job info is not available")
        return self.job_info.job_location

    @property
    def job_salary(self) -> str:
        if not self.job_info:
            raise ValueError("Job info is not available")
        return self.job_info.job_salary

    @property
    def company_name(self) -> str:
        if not self.job_info:
            raise ValueError("Job info is not available")
        return self.job_info.company_name

    @property
    def company_description(self) -> str:
        if not self.job_info:
            raise ValueError("Job info is not available")
        return self.job_info.company_description

    @property
    def key_points(self) -> list[str]:
        if not self.jd_key_points:
            raise ValueError("Job key points is not available")
        return self.jd_key_points.key_points

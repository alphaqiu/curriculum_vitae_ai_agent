from typing import List, Optional

import yaml
from loguru import logger
from pydantic import BaseModel, model_validator

from src.config import Config


class JobPreference(BaseModel):
    """求职意向信息类，包含职位、地点、薪资等求职相关信息"""

    position: str  # 期望职位
    location: str  # 期望工作地点
    salary: str  # 期望薪资
    industry: str  # 期望行业
    employment_type: str  # 工作类型（全职/兼职等）

    def __str__(self) -> str:
        return (
            f"  职位 = {self.position}\n"
            f"  地点 = {self.location}\n"
            f"  薪资 = {self.salary}\n"
            f"  行业 = {self.industry}\n"
            f"  类型 = {self.employment_type}\n"
        )


class ResumeProfile(BaseModel):
    """个人基本信息类，包含姓名、年龄、联系方式等基本信息"""

    name: str  # 姓名
    gender: str  # 性别
    age: int  # 年龄
    email: str  # 电子邮箱
    education_background: str  # 教育背景
    work_experience: str  # 工作经验
    github: Optional[str] = None  # github链接
    skills: Optional[str] = None  # 技能特长
    projects: Optional[str] = None  # 项目经验
    awards: Optional[str] = None  # 获奖情况
    mobile_phone: str  # 手机号码
    job_seeking_status: str  # 求职状态
    desired_positions: List[JobPreference]  # 求职意向列表

    @model_validator(mode="after")
    def validate_desired_positions(self) -> "ResumeProfile":
        """验证至少存在一个求职意向"""
        if not self.desired_positions:
            raise ValueError("At least one desired position is required")
        return self

    def __str__(self) -> str:
        result = [
            f"  姓名 = {self.name}",
            f"  性别 = {self.gender}",
            f"  年龄 = {self.age}",
            f"  邮箱 = {self.email}",
            f"  教育背景 = {self.education_background}",
            f"  工作经验 = {self.work_experience}",
            f"  手机号码 = {self.mobile_phone}",
            f"  求职状态 = {self.job_seeking_status}",
        ]
        if self.github:
            result.append(f"  个人github = {self.github}")
        if self.skills:
            result.append(f"  技能特长 = {self.skills}")
        if self.projects:
            result.append(f"  项目经验 = {self.projects}")
        if self.awards:
            result.append(f"  获奖情况 = {self.awards}")

        # 添加求职意向
        result.append("\n  求职意向:")
        for pos in self.desired_positions:
            pos_str = str(pos).replace("  ", "    ")  # 增加缩进级别
            result.append(pos_str)

        return "\n".join(result)


class EducationDetail(BaseModel):
    """教育经历详情类，包含学校、专业、学位等教育相关信息"""

    school: str  # 学校名称
    major: str  # 专业
    degree: str  # 学位
    start_date: str  # 入学时间
    graduation_date: str  # 毕业时间
    school_experience: Optional[str] = None  # 在校经历
    graduation_project_topic: Optional[str] = None  # 毕业设计题目
    graduation_project_description: Optional[str] = None  # 毕业设计描述

    def __str__(self) -> str:
        result = [
            f"  学校 = {self.school}",
            f"  专业 = {self.major}",
            f"  学位 = {self.degree}",
            f"  入学时间 = {self.start_date}",
            f"  毕业时间 = {self.graduation_date}",
        ]
        if self.school_experience:
            result.append(f"  在校经历 = {self.school_experience}")
        if self.graduation_project_topic:
            result.append(f"  毕业设计题目 = {self.graduation_project_topic}")
        if self.graduation_project_description:
            result.append(f"  毕业设计描述 = {self.graduation_project_description}")
        return "\n".join(result)


class WorkExperience(BaseModel):
    """工作经历类，包含公司、职位、工作内容等详细信息"""

    company: str  # 公司名称
    position: str  # 职位
    start_date: str  # 入职时间
    end_date: str  # 离职时间
    work_experience: str  # 工作经历
    work_experience_description: str  # 工作描述
    work_experience_achievements: Optional[str] = None  # 工作成就
    work_experience_skills: Optional[str] = None  # 使用的技能
    work_experience_projects: Optional[str] = None  # 参与的项目
    work_experience_awards: Optional[str] = None  # 获得的奖项
    tags: Optional[List[str]] = None  # 技能标签

    def __str__(self) -> str:
        result = [
            f"  公司 = {self.company}",
            f"  职位 = {self.position}",
            f"  入职时间 = {self.start_date}",
            f"  离职时间 = {self.end_date}",
            f"  工作经历 = {self.work_experience}",
            f"  工作描述 = {self.work_experience_description}",
        ]
        if self.work_experience_achievements:
            result.append(f"  工作成就 = {self.work_experience_achievements}")
        if self.work_experience_skills:
            result.append(f"  使用技能 = {self.work_experience_skills}")
        if self.work_experience_projects:
            result.append(f"  参与项目 = {self.work_experience_projects}")
        if self.work_experience_awards:
            result.append(f"  获得奖项 = {self.work_experience_awards}")
        if self.tags:
            result.append(f"  技能标签 = {', '.join(self.tags)}")
        return "\n".join(result)


class ProjectExperience(BaseModel):
    """项目经历类，包含项目名称、角色、时间等项目相关信息"""

    project_name: str  # 项目名称
    project_role: str  # 项目角色
    project_start_date: str  # 项目开始时间
    project_end_date: str  # 项目结束时间
    project_description: str  # 项目描述
    project_achievements: Optional[str] = None  # 项目成就
    project_link: Optional[str] = None  # 项目链接
    project_skills: Optional[str] = None  # 项目使用的技能

    def __str__(self) -> str:
        result = [
            f"  项目名称 = {self.project_name}",
            f"  项目角色 = {self.project_role}",
            f"  开始时间 = {self.project_start_date}",
            f"  结束时间 = {self.project_end_date}",
            f"  项目描述 = {self.project_description}",
        ]
        if self.project_achievements:
            result.append(f"  项目成就 = {self.project_achievements}")
        if self.project_link:
            result.append(f"  项目链接 = {self.project_link}")
        if self.project_skills:
            result.append(f"  使用技能 = {self.project_skills}")
        return "\n".join(result)


class QualificationCertificate(BaseModel):
    """资格证书类，包含证书名称、获得时间等证书相关信息"""

    certificate_name: str  # 证书名称
    certificate_date: str  # 获得时间
    certificate_link: Optional[str] = None  # 证书链接

    def __str__(self) -> str:
        result = [
            f"  证书名称 = {self.certificate_name}",
            f"  获得时间 = {self.certificate_date}",
        ]
        if self.certificate_link:
            result.append(f"  证书链接 = {self.certificate_link}")
        return "\n".join(result)


class VolunteerExperience(BaseModel):
    """志愿者经历类，包含志愿者经历名称、时间等志愿者经历相关信息"""

    volunteer_experience_name: str  # 志愿者经历名称
    start_date: str  # 志愿者经历开始时间
    end_date: str  # 志愿者经历结束时间
    service_duration: str  # 服务时长
    volunteer_experience_description: str  # 志愿者经历描述


class HobbiesAndInterests(BaseModel):
    """兴趣爱好类，包含兴趣爱好名称、时间等兴趣爱好相关信息"""

    hobbies_and_interests_name: str  # 兴趣爱好名称
    hobbies_and_interests_description: List[str]  # 兴趣爱好描述


class CurriculumVitae(BaseModel):
    """简历数据主类，包含所有个人信息、教育经历、工作经历等完整信息"""

    resume_profile: ResumeProfile  # 个人基本信息
    personal_advantage: List[str]  # 个人优势列表
    education_details: List[EducationDetail]  # 教育经历列表
    work_experience: List[WorkExperience]  # 工作经历列表
    project_experience: Optional[List[ProjectExperience]] = None  # 项目经验列表
    qualification_certificate: Optional[List[QualificationCertificate]] = (
        None  # 资格证书列表
    )
    volunteer_experience: Optional[List[VolunteerExperience]] = None  # 志愿者经历列表
    hobbies_and_interests: Optional[List[HobbiesAndInterests]] = None  # 兴趣爱好列表

    def __str__(self) -> str:
        sections = []

        # 个人信息
        sections.append("个人信息:")
        sections.append(str(self.resume_profile))

        # 个人优势
        sections.append("\n个人优势:")
        for advantage in self.personal_advantage:
            sections.append(f"  {advantage}")

        # 教育经历
        sections.append("\n教育经历:")
        sections.extend([str(edu) for edu in self.education_details])

        # 工作经历
        sections.append("\n工作经历:")
        sections.extend([str(work) for work in self.work_experience])

        # 项目经历
        if self.project_experience:
            sections.append("\n项目经历:")
            sections.extend([str(proj) for proj in self.project_experience])

        # 资格证书
        if self.qualification_certificate:
            sections.append("\n资格证书:")
            sections.extend([str(cert) for cert in self.qualification_certificate])

        # 志愿者经历
        if self.volunteer_experience:
            sections.append("\n志愿者经历:")
            sections.extend([str(vol) for vol in self.volunteer_experience])

        if self.hobbies_and_interests:
            sections.append("\n兴趣爱好:")
            sections.extend([str(hob) for hob in self.hobbies_and_interests])
        return "\n\n".join(sections)


def load_curriculum_vitae(config: Config) -> CurriculumVitae:
    """加载简历数据"""
    with open(config.get_resume_path(), "r", encoding="utf-8") as f:
        config_data = yaml.safe_load(f)
    logger.debug("简历数据加载成功")
    return CurriculumVitae(**config_data)

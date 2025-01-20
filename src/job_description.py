from pydantic import BaseModel, Field


class JobDescription(BaseModel):
    """职位信息数据模型"""

    job_name: str = Field(description="职位名称")
    job_description: str = Field(description="职位描述")
    job_requirements: str = Field(description="职位要求")
    job_location: str = Field(description="工作地点")
    job_salary: str = Field(description="薪资范围")
    company_name: str = Field(description="公司名称")
    company_description: str = Field(description="公司简介")


class JobKeyPoints(BaseModel):
    """职位关键点数据模型"""

    key_points: list[str] = Field(description="职位描述中最重要的三个关键点")

    def __str__(self):
        return "\n".join("- " + point for point in self.key_points)

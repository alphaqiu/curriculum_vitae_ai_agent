from enum import Enum
from pathlib import Path

import yaml
from dotenv import load_dotenv
from pydantic import BaseModel, Field, model_validator


class LLMProvider(str, Enum):
    """模型使用选择
    值是选用的模型名称
    """

    Tongyi = "qwen-plus"
    ChatGPT = "gpt-4o"
    Claude = "claude-3-5-sonnet-20240620"
    Google = "gemini-1.5-flash-latest"
    DeepSeek = "deepseek-chat"
    OLLAMA = "qwen2.5"


class Config(BaseModel):
    """配置类"""

    task_path: str = Field(
        description="任务文件路径，包含cv.yml,secrets.yml,config.yml和resume_template目录",
        default="./data",
    )
    resume_file_name: str = Field(description="简历文件", default="info.yml")
    model_provider: LLMProvider = Field(
        description="模型使用选择", default=LLMProvider.Tongyi
    )

    @model_validator(mode="after")
    def validate_resume_file_exists(self) -> "Config":
        """验证简历文件是否存在"""
        resume_path = Path(self.task_path) / self.resume_file_name
        if not resume_path.exists():
            raise ValueError(f"Resume file {resume_path} does not exist")
        return self

    def get_resume_path(self) -> Path:
        return Path(self.task_path) / self.resume_file_name


def load_config(config_path: str) -> Config:
    """加载配置, 并从.env文件中加载环境变量"""
    load_dotenv()
    with open(config_path, "r", encoding="utf-8") as f:
        config_data = yaml.safe_load(f)
    return Config(**config_data)

from langchain_community.chat_models.tongyi import ChatTongyi
from langchain_core.language_models.chat_models import BaseChatModel
from langchain_ollama import ChatOllama
from langchain_openai import ChatOpenAI
from loguru import logger

from src.config import Config, LLMProvider


def get_llm(config: Config, *args, **kwargs) -> BaseChatModel:
    class ChatDeepSeek(ChatOpenAI):
        def __init__(
            self,
            model=config.model_provider.value,
            base_url="https://api.deepseek.com/v1",
            *args,
            **kwargs,
        ):
            super().__init__(model=model, base_url=base_url, *args, **kwargs)

    match config.model_provider:
        case LLMProvider.DeepSeek:
            logger.info("使用DeepSeek的API")
            return ChatDeepSeek(*args, **kwargs)
        case LLMProvider.Tongyi:
            logger.info("使用阿里云的API")
            return ChatTongyi(model=config.model_provider.value, *args, **kwargs)
        case _:  # use local ollama
            logger.info("使用本地ollama API")
            return ChatOllama(model=LLMProvider.OLLAMA.value, *args, **kwargs)

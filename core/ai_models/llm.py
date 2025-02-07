import ollama
from typing import List, Dict
from voice_assistant.config.settings import settings
from voice_assistant.utils.exceptions import LLMException


class LLMClient:
    def __init__(self):
        self.history: List[Dict] = []

    def chat(self, prompt: str, temperature: float = 0.7) -> str:
        """带历史上下文的对话"""
        try:
            self.history.append({"role": "user", "content": prompt})

            response = ollama.chat(
                model=settings.llm_model,
                messages=self.history[-5:],  # 保留最近5条上下文
                options={"temperature": temperature}
            )

            reply = response["message"]["content"]
            self.history.append({"role": "assistant", "content": reply})
            return reply

        except ollama.ResponseError as e:
            raise LLMException(f"模型响应错误: {e.error}") from e
        except ConnectionError as e:
            raise LLMException("连接大模型服务失败") from e

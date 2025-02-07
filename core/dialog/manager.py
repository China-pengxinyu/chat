from .history import ConversationHistory
from .emotion import EmotionAnalyzer
from voice_assistant.config.settings import settings


class DialogManager:
    def __init__(self):
        self.history = ConversationHistory(max_length=settings.max_history_length)
        self.emotion_analyzer = EmotionAnalyzer()

    def process(self, user_input):
        # 添加用户输入到历史
        self.history.add("user", user_input)

        # 生成回复
        response = self._generate_response(user_input)

        # 分析情感
        emotion = self.emotion_analyzer.analyze(response)

        # 添加AI回复到历史
        self.history.add("assistant", response)

        return response, emotion

    def _generate_response(self, prompt):
        # 调用LLM生成回复
        # （实际实现需集成LLM模块）
        return "这是测试回复"

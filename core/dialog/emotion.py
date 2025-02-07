class EmotionAnalyzer:
    def analyze(self, text):
        # 简单实现，实际应调用LLM
        if "开心" in text:
            return "happy"
        elif "生气" in text:
            return "angry"
        return "neutral"

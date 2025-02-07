from collections import deque


class ConversationHistory:
    def __init__(self, max_length=5):
        self.history = deque(maxlen=max_length)

    def add(self, role, content):
        self.history.append({"role": role, "content": content})

    def get_context(self):
        return list(self.history)

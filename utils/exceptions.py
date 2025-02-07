class AssistantException(Exception):
    """基础异常类"""
    def __init__(self, message: str, code: int = 1000):
        super().__init__(message)
        self.code = code

class AudioException(AssistantException):
    """音频相关异常"""
    def __init__(self, message: str = "音频处理错误", code: int = 2000):
        super().__init__(message, code)

class DeviceNotFoundError(AudioException):
    """硬件设备未找到"""
    def __init__(self, device: str):
        super().__init__(f"音频设备 {device} 未找到", 2001)

class SynthesisException(AssistantException):
    """语音合成异常"""
    def __init__(self, message: str = "语音生成失败", code: int = 3000):
        super().__init__(message, code)

class APITimeout(SynthesisException):
    """API请求超时"""
    def __init__(self):
        super().__init__("语音合成API响应超时", 3001)

class LLMException(AssistantException):
    """大模型交互异常"""
    def __init__(self, message: str = "大模型服务错误", code: int = 4000):
        super().__init__(message, code)

class RecognitionException(AssistantException):
    """语音识别异常"""
    def __init__(self, message: str = "语音识别失败", code: int = 5000):
        super().__init__(message, code)


class FileNotFoundError:
    pass
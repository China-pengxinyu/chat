from dataclasses import dataclass


@dataclass
class AppSettings:
    # 音频参数
    sample_rate: int = 16000
    vad_aggressiveness: int = 3
    silence_timeout: float = 0.4  # 秒

    # 模型参数
    whisper_model: str = "large-v2"
    llm_model: str = "deepseek-r1"

    # 服务配置
    sovits_api: str = "http://localhost:9874"

    # 路径配置
    ref_audio_dir: str = "voices"
    log_file: str = "assistant.log"


settings = AppSettings()

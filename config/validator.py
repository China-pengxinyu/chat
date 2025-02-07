import os
from .settings import settings
from ..utils.exceptions import DeviceNotFoundError


def validate_config():
    """启动前配置验证"""
    # 验证音频目录
    if not os.path.exists(settings.ref_audio_dir):
        os.makedirs(settings.ref_audio_dir, exist_ok=True)

    # 验证参考音频
    default_voice = os.path.join(settings.ref_audio_dir, "default.wav")
    if not os.path.exists(default_voice):
        raise FileNotFoundError(f"默认音色文件 {default_voice} 不存在")

    # 验证录音设备
    try:
        import sounddevice as sd
        devices = sd.query_devices()
        if len(devices) == 0:
            raise DeviceNotFoundError("默认输入设备")
    except Exception as e:
        raise DeviceNotFoundError("音频设备初始化失败") from e

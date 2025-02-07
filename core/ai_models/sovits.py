import requests
from voice_assistant.config.settings import settings
from voice_assistant.config.constants import EMOTION_MAP
from voice_assistant.utils.exceptions import SynthesisException


class VoiceSynthesizer:
    def synthesize(self, text, emotion="neutral"):
        params = {
            "text": text,
            "style": EMOTION_MAP.get(emotion, "default"),
            "ref_audio_path": settings.ref_audio_dir + "/default.wav"
        }

        try:
            response = requests.post(
                f"{settings.sovits_api}/voice",
                json=params,
                timeout=30
            )
            if response.status_code == 200:
                return response.content
            raise SynthesisException("API返回错误")
        except Exception as e:
            raise SynthesisException("语音合成失败") from e

from faster_whisper import WhisperModel
from voice_assistant.config.settings import settings
from utils.exceptions import RecognitionException


class SpeechRecognizer:
    def __init__(self):
        self.model = WhisperModel(
            settings.whisper_model,
            device="cuda" if torch.cuda.is_available() else "cpu"
        )

    def transcribe(self, audio_data):
        try:
            segments, _ = self.model.transcribe(audio_data, vad_filter=True)
            return " ".join(segment.text for segment in segments)
        except Exception as e:
            raise RecognitionException("语音识别失败") from e

import sounddevice as sd
import numpy as np
import webrtcvad
from utils.exceptions import AudioException
from voice_assistant.config.settings import settings

class AudioRecorder:
    def __init__(self):
        self.sample_rate = settings.sample_rate
        self.vad = webrtcvad.Vad(settings.vad_aggressiveness)
        self.silence_frames = int(settings.silence_timeout * self.sample_rate / 160)

    def capture(self) -> np.ndarray:
        """带实时反馈的语音激活录音"""
        buffer = []
        silence_count = 0
        print("\n🎤 请开始说话...", end="", flush=True)

        try:
            with sd.InputStream(
                    samplerate=self.sample_rate,
                    channels=1,
                    dtype="int16",
                    blocksize=160
            ) as stream:
                while True:
                    data, _ = stream.read(160)
                    buffer.append(data)

                    if self.vad.is_speech(data.tobytes(), self.sample_rate):
                        print("▮", end="", flush=True)
                        silence_count = 0
                    else:
                        silence_count += 1
                        if silence_count > self.silence_frames:
                            break

            return np.concatenate(buffer)
        except sd.PortAudioError as e:
            raise AudioException("麦克风访问失败") from e

    def save_audio(self, audio_data: np.ndarray, filename: str):
        """将音频数据保存到文件"""
        sd.write(filename, audio_data, self.sample_rate)

    def play_audio(self, audio_data: np.ndarray):
        """播放音频数据"""
        sd.play(audio_data, self.sample_rate)
        sd.wait()

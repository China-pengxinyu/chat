from pydub import AudioSegment
from pydub.playback import play
from voice_assistant.utils.exceptions import AudioException

class AudioPlayer:
    @staticmethod
    def play_from_file(file_path):
        try:
            audio = AudioSegment.from_file(file_path)
            play(audio)
        except Exception as e:
            raise AudioException(f"播放失败: {str(e)}") from e

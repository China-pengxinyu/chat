from typing import Optional
from core.audio.recorder import AudioRecorder
from core.audio.player import AudioPlayer
from core.ai_models.whisper import SpeechRecognizer
from core.ai_models.llm import LLMClient
from core.ai_models.sovits import VoiceSynthesizer
from core.dialog.manager import DialogManager
from config.settings import settings
from utils.logger import logger


class VoiceAssistantService:
    def __init__(self):
        # 初始化组件
        self.recorder = AudioRecorder()
        self.player = AudioPlayer()
        self.recognizer = SpeechRecognizer()
        self.llm = LLMClient()
        self.synthesizer = VoiceSynthesizer()
        self.dialog = DialogManager()

        # 状态标志
        self.is_running = False

    def start(self):
        """启动语音助手服务"""
        self.is_running = True
        logger.info("语音助手服务已启动")

        try:
            while self.is_running:
                self._process_interaction()
        except KeyboardInterrupt:
            self.stop()
        except Exception as e:
            logger.error(f"服务异常终止: {str(e)}")
            raise

    def _process_interaction(self):
        """处理单次交互流程"""
        try:
            # 录音
            audio_data = self.recorder.capture()
            if audio_data.size == 0:
                return

            # 识别
            text = self.recognizer.transcribe(audio_data)
            if not text:
                logger.warning("未识别到有效语音")
                return

            # 生成回复
            response, emotion = self.dialog.process(text)

            # 合成语音
            audio = self.synthesizer.synthesize(response, emotion)

            # 播放
            self.player.play(audio)

        except Exception as e:
            logger.error(f"交互流程异常: {str(e)}")
            self._handle_error(e)

    def stop(self):
        """安全停止服务"""
        self.is_running = False
        logger.info("正在停止服务...")
        # 清理资源
        self.recorder = None
        self.player = None

    def _handle_error(self, error: Exception):
        """错误处理策略"""
        # TODO: 实现错误恢复逻辑
        pass

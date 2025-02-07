from services.voice_service import VoiceAssistantService
from config.validator import validate_config
from utils.custom_logger import setup_logger
from utils.exceptions import DeviceNotFoundError, FileNotFoundError, Exception


def main():
    # 初始化系统
    logger = setup_logger("Main")

    try:
        # 配置验证
        validate_config()

        # 启动服务
        logger.info("=== 语音助手启动中 ===")
        assistant = VoiceAssistantService()
        assistant.start()

    except DeviceNotFoundError as e:
        logger.error(f"硬件错误: {str(e)}")
    except FileNotFoundError as e:
        logger.error(f"配置文件错误: {str(e)}")
    except Exception as e:
        logger.critical(f"未处理的异常: {str(e)}", exc_info=True)
    finally:
        logger.info("=== 服务已停止 ===")


if __name__ == "__main__":
    main()

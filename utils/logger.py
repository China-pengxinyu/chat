import logging
import config.settings as settings  # 确保正确导入 settings.py

def setup_logger(name):
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )

    # 文件日志
    file_handler = logging.FileHandler(settings.log_file)
    file_handler.setFormatter(formatter)

    # 控制台日志
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger

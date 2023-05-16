# -*- coding: utf-8 -*-
from os import path, remove
import logging.config
from sys import platform, argv

try:
    from .lib.parser import ParserAniLibria
    from .lib.model import ModelAniLibria
    from .lib.view import View
    from .lib.router import router
except ImportError:
    from source.develop.xrenb_tv.resources.lib.parser import ParserAniLibria
    from source.develop.xrenb_tv.resources.lib.model import ModelAniLibria
    from source.develop.xrenb_tv.resources.lib.view import View
    from source.develop.xrenb_tv.resources.lib.router import router

id_a: str = argv[0].split("//")[1].split("/")[0]

if platform == "linux" or platform == "linux2":
    kodi_path = path.join(
        "$HOME",
        ".kodi",
        "temp",
        id_a + ".log"
    )
elif platform == "darwin":
    # OS X
    kodi_path = path.join(
        "Users",
        "<username>",
        "Library",
        "Logs",
        id_a + ".log"
    )
elif platform == "win32":
    kodi_path = path.join(
        "%LOCALAPPDATA%",
        "Packages",
        "XBMCFoundation.Kodi_4n2hpmxwrvr6p",
        "LocalCache",
        "Roaming",
        "Kodi",
        id_a + ".log"
    )
else:
    kodi_path = 0
if kodi_path:
    log = path.expandvars(kodi_path)
    # Удалите существующий файл лога, если он есть, чтобы создавать новый файл во время каждого выполнения
    if path.isfile(log):
        remove(log)

    if View().get_setting("log") == "true":
        # Создайте Logger
        logger = logging.getLogger(__name__)
        logger.setLevel(logging.DEBUG)

        # Создайте обработчик для записи данных в файл
        logger_handler = logging.FileHandler(log)
        logger_handler.setLevel(logging.DEBUG)

        # Создайте Formatter для форматирования сообщений в логе
        logger_formatter = logging.Formatter("%(asctime)s - %(name)s - %(lineno)d - %(funcName)s - %(levelname)s - %(message)s")

        # Добавьте Formatter в обработчик
        logger_handler.setFormatter(logger_formatter)

        # Добавте обработчик в Logger
        logger.addHandler(logger_handler)
        logger.info("Логи удаляются при повторном запуске")

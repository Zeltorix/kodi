# -*- coding: utf-8 -*-
# Module: addon
# Author: Zeltorix
# Created on: 2023.01.14
# License: GPL v.3 https://www.gnu.org/copyleft/gpl.html
"""
Плагин для KODI 19.x "Matrix" и выше.
"""

import sys
from resources.lib import router

if __name__ == '__main__':
    # Вызовите функцию маршрутизатора и передайте ей параметры вызова плагина.
    # Мы используем нарезку строк, чтобы обрезать начальную строку '?' из paramstring вызова плагина
    # Пример:
    # sys.argv
    # plugin://plugin.video.zeltorix.anilibria/?router=play&video=https://cache.libria.fun/videos/media/ts/9286/10/720/be20bca54b076a9131aca90e8f7c537e.m3u8
    # sys.argv[2]
    # plugin.video.zeltorix.anilibria/?router=play&video=https://cache.libria.fun/videos/media/ts/9286/10/720/be20bca54b076a9131aca90e8f7c537e.m3u8
    # sys.argv[2][1:]
    # ?router=play&video=https://cache.libria.fun/videos/media/ts/9286/10/720/be20bca54b076a9131aca90e8f7c537e.m3u8
    # Для дальнейшего
    #     {
    #       "router": "play"
    #       "video": "https://cache.libria.fun/videos/media/ts/9286/10/720/be20bca54b076a9131aca90e8f7c537e.m3u8"
    #     }
    # Остальные примеры слишком большие
    router.router(sys.argv[2][1:])

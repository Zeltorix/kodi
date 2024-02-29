# -*- coding: utf-8 -*-
# Module: addon
# Author: Zeltorix
# Created on: 2023.07.17
# License: GPL v.3 https://www.gnu.org/copyleft/gpl.html
"""
Плагин для KODI 19.x "Matrix" и выше.
Не тестируемый файл
"""

import sys

from view import View

from resources.lib.router import router
from resources.lib.auth import Auth


if __name__ == '__main__':
    View().check_modules()
    Auth().token_new()
    router(sys.argv[2][1:])

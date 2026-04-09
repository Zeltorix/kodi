# -*- coding: utf-8 -*-
# Module: addon
# Author: Zeltorix
# Created on: 2023.12.07
# License: GPL v.3 https://www.gnu.org/copyleft/gpl.html
"""
Плагин для KODI 19.x "Matrix" и выше.
Не тестируемый файл
"""

import sys
from resources.lib.router import router
from view import View

if __name__ == '__main__':
    View().check_modules()
    router(sys.argv[2][1:])

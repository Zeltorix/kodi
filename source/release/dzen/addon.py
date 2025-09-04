# -*- coding: utf-8 -*-
# Module: addon
# Author: Zeltorix
# Created on: 2024.03.21
# License: GPL v.3 https://www.gnu.org/copyleft/gpl.html
"""
Плагин для KODI 19.x "Matrix" и выше.
Не тестируемый файл
"""

import sys
from resources.lib.router import router

if __name__ == '__main__':
    router(sys.argv[2][1:])

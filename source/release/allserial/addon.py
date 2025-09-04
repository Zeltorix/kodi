# -*- coding: utf-8 -*-
# Module: addon
# Author: Zeltorix
# Created on: 2023.09.13
# License: GPL v.3 https://www.gnu.org/copyleft/gpl.html
"""
Плагин для KODI 19.x "Matrix" и выше.
Не тестируемый файл
"""

import sys

from view import View

from resources.lib.router import router
from resources.lib.library import Library


if __name__ == '__main__':
    _view = View()
    _library = Library()

    _view.check_modules()
    _library.default()
    router(sys.argv[2][1:])

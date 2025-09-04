# -*- coding: utf-8 -*-
# Module: addon
# Author: Zeltorix
# Created on: 2023.03.01
# License: GPL v.3 https://www.gnu.org/copyleft/gpl.html
"""
Плагин для KODI 19.x "Matrix" и выше.
Не тестируемый файл
"""
# Стандартные библиотеки
from sys import argv

# Модули плагина
from resources.lib.router import router


if __name__ == '__main__':
    router(argv[2][1:])

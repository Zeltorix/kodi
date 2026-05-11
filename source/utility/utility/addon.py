# -*- coding: utf-8 -*-
# Module: addon
# Author: Zeltorix
# Created on: 2023.02.25
# License: GPL v.3 https://www.gnu.org/copyleft/gpl.html
"""
Плагин для KODI 19.x "Matrix" и выше.

"""
import os
import sys
from urllib.parse import parse_qsl

sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'resources', 'lib'))
from web_api_request import Proxy
from view import View


if __name__ == '__main__':
    def router(data_string: str) -> None:
        try:
            params_dict: dict = dict(parse_qsl(data_string))
        except TypeError:
            raise TypeError(f'Нельзя представить как словарь: {data_string}')
        _view = View()
        if params_dict:
            if params_dict["router"] == "proxy_provider_reload":
                if Proxy().proxy_provider_reload():
                    _view.dialog_ok("Прокси", "Поставщик прокси обновлён")
        else:
            _view.open_settings()

            # _view.output({
            #     "list": [
            #         {
            #             "title": "Здесь ни чего интересного пока нет.",
            #         },
            #     ]
            # })


    router(sys.argv[2][1:])

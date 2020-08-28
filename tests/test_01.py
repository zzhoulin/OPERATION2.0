# -*- coding: utf-8 -*-
# @Author : Joy

import requests
import pytest
from Common.commlib import get_test_data


cases, list_params = get_test_data("D:/TestProject/Operation2.0/data/test_02.yaml")


class Test_01(object):
    @pytest.mark.parametrize("case,http,excepted", list(list_params), ids=cases)
    def test_01(self, case, http, excepted):
        host = "http://test.feiyuanenv.com:8830"
        r = requests.request(http["method"],
                             url=host + http["path"],
                             headers=http["headers"],
                             params=http["params"])
        response = r.json()
        assert response["body"] == excepted['response']["name"]
        assert response["body"]["username"] == excepted['response']["username"]


# -*- coding: utf-8 -*-
# filename: main.py
"""
聚合数据接口
"""
import sys
reload(sys)
sys.setdefaultencoding('utf8')  # 编译环境utf8
# import time
# from purl import URL
import requests
import json
from mengbao_private_conf import juhe_url_randn_joke


class Juhe(object):
    def __init__(self):
        pass

    def get_joke(self):
        """获取随机笑话"""
        try:
            resp = requests.get(juhe_url_randn_joke)
            if resp.ok:
                jokes = self._parse_joke(resp.content)
                return jokes
            else:
                return 'get_joke()解析错误<003>: %s' % resp.status_code
        except:
            return 'get_joke()请求错误<004>'

    @staticmethod
    def _parse_joke(resp_content):
        try:
            ret = json.loads(resp_content)
            if ret['reason'] == 'success':
                return '\n----------\n'.join([i['content'] for i in ret['result']])
            else:
                return u'_parse_joke()解析错误<001>'
        except:
                return u'_parse_joke()解析错误<002>'



if __name__ == '__main__':
    jh = Juhe()
    print jh.get_joke()

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
from mengbao_private_conf import juhe_url_randn_joke, juhe_url_new_joke
import random

class Juhe(object):
    def __init__(self):
        pass

    def get_joke(self, typ='new'):
        """获取随机笑话"""
        try:
            if typ == 'new':
                resp = requests.get(juhe_url_new_joke)
                if resp.ok:
                    jokes = self._parse_new_joke(resp.content)
                    return jokes
                else:
                    return 'get_joke()解析错误<003>: %s' % resp.status_code
            elif typ == 'randn':
                resp = requests.get(juhe_url_randn_joke)
                if resp.ok:
                    jokes = self._parse_randn_joke(resp.content)
                    return jokes
                else:
                    return 'get_joke()解析错误<005>: %s' % resp.status_code
        except:
            raise
            return 'get_joke()请求错误<004>'

    @staticmethod
    def _parse_randn_joke(resp_content):
        try:
            ret = json.loads(resp_content)
            if ret['reason'].lower() == 'success':
                return random.choice(ret['result'])['content'].strip()
                # return '\n----------\n'.join([i['content'] for i in results])
            else:
                return u'_parse_randn_joke()解析错误<003>'
        except:
            raise
            return u'_parse_randn_joke()解析错误<004>'



    @staticmethod
    def _parse_new_joke(resp_content):
        try:
            ret = json.loads(resp_content)
            if ret['reason'].lower() == 'success':
                return '\n----------\n'.join([i['content'].strip() for i in ret['result']['data']])
            else:
                return u'_parse_new_joke()解析错误<001>'
        except:
                return u'_parse_new_joke()解析错误<002>'



if __name__ == '__main__':
    ju = Juhe()
    jokes = ju.get_joke('new')
    print jokes
    jokes = ju.get_joke('randn')
    print jokes
    del ju

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
from mengbao_private_conf import juhe_url_robot_model
import random

class Juhe(object):
    def __init__(self):

        pass

    def get_robot(self, info):
        """问答机器人
        {
            "reason":"成功的返回",
            "result": /*根据code值的不同，返回的字段有所不同*/
                {
                    "code":100000, /*返回的数据类型，请根据code的值去数据类型API查询*/
                    "text":"你好啊，希望你今天过的快乐"
                },
             "error_code":0
        }"""
        # http://op.juhe.cn/robot/index?info=你好&key=您申请到的APPKEY
        url = juhe_url_robot_model % {'info': info}
        try:
            resp = requests.get(url)
            if resp.ok:
                answer = json.loads(resp.content)
                return answer['result']['text']
            else:
                return resp.content
        except:
            return 'get_robot()请求错误<005>'



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
            # raise
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
    answer = ju.get_robot('你好')
    print answer
    answer = ju.get_robot('北京天气')
    print answer
    del ju

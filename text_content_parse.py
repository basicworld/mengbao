# -*- coding: utf-8 -*-
"""
解析文本消息内容
可能是：英汉翻译、天气、笑话、手机归属地、身份证归属地、快递单号
"""
import re
import sys
reload(sys)
sys.setdefaultencoding('utf8')  # 编译环境utf8


help_info = u'''\
功能示例
【手机归属】
15311448899
归属地15311448899
gsd15311448899\
'''
from Account import MysqlQuery

def text_parse(content, **kwargs):
    """处理"""
    content.strip()
    # 检测是否为手机号
    _copy = content
    if _copy.startswith(u'归属地') or _copy.startswith(u'gsd'):
        _copy = _copy[3:].strip()
    if _copy.startswith('+86'):
        _copy = _copy[3:]
    _copy = re.sub(r' |-', '', _copy)
    if _copy.isalnum() and len(_copy) == 11 and _copy[0] == '1':
        my = MysqlQuery()
        resp = my.query_phone(_copy)
        del my
        return resp
    else:
        return help_info

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
1. 查询手机归属地
15311448899
手机15311448899
sj15311448899
(至少输入手机号前7位)

2. 查询身份证归属地
身份证110100199212303410
sfz110100199212303410
(至少输入身份证前6位)\

3. 看笑话
xh
joke
笑话
'''
from Account import MysqlQuery
from Juhe import Juhe


def text_parse(content, **kwargs):
    """处理文本"""
    content = content.strip()
    # 如果是笑话，则调用聚合数据
    if content in [u'笑话', 'xh', 'joke']:
        ju = Juhe()
        jokes = ju.get_joke()
        del ju
        return jokes

    # 检测是否为手机号, 如果是则返回归属地
    _copy = content.lower()
    if _copy.startswith(u'手机') or _copy.startswith(u'sj'):
        _copy = _copy[2:].strip()
    if _copy.startswith('+86'):
        _copy = _copy[3:]
    _copy = re.sub(r' |-', '', _copy)
    if _copy.isalnum() and len(_copy) >= 7 and _copy[0] == '1':
        my = MysqlQuery()
        resp = my.query_phone(_copy)
        del my
        return resp

    # 检测是否为身份证号，如果是则返回归属地
    _copy = content.lower()
    if _copy.startswith(u'身份证') or _copy.startswith(u'sfz'):
        _copy = _copy[3:].strip()
    _copy = re.sub(r' |-', '', _copy)
    if _copy.isalnum() and len(_copy) >= 6:
        my = MysqlQuery()
        resp = my.query_idcard(_copy)
        del my
        return resp

    return help_info

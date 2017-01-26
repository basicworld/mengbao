# -*- coding: utf-8 -*-
"""
解析文本消息内容
可能是：英汉翻译、天气、笑话、手机归属地、身份证归属地、快递单号
"""


def text_parse(content):
    """处理"""
    # 检测是否为手机号
    if content.isalnum() and len(content) == 11:
        return u'手机号'

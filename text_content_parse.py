# -*- coding: utf-8 -*-
"""
解析文本消息内容
可能是：英汉翻译、天气、笑话、手机归属地、身份证归属地、快递单号
"""


def text_parse(content):
    """处理"""
    # 检测是否为手机号
    if content.isalnum() and len(content) == 11:
<<<<<<< HEAD
        return u'手机号'
    else:
        return u'未识别的文本信息'
=======
        return u'这或许是个手机号'
    else:
        return u'哎呀我还不认识，我回去再多读点书'
>>>>>>> d9aa4c202ccf2ff9a8bad5e08baff5bfdca38157

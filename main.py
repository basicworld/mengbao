# -*- coding: utf-8 -*-
# filename: main.py
"""
主框架，主文件
"""
from text_content_parse import text_parse
# wechat-sdk setting start
from mengbao_private_conf import *
from wechat_sdk import WechatConf
conf = WechatConf(
    token=mbtoken,
    appid=mbappid,
    appsecret=mbappsecret,
    encrypt_mode=mbencrypt_mode,  # 可选项：normal/compatible/safe，分别对应于 明文/兼容/安全 模式
    encoding_aes_key=mbencoding_aes_key,  # 如果传入此值则必须保证同时传入 token, appid
)

from wechat_sdk import WechatBasic
from wechat_sdk.exceptions import ParseError  # 用于接收消息
# 消息类型
from wechat_sdk.messages import TextMessage  # (文本消息类),
# from wechat_sdk.messages import ImageMessage  # (图片消息类),
# from wechat_sdk.messages import VideoMessage  # (视频消息类),
# from wechat_sdk.messages import LocationMessage  # (位置消息类),
# from wechat_sdk.messages import LinkMessage  # (链接消息类),
# from wechat_sdk.messages import EventMessage  # (事件消息类),
# from wechat_sdk.messages import VoiceMessage  # (语音消息类)

wechat = WechatBasic(conf=conf)
# wechat-sdk setting end

# flask setting start
from flask import Flask
from flask import request
app = Flask(__name__)

@app.route('/wx', methods=['GET', 'POST'])
def handle():
    # return 'hello world'
    # 验证消息来源，api接入
    if request.method=='GET':
        try:
            signature = request.args.get('signature', '')
            timestamp = request.args.get('timestamp', '')
            nonce = request.args.get('nonce', '')
            echostr = request.args.get('echostr', '')
            # print (signature, timestamp, nonce)
            if wechat.check_signature(signature, timestamp, nonce):
                # print echostr
                return echostr  # 正确消息时，返回该值
            else:
                return 'Wrong'
        except:
            return 'Wrong'

    # 回复消息
    if request.method == 'POST':
        try:
            body_text = request.content
            wechat.parse_data(body_text)

            # msg_id = wechat.message.id          # 对应于 XML 中的 MsgId
            # msg_target = wechat.message.target  # 对应于 XML 中的 ToUserName
            # msg_source = wechat.message.source  # 对应于 XML 中的 FromUserName
            # msg_time = wechat.message.time      # 对应于 XML 中的 CreateTime
            # msg_type = wechat.message.type      # 对应于 XML 中的 MsgType
            # msg_raw = wechat.message.raw        # 原始 XML 文本，方便进行其他分析

            if isinstance(wechat.message, TextMessage):
                # 处理文字消息
                receive_content = wechat.message.content  # 接收的消息
                # 消息处理
                response_content = text_parse(receive_content)
                # 构建微信xml
                xml = wechat.response_text(content=response_content)
                return xml
            else:
                # 其他消息类型暂不处理
                return u'开发中,敬请期待...'
        except ParseError:
            print 'Invalid Body Text'


if __name__ == '__main__':
    app.run(port='8008')

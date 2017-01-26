# -*- coding: utf-8 -*-
# filename: main.py

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
wechat = WechatBasic(conf=conf)
# wechat-sdk setting end

# flask setting start
from flask import Flask
from flask import request
app = Flask(__name__)

@app.route('/wx', methods=['GET', 'POST'])
def handle():
    # return 'hello world'
    if request.method=='GET':
        signature = request.args.get('signature', '')
        timestamp = request.args.get('timestamp', '')
        nonce = request.args.get('nonce', '')
        echostr = request.args.get('echostr', '')
        if wechat.check_signature(signature, timestamp, nonce):
            return echostr
        else:
            return 'Wrong'


if __name__ == '__main__':
    app.run(port='8008')

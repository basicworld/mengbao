# -*- coding: utf-8 -*-
# filename: main.py
from flask import Flask
app = Flask(__name__)


@app.route('/wx')
def hello_world():
    return 'hello world'


if __name__ == '__main__':
    app.run(port='8008')

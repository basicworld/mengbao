# -*- coding: utf-8 -*-
"""

"""
import os
import sys
reload(sys)
sys.setdefaultencoding('utf8')  # 编译环境utf8
ROOT_DIR = os.path.realpath(os.path.dirname(__file__))


if __name__ == '__main__':
    print ROOT_DIR

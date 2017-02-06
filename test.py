# -*- coding: utf-8 -*-

import re
import sys
reload(sys)
sys.setdefaultencoding('utf8')  # 编译环境utf8


from text_content_parse import text_parse

if __name__ == '__main__':
    print text_parse('test')
    print text_parse('你好')

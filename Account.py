# -*- coding: utf-8 -*-
# filename: main.py
"""
一些账户类
"""
import sys
reload(sys)
sys.setdefaultencoding('utf8')  # 编译环境utf8
import MySQLdb as mdb
import sys

sql_query_words_model = """
SELECT *
from Words w
where w.word='%(word)s';"""

sql_query_phone_model = """
select m.MobileNumber,
m.MobileType,
m.MobileArea,
m.AreaCode
from Mobile m
where TRUE
and m.MobileNumber='%(phone)s';
"""
str_query_phone_model = u"""\
手机号字段: %s
手机号类型: %s
手机号归属地: %s
归属地区号: %s\
"""
sql_query_idcard_model = u'''
select i.`Zone`, i.`Desc`
from IDCard i
where TRUE
and i.Zone='%(idcard)s';'''
str_query_idcard_model = u"""\
身份证字段: %s
身份证归属地: %s
"""
sql_error_model = "未查询到相关信息"

class MysqlQuery(object):
    def __init__(self, host='localhost', user='wechat', passwd='', dbname='mengbao'):
        # try:
        self.con = mdb.connect(host, user, passwd, dbname)
        self.cur = self.con.cursor()

    def __del__(self):
        self._close()

    def __exit__(self):
        self._close()

    def _close(self):
        if self.con:
            self.con.close()

    def query_phone(self, phone):
        phone = self._get_head(phone)
        sql = sql_query_phone_model % {'phone': phone}
        try:
            self.cur.execute(sql)
            que = self.cur.fetchone()
            return (str_query_phone_model % que) if que else sql_error_model
        except mdb.Error, e:
            return "Error %d: %s" % (e.args[0], e.args[1])

    def query_idcard(self, idcard):
        idcard = self._get_head(idcard, 6)
        sql = sql_query_idcard_model % {'idcard': idcard}
        try:
            self.cur.execute(sql)
            que = self.cur.fetchone()
            return (str_query_idcard_model % que) if que else sql_error_model
        except mdb.Error, e:
            return "Error %d: %s" % (e.args[0], e.args[1])

    def query_word(self, word):
        """英汉字典"""
        # 如果不是英文单词，返回False
        if (not word.isalpha()) or word.isdigit():
            return False
        try:
            sql = sql_query_words_model % {'word': word}
            self.cur.execute(sql)
            que = self.cur.fetchone()
            if que:
                return que[-1]
            elif not word.islower():
                sql = sql_query_words_model % {'word': word.lower()}
                self.cur.execute(sql)
                que = self.cur.fetchone()
                # return que[-1]
                return (str_query_words_model % que) if que else False
            else:
                return False
        except mdb.Error, e:
            return "Error %d: %s" % (e.args[0], e.args[1])

    def _test(self):
        self.cur.execute("SELECT VERSION()")
        ver = self.cur.fetchone()
        return "Database version : %s " % ver

    @staticmethod
    def _get_head(phone, head=7):
        return phone[:head]


if __name__ == '__main__':
    my = MysqlQuery()
    print my._test()
    print my.query_phone('15311447009')
    print my.query_phone('1299999')
    print my.query_phone('234111113')
    print my.query_phone('153')
    print my.query_idcard('sfz110100')
    print my.query_idcard('sfz999999')
    print my.query_idcard('110100199212292314')
    print my.query_word('110100199212292314')
    print my.query_word('english')
    print my.query_word('你好')
    del my

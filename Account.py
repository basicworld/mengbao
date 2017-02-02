# -*- coding: utf-8 -*-
# filename: main.py
"""
一些账户类
"""
import sys
reload(sys)
sys.setdefaultencoding('utf8')  # 编译环境utf8


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
归属地区号: %s
"""
import MySQLdb as mdb
import sys


class MysqlQuery(object):
    def __init__(self, host='localhost', user='wechat', passwd='', dbname='mengbao'):
        try:
            self.con = mdb.connect(host, user, passwd, dbname)
            self.cur = self.con.cursor()
        except mdb.Error, e:
            print "Error %d: %s" % (e.args[0], e.args[1])
            sys.exit(1)

    def __del__(self):
        self._close()

    def __exit__(self):
        self._close()

    def _close(self):
        if self.con:
            self.con.close()

    def query_phone(self, phone):
        phone = self._get_phone_head(phone)
        sql = sql_query_phone_model % {'phone': phone}
        self.cur.execute(sql)
        que = self.cur.fetchone()
        return str_query_phone_model % que

    def query_english(self):
        pass

    def _test(self):
        self.cur.execute("SELECT VERSION()")
        ver = self.cur.fetchone()
        return "Database version : %s " % ver

    @staticmethod
    def _get_phone_head(phone):
        return phone[:7]


if __name__ == '__main__':
    my = MysqlQuery()
    print my._test()
    print my.query_phone('15311447009')
    print my.query_phone('13513208899')
    del my

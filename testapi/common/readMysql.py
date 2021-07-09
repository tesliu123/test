import pprint

import pymysql
from readConfig import *


'''读取mysql数据库'''

c = ReadConfig('../fileConfig/config.ini')
host = c.get_datebase('host')
username = c.get_datebase('username')
password = c.get_datebase('password')
port = int(c.get_datebase('port'))
database = c.get_datebase('database')


class ReadMysql:
    def __init__(self):
        self.con = pymysql.connect(host=host, port=port, user=username, password=password, db=database, charset='utf8')
        self.cur = self.con.cursor()

    def select_all(self):
        sql = 'select * from t_app_config'
        r = self.cur.execute(sql)
        result = self.cur.fetchall()
        lresult = list(result)
        self.con.close()
        return lresult

    def select_one(self):
        sql = 'select * from t_app_config'
        r = self.cur.execute(sql)
        a = []
        for i in range(r):
            result = list(self.cur.fetchone())
            a.append(result)
        return a


if __name__ == '__main__':
    m = ReadMysql()
    # pprint.pprint(m.select_all())
    pprint.pprint(m.select_one())

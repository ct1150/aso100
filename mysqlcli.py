import pymysql
from setting import *
from pprint import pprint


class MysqlCli(object):
    def __init__(self):
        self.db = pymysql.connect(host=MYSQL_IP, port=MYSQL_PORT, user=MYSQL_USER, password=MYSQL_PWD,
                                  database=MYSQL_DB)
        self.cursor = self.db.cursor()

    # 执行单个命令
    def execute(self, sql):
        try:
            self.cursor.execute(sql)
            self.db.commit()
            res = self.cursor.fetchall()
            if res:
                return res
            else:
                return "exec done"
        except Exception as e:
            return "execute error", e.detail

    # 批量执行命令
    def execute_many(self, sql, values):
        try:
            res = self.cursor.executemany(sql, values)
            self.db.commit()
            res = self.cursor.fetchall()
            if res:
                return res
            else:
                return "exec done"
        except Exception as e:
            return "execute error", e

    def __del__(self):
        self.cursor.close()
        self.db.close()


if __name__ == '__main__':
    mysql = MysqlCli()
    pprint(mysql.execute('select * from tread_rank limit 1'))

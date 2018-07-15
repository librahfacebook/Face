'''
将用户信息进行保存并上传到个人数据库内
'''
import pymysql


class DBHelper:
    def __init__(self, host='127.0.0.1', user='root',
                 pwd='158968', db='face'):
        self.host = host
        self.user = user
        self.pwd = pwd
        self.db = db
        self.conn = None

    # 连接数据库
    def connect(self):
        try:
            self.conn = pymysql.connect(self.host, self.user,
                                        self.pwd, self.db, charset='utf8')
        except:
            print("connect error...")
            return False
        self.cur = self.conn.cursor()
        return True

    # 关闭数据库
    def close(self):
        if self.conn and self.cur:
            self.cur.close()
            self.conn.close()
        return True

    # 插入操作,执行数据库语句
    def execute(self, sql, params=None):
        # 连接数据库
        self.connect()
        try:
            if self.conn and self.cur:
                self.cur.execute(sql, params)
                self.conn.commit()
        except:
            print("insert error...")
            self.close()
            return False
        return True

    # 查询表数据
    def fetchall(self, sql, params=None):
        self.execute(sql, params)
        return self.cur.fetchall()

import pymysql

db_host = "sql.tomxin.cn"
db_user = "fjut_workhub"
db_passwd = "fjut666"
db_name = "fjut_workhub"
db_charset = "utf8"

class Mysql(object):
    def __init__(self):
        try:
            self.conn = pymysql.connect(
                host=db_host,
                port=3306,
                user=db_user,
                passwd=db_passwd,
                db=db_name,
                charset=db_charset
            )
        except Exception as e:
            print(e)
        else:
            print('连接成功')
            self.cur = self.conn.cursor()

    # def create_table(self):
    #     sql = 'create table testtb(id int, name varchar(10),age int)'
    #     res = self.cur.execute(sql)
    #     print(res)

    def close(self):
        self.cur.close()
        self.conn.close()

    def insert(self,sql):  # 增
        # sql = 'insert into testtb values(1,"Tom",18),(2,"Jerry",16),(3,"Hank",24)'
        res = self.cur.execute(sql)
        if res:
            self.conn.commit()
        else:
            self.conn.rollback()
        return res

    def delete(self, sql):  # 删
        # sql = 'delete from testtb where id=1'
        res = self.cur.execute(sql)
        if res:
            self.conn.commit()
        else:
            self.conn.rollback()
        return res

    def update(self, sql):  # 改
        # sql = 'update testtb set name="Tom Ding" where id=2'
        res = self.cur.execute(sql)
        if res:
            self.conn.commit()
        else:
            self.conn.rollback()
        return res

    def select(self, sql):  # 查
        # sql = 'select * from testtb'
        self.cur.execute(sql)
        res = self.cur.fetchall()
        return res

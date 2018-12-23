import pymysql
import tomxin.tx_time

db_host = "sql..cn"
db_user = ""
db_passwd = "@"
db_name = ""
db_charset = "utf8"

'''
   for row in results:
      fname = row[0]
      lname = row[1]
      age = row[2]
      sex = row[3]
      income = row[4]
'''
def select(selectSql):
    try:
        db = pymysql.connect(user=db_user, passwd=db_passwd, host=db_host, db=db_name, charset=db_charset)
        cursor = db.cursor()
        cursor.execute(selectSql)
        row = cursor.fetchall()
    except Exception as e:
        print(tomxin.tx_time.now_time() + "【查询数据出错】exception SQL：" + selectSql)
        raise e
    else:
        return row
    finally:
        # 关闭数据库连接
        db.close()



'''
插入不重复的数据
selectSql：查询不重复的sql
insertSql：要插入的sql
'''
def insertUnique(selectSql, insertSql):
    # 查询数据库中是否已经有了
    db = pymysql.connect(user = db_user, passwd = db_passwd, host = db_host, db = db_name, charset = db_charset)
    cursor = db.cursor()
    cursor.execute(selectSql)
    row = cursor.fetchone()
    if len(row) == 0:  # 如果数据库中没有相同记录，执行插入
        # 执行sql语句
        cursor.execute(insertSql)
        # 提交到数据库执行
        db.commit()
    # 关闭数据库连接
    db.close()

'''
写操作
'''
def operate(insertSql):
    try:
        db = pymysql.connect(user=db_user, passwd=db_passwd, host=db_host, db=db_name, charset=db_charset)
        cursor = db.cursor()
        # 执行sql语句
        cursor.execute(insertSql)
        # 提交到数据库执行
        db.commit()
    except Exception as e:
        print(tomxin.tx_time.now_time() + "【操作数据出错】exception SQL：" + insertSql)
        raise e
    finally:
        # 关闭数据库连接
        db.close()


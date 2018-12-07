import pymysql

db_host = ""
db_user = ""
db_passwd = "@"
db_name = ""
db_charset = "utf8"

def select(selectSql):
    # 查询数据库中是否已经有了
    db = pymysql.connect(user = db_user, passwd = db_passwd, host = db_host, db = db_name, charset = db_charset)
    cursor = db.cursor()
    cursor.execute(selectSql)
    row = cursor.fetchall()
    # 关闭数据库连接
    db.close()
    return row

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
    if row == None:  # 如果数据库中没有相同记录，执行插入
        # 执行sql语句
        cursor.execute(insertSql)
        # 提交到数据库执行
        db.commit()
    # 关闭数据库连接
    db.close()

def operate(insertSql):
    db = pymysql.connect(user = db_user, passwd = db_passwd, host = db_host, db = db_name, charset = db_charset)
    cursor = db.cursor()
    # 执行sql语句
    cursor.execute(insertSql)
    # 提交到数据库执行
    db.commit()
    # 关闭数据库连接
    db.close()


import pymysql
db = pymysql.connect(host='localhost',
                     database='empdb',
                     user='root',
                     password='123456',
                     charset="utf8")
cursor = db.cursor()

# SQL语句
sql = 'select * from user'
cursor.execute(sql)

# 获取所有结果集
print(cursor.fetchall())

import pymysql
db=pymysql.connect(host='localhost',user='root',password='a18839112505',port=3306,db='weather')
cursor=db.cursor()
sql='CREATE TABLE IF NOT EXISTS student (id CHAR(24),name CHAR(24),age INT,PRIMARY KEY(id))'
cursor.execute(sql)
db.close()

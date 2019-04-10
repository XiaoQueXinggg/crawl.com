import pymysql
db=pymysql.connect(host='localhost',user='root',password='a18839112505',port=3306)
cursor=db.cursor()
cursor.execute('SELECT VERSION()')
data=cursor.fetchone()
print('Database version',data)
cursor.execute("CREATE DATABASE weather DEFAULT CHARACTER SET utf8")
db.close()



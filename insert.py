import pymysql
id='1291517960'
name='aokai'
age=30
db=pymysql.connect(host='localhost',user='root',password='a18839112505',port=3306,db='weather')
cursor=db.cursor()
sql='INSERT INTO student(id,name,age) values(%s,%s,%s)'
try:
    cursor.execute(sql,(id,name,age))
    db.commit()
except:
    db.rollback()
db.close()

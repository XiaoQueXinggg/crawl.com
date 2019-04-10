import pymysql as py
db=py.connect(host='localhost',
              user='root',
              password='a18839112505',
              port=3306,
              db='weather')
cursor=db.cursor()
#cursor.execute('DROP TABLE IF EXISTS douban_analysis')
#sql='CREATE TABLE douban_analysis(id INT AUTO_INCREMENT,name CHAR(255),url CHAR(255),score INT,derector CHAR(255),composer CHAR(255),actor CHAR(255),category CHAR(255),district CHAR(255),language CHAR(255),showtime CHAR(255),length CHAR(255),othername CHAR(255),description CHAR(255),PRIMARY KEY (id))engine=InnoDB DEFAULT CHARSET UTF8MB4'
#cursor.execute(sql)
f=open('C:/Users/576670267/Desktop/new_douban.txt','r',encoding='utf-8')
n=0
while True:
    fr=f.readline()
    if len(fr):
        info=fr.split('^',13)
        name=info[1]
        url=info[2]
        score=info[4]
        derector=info[5].split('/')[0]
        composer=info[6].split('/')[0]
        actor=info[7].split('/')[0]
        category=info[8]
        district=info[9]
        language=info[10]
        showtime=info[11]
        length=info[12]
        othername=info[13]
        sql1='''INSERT INTO douban_analysis (name,url,score,derector,composer,actor,category,district,language,showtime,length,othername) VALUES('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')'''%(name,url,score,derector,composer,actor,category,district,language,showtime,length,othername)
        cursor.execute(sql1)
        db.commit()
        n=n+1
        if n==100:
            print('已输入%s个'%n)
    else:
        break
f.close()
db.close()



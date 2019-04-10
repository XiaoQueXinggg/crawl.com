import requests
from bs4 import BeautifulSoup
import time
f=open('douban.txt','r',encoding='utf-8')
header={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:62.0) Gecko/20100101 Firefox/62.0'}
with open('new_douban.txt','w',encoding='utf-8') as fw:
    count=0
    errorcount=0
    for line in f.readlines():
        if len(line)<5:
            continue
        else:
            line=line.split(';')
            movieid=line[0]
            title=line[1]
            url=line[2]
            cover=line[3]
            rate=line[4].rstrip('\n')
            
            response=requests.get(url).text
            soup=BeautifulSoup(response,'lxml')
            info=soup.select('#info')[0]
            info=info.get_text().split('\n')
            director=info[1].split(':')[-1].strip()
            composer=info[2].split(':')[-1].strip()
            actor=info[3].split(':')[-1].strip()
            category=info[4].split(':')[-1].strip()
            district=info[5].split(':')[-1].strip()
            language=info[6].split(':')[-1].strip()
            showtime=info[7].split(':')[-1].strip()
            length=info[8].split(':')[-1].strip()
            othername=info[9].split(':')[-1].strip()
            try:
                
                description=soup.find_all("span",attrs={"property":"v:summary"})[0].get_text() 
                description=description.lstrip().lstrip('\n\t').rstrip().rstrip('\n\t')
            except:
                description='无'
            fw.write('{}^{}^{}^{}^{}^{}^{}^{}^{}^{}^{}^{}^{}^{}\n'.format(movieid,title,url,cover,rate,director,composer,actor,category,district,language,showtime,length,othername,description+'\n'))
            count+=1
            time.sleep(2.5)
            if(count%100==0):
                print('已经完成{}个'.format(count))
print('总共完成{}个'%count)
                

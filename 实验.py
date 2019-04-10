import time
import requests
headers={'Host':'movie.douban.com',
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:62.0) Gecko/20100101 Firefox/62.0',
'Accept':'*/*',
'Accept-Language':'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
'Accept-Encoding':'gzip, deflate, br',
'Referer':'https://movie.douban.com/explore',
'X-Requested-With':'XMLHttpRequest',
'Cookie':'__utma=30149280.1282991193.1491880768.1537841312.1537843896.11; __utmz=30149280.1537841312.10.8.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1537843895%2C%22https%3A%2F%2Fwww.douban.com%2F%22%5D; _pk_id.100001.4cf6=79bbbaee17b94ea9.1500621595.8.1537843895.1537841693.; __utma=223695111.2071332893.1500621597.1537841311.1537843896.5; _vwo_uuid_v2=DCFCFE0D0ADB4263B3D11766C2061014|3ea5a6b3dc4550fbcf67ecf3e5297f2e; viewed="2125040_1083989_25756947_4605583_1292416"; gr_user_id=53a6faf2-ad8e-4e0c-bc48-41e96697c235; ll="118241"; bid=bj0z7di26_8; __utmv=30149280.14880; douban-profile-remind=1; __utmz=223695111.1537841311.4.2.utmcsr=douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/; __yadk_uid=LbVZBzPEoyRx59FBxrKF6Lf2Bqc0Prnq; ap_v=0,6.0; __utmc=30149280; __utmc=223695111; _pk_ses.100001.4cf6=*; __utmb=30149280.0.10.1537843896; __utmb=223695111.0.10.1537843896',    
'Connection':'keep-alive'}
url='https://movie.douban.com/j/search_tags?type=movie&source='
tags=requests.get(url,headers=headers).json()['tags']
print(tags)
with open('douban.txt','w',encoding='utf-8') as f:  
    for i in tags:
        start_page=0
        f.write(str(i)+'\n')
        print('开始输入'+i+'类电影')
        while True:
            url_='https://movie.douban.com/j/search_subjects?type=movie&tag='+str(i)+'&page_limit=20&page_start='+str(start_page)
            movies=requests.get(url_).json()['subjects']
            if len(movies)==0:
                break
            for subject in movies:
                rate=subject['rate']
                title=subject['title']
                url=subject['url']
                cover=subject['cover']
                movieId=subject['id']
                f.write(movieId+';'+str(title)+';'+str(url)+';'+str(cover)+';'+rate+'\n')
                
            start_page+=20

            
            

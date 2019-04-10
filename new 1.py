import requests
from bs4 import BeautifulSoup


def get_html(page):
    try:
        url="https://alpha.wallhaven.cc/search"
        data={'q':'',
              'categories':'001',
              'purity':'100',
              'topRange':'1M',
              'sorting':'toplist',
              'order':'desc',
              'page':page,


            }
        r=requests.get(url,params=data)
        r.raise_for_status()
        r.encoding='utf-8'
        return r.text
            
    except:
        print('something wrong')
                   
def get_urls():
    html=get_html(page)
    urls=[]
    soup=BeautifulSoup(html,'lxml')    
    div=soup.find_all('a',attrs={'class':'preview'})
    for a in div :
        
    return urls
def OutImg():
    urls=get_urls()
    base_file="C:/Users/576670267/Desktop/img/"
    for url in urls:
        count=1
        with open(base_file+str(count)+'.jpg','wb+') as f:
            response=requests.get(url)
            content=response.content
            f.write(content)
            count=count+1
 
if __name__=='__main__':
    OutImg()
    

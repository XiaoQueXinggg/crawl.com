import http.cookiejar
from urllib import request
from bs4 import BeautifulSoup
headers={'Referer':'Referer: https://accounts.douban.com/login?redir=https://www.douban.com/&source=index_nav',
         'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:63.0) Gecko/20100101 Firefox/63.0'}
name='cookie.text'
cookie=http.cookiejar.MozillaCookieJar(name)
try:
    cookie.load(ignore_discard=True,ignore_expires=True)
except:
    print('cannot load cookie')
opener=request.build_opener(request.HTTPCookieProcessor(cookie))
opener.addheaders=[(key,value)for key,value in headers.items()]
url='https://www.douban.com/people/148806586/'
response=opener.open(url)
print(type(response))
status=response.code
req=response.read()
response=req.decode('utf-8')
soup=BeautifulSoup(response,'lxml')
a=soup.find_all('p',attrs={"class":'text'})[0]
text=a.find('a',attrs={'target':'_blank'}).text.split(' ')[0]
print(status)
print(text)

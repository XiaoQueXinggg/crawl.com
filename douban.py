import urllib
import re
import http.cookiejar
url='https://accounts.douban.com/login'
name='cookie.text'
cookie=http.cookiejar.MozillaCookieJar(name)
#MozillaCookieJar
handler=urllib.request.HTTPCookieProcessor(cookie)
opener=urllib.request.build_opener(handler)
def get_id():
    url='https://accounts.douban.com/login'
    request=urllib.request(url)
    request.add_header('Referer','Referer: https://accounts.douban.com/login?redir=https://www.douban.com/&source=index_nav')
    request.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:63.0) Gecko/20100101 Firefox/63.0')
    res=urllib.urlopen(request).read()
def login(usename,password):
    postdata={'form_email':str(usename),
'form_password':str(password),
'login':'登录',
'redir':'https://www.douban.com/',
'source':'index_nav'}
    #headers={'Referer':'Referer: https://accounts.douban.com/login?redir=https://www.douban.com/&source=index_nav',
       #'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:63.0) Gecko/20100101 Firefox/63.0'}
    data=bytes(urllib.parse.urlencode(postdata),encoding='utf-8')
    request=urllib.request.Request(url,data=data,method='POST')
    request.add_header('Referer','https://accounts.douban.com/login?redir=https://www.douban.com/&source=index_nav')
    request.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:63.0) Gecko/20100101 Firefox/63.0')
    #print(request.headers)
    response=opener.open(request).read()
    print(type(response))
    res=response.decode('utf-8')
    img_url=re.findall(r'<img id="captcha_image" src="(.*?)" alt="captcha" class="captcha_image"/>',res)[0]
    captcha=re.findall('<input type="hidden" name="captcha-id" value="(.*?)"/>',res)[0]
    return img_url,captcha
def captcha_login(usename,password,img,captcha):
    url='https://accounts.douban.com/login'
    dat={'form_email':str(usename),                    
          'form_password':str(password),
          'login':'登录',
          'captcha-solution':45436,
          'captcha-id':captcha,
          'captcha-solution':img,
          'redir':'https://www.douban.com/',
          'source':'index_nav'}
    dat=bytes(urllib.parse.urlencode(dat),encoding='utf-8')
    request=urllib.request.Request(url,data=dat,method='POST')
    request.add_header('Referer','https://accounts.douban.com/login?redir=https://www.douban.com/&source=index_nav')
    request.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:63.0) Gecko/20100101 Firefox/63.0')
    response=opener.open(request).read()
    res=response.decode('utf-8')
    print(res[:3000])
    cookie.save(ignore_discard=True,ignore_expires=True)
if __name__=='__main__':
    usename=input('请输入账号：')
    password=input('请输入密码：')
    img_url,captcha=login(usename,password)
    urllib.request.urlretrieve(img_url,'1111.jpg')
    img=input('请输入验证码')
    captcha_login(usename,password,img,captcha)



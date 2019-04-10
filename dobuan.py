import requests
session=requests.session()
def login_douban():
    
    headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:61.0) Gecko/20100101 Firefox/61.0'
             }
    data={'form_email':'18839112505',
'form_password':'a18839112505',
'source':'index_nav'}
    response=session.post('https://www.douban.com/',headers=headers,params=data)
    print(response.url)
login_douban()

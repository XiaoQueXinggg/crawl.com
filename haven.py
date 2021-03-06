from bs4 import BeautifulSoup
import aiohttp
import asyncio
import requests
import re
import aiohttp
headers={'Host': 'alpha.wallhaven.cc',
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:63.0) Gecko/20100101 Firefox/63.0',
'Accept': 'text/html, */*; q=0.01',
'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
'X-Requested-With': 'XMLHttpRequest',
'Connection': 'keep-alive',
'Cookie': '__cfduid=da85f62f8ad370790acbb1b7cf4c4a5521519099443; _ga=GA1.2.1086478473.1523436614; _pk_id.1.1f04=c1c4d71145eec100.1538353862.7.1540603088.1540603087.; _pk_ref.1.1f04=%5B%22%22%2C%22%22%2C1540603087%2C%22https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3Dc0teaOQgvwcp77rd5mv-EyVE0FijzvXm3bzXENNMnZdLzOT_YXnI0G1rEiHdSXQ3%26wd%3D%26eqid%3Da3fca97d00049299000000035bbaafc2%22%5D; wallhaven_session=eyJpdiI6IkVJcis1UzFjMHJ3dVwvWFZBSnVcL1BXMTM5a0s0cXZ4TjRBS0tlZWluZzdtcz0iLCJ2YWx1ZSI6IktXcUdmRTNBNjdocFM5ek1mWkd4eGFJM0VhWWU1aG1KQXBINGRPMmpyZmJPY0wxU1wvdDBWOWowcjZBSXg2c1M3eFlNOUxoOXdvZHhqTG5VYm11VTd4QT09IiwibWFjIjoiZTg1ZDRjY2E4NmU4NjZlMzgyMjIyMTM3MTlkZjBhYWRlMWVhN2IwOTI0YTAxNzdhYTNjNjM1Zjk4YTMyNmNmMiJ9; _pk_ses.1.1f04=*'}

def get_urls(url):
    response=requests.get(url).text
    soup=BeautifulSoup(response,'lxml')
    mat=re.compile(r'a class="preview" href="(.*?\d+)" target="_blank"')
    img_url=re.findall(mat,str(soup))
    return img_url
async def img(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.text()
async def get_content(url,name):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as res:
            print('在读二进制')
            content= await res.read()
            print('已读二进制')
            with open('/Users/576670267/Desktop/haven/'+str(name)+'.jpg','wb') as f:
                f.write(content)
async def img_url(url):
    response=await img(url)
    print('图片地址')
    soup=BeautifulSoup(response,'lxml')
    comp=re.compile(r'id="wallpaper" src="//wallpapers.wallhaven.cc/wallpapers/full/wallhaven-(\d+).jpg"') 
    name=re.findall(comp,str(soup))[0]
    img_loc='http://wallpapers.wallhaven.cc/wallpapers/full/wallhaven-'+name+'.jpg'
    await get_content(img_loc,name)
    print('完成')
if __name__=='__main__':
    for i in range(3,6):
        url='https://alpha.wallhaven.cc/search?q=&categories=001&purity=100&sorting=toplist&order=asc&page='+str(i)
        urls=get_urls(url)[0:5]
        print('得到url')
        loop=asyncio.get_event_loop()
        tasks=[img_url(url) for url in urls]
        print('加入任务')
        loop.run_until_complete(asyncio .wait(tasks))
        loop.close() 

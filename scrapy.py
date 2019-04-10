import requests
from bs4 import BeautifulSoup
import time
import sys

def get_html(url):
    try:
       non_bmp_map=dict.fromkeys(range(0x10000,sys.maxunicode+1),0xfffd)
       r=requests.get(url,timeout=30)
       r.raise_for_status()
       print(r.apparent_encoding)
       
       return r.text.translate(non_bmp_map)
    except:
        return "ERROR"    
def get_content(url):
    comments=[]
    html=get_html(url)
    soup=BeautifulSoup(html,'lxml')
    liTags=soup.find_all('li',attrs={'class':' j_thread_list clearfix'})
    print(liTags)
    for li in liTags:
        comment={}
        try:
            comment['title']=li.find('a',attrs={'class':'j_th_tit'}).text.strip()
            comment['link']=li.find('a',attrs={'class':'j_th_tit'})['href']
            comment['name']=li.find('span',attrs={'class':'tb_icon_author'}).text.strip()
            comment['time']=li.find('span',attrs={'class':'pull-right is_show_create_time'}).text.strip()
            comment['relyNum']=li.find('span',attrs={'class':'threadlist_rep_num center_text'}).text.strip()
            comments.append(comment)
        except:
            print('错啦')
    print(comments)
    return comments
def OutFile(dict):
    print('跑这了')
    with open('KouTu.txt','a+') as f:
        for comment in dict:
            f.write('标题：{}\t链接：{}\t发帖人：{}\t发帖时间：{}\t回复数量：{}\t'.format
                    (comment['title'],comment['link'],comment['name'],comment['time'],comment
                     ['relyNum']))

        print('完了')
        
def main(base_url,deep):
    print('开始了')
    url_list=[]
    for i in range(0,deep):
        url_list.append(base_url+'&pn='+str(50*i))
    print('网页添加完了')
    for url in url_list:
        content=get_content(url)
        OutFile(content)
    print('保存完了')
base_url='https://tieba.baidu.com/f?kw=抠图&ie=utf-8'
deep=4  
if __name__=='__main__':
    main(base_url,deep)

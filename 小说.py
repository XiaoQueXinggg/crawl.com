import requests
from bs4 import BeautifulSoup
def get_html(url):
    try:       
        r=requests.get(url,timeout=30)
        r.raise_for_status
        r.encoding=('utf-8')
        return r.text
    except:
        return"错误"        
    return r.text
def get_content(url):
    url_list=[]
    html=get_html(url)
    soup=BeautifulSoup(html,'lxml')
    
    catagory_list=soup.find_all('div',attrs={'class':'index_toplist mright mbottom'})
    history_finished_list=soup.find_all('div',attrs={'class':' index_toplist mright mbottom'})
    for cate in catagory_list:
        name=cate.find('div',attrs={'class':'toptab'}).span.string
        with open('novel_list.csv','a+') as f:
            f.write('小说种类：{}\n'.format(name))
        general_list=cate.find(style='display: block;')
        book_list=general_list.find_all('li')
        for book in book_list:
            link='https://www.qu.la'+book.a['href']
            title=book.a['title']
            url_list.append(link)
            with open('novel_list.csv','a') as f:
                f.write('小说名：{:<}\t 地址：{:<}\n'.format(title,link))
    for cate in history_finished_list:
        name=cate.find('div',attrs={'class':'toptab'}).span.string
        with open('novel_list.csv','a') as f:
            f.write('小说种类：{}\n'.format(name))
        general_list=cata.find(style='display: block;')
        book_list=general_list.find_all('li')
        for book in book_list:
            link='https://www.qu.la'+book.a['href']
            title=book.a['title']
            url_list.append(link)
            with open('novel_list.csv','a') as f:
                f.write('小说名：{:<}\t 地址：{:<}\n'.format(title,link))
    return url_list
def get_txt_url(url):
    url_list=[]
    html=get_html(url)
    soup=BeautifulSoup(html,'lxml')
    txt_name=soup.find('h1').text
    lista=soup.find_all('dd')
    with open('/Users/576670267/Desktop/novel/{}.txt'.format(txt_name),'a+') as f:
        f.write('小说标题：{}'.format(txt_name))
    for url in lista:
        url_list.append('https://www.qu.la/'+url.a['href'])
    return url_list,txt_name
def get_one_txt(url_list,txt_name):
    for url in url_list:
        html=get_html(url).replace('<br>','\n')
        soup=BeautifulSoup(html,'lxml')
        try:
            title=soup.find('title').text
            
            txt=soup.find('div',id='content').text.replace('chaptererror();','')
            with open('/Users/576670267/Desktop/novel/{}.txt','a') as f:
                f.write(title+'\n\n')
                f.write(txt)
                print('当前小说：{}  当前章节：{}打印完毕'.format(txt_name,title))
        except:
            print('出了点小毛病' )
def get_all_txt(url_list):
    for url in url_list:
        page_list,txt_name=get_txt_url(url)
        for page_url in page_lsit:
            get_one_txt(page_url,txt_name)
            print('当前进度{}%'.format(url_list.index(url)/len(url_list)*100))
def main():
    url="https://www.qu.la/paihangbang/"    
    url_list=get_content(url)
    url_list=list(set(url_list))
    get_all_txt(url_list)
if __name__=='__main__':
    main()
            



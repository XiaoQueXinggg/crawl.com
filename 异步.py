import requests
import pymysql
def get_json():
    headers={'Accept':'application/json, text/javascript, */*; q=0.01',
    'Accept-Encoding':'gzip, deflate, br',
    'Accept-Language':'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
    'Connection':'keep-alive',
    'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
    'Cookie':'Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1536048630,1536308091,1537098307,1537102262; _ga=GA1.2.2050138044.1532701037; user_trace_token=20180727221716-c3e5be09-91a7-11e8-a6ea-525400f775ce; LGUID=20180727221716-c3e5c10a-91a7-11e8-a6ea-525400f775ce; index_location_city=%E5%85%A8%E5%9B%BD; JSESSIONID=ABAAABAAAFCAAEGEAE8CC63266F605089692C573E2AE7DA; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1537102262; _gid=GA1.2.464123406.1537098308; LGRID=20180916205100-29c8c008-b9af-11e8-a052-525400f775ce; TG-TRACK-CODE=search_code; SEARCH_ID=0f85a6d16012493cbdac1d6344f37f75; LGSID=20180916205100-29c8bea2-b9af-11e8-a052-525400f775ce; PRE_UTM=; PRE_HOST=www.baidu.com; PRE_SITE=https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3DsXx-1gnhEXwu7_Q9oMO-feoyoezmUiEFCP9apmSalom%26wd%3D%26eqid%3Dc1dbb9820006c8c1000000035b9e4239; PRE_LAND=https%3A%2F%2Fwww.lagou.com%2F',
    'Host':'www.lagou.com',
    'XMLHttpRequest':'XMLHttpRequest',
    'X-Anit-Forge-Token':'None',   
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:62.0) Gecko/20100101 Firefox/62.0',
    'Referer':'https://www.lagou.com/jobs/list_Python?px=default&city=%E9%83%91%E5%B7%9E'
            }
    data={'first':'true',
    'kd':'Python',
    'pn':1}
    req=requests.post('https://www.lagou.com/jobs/positionAjax.json?px=new&city=郑州&needAddtionalResult=false',params=data,headers=headers).json()
    response=req['content']['positionResult']['result']
    info_list=[]
    for i in response:
        info=[]
        info.append((i.get(i['positionName'],'无')))
        info.append((i.get(i['workYear'],'无')))
        info.append((i.get(i['education'],'无')))
        info.append((i.get(i['salary'],'无')))
        info.append((i.get(i['positionAdvantage'],'无')))
        info.append((i.get(i['companyShortName'],'无')))
        info.append((i.get(i['district'],'无')))
        info_list.append(info)
    return info_list  
def get_conn(info_list):
    conn=pymysql.connect(host='localhost',
                                user='root',
                                password='a18839112505',
                                db='weather',
                                charset='utf8mb4',
cursorclass=pymysql.cursors.DictCursor)
    with conn.cursor() as cursor:
        sql="INSERT INTO 'job'('职位','工作经历','教育','薪水','公司优势','公司名字','公司地点')VALUES(%s,%s,%s,%s,%s,%s,%s)"
        for i in info_list:
            cursor.execute(sql,i)
        
        conn.commit()
def main():
    info_list=get_json()
    get_conn(info_list)
    print('写入完毕')
if __name__=='__main__':
    main()

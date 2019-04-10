import requests
alive_ip=[]
dir_path='C:/Users/576670267/Desktop/'
def test_alive(proxys):
    global alive_ip
    for proxy in proxys:
        proxies={'http':proxy} 
        print('正在测试：{}'.format(proxies))
        try:
            r=requests.get("https://www.qiushibaike.com/8hr/page/1/",proxy=proxies,timeout=3)
            if r.status_code==200:
                print('{}：可以用'.format(proxies))
                alive_ip.append(proxies)
        except:
            print('这个不能用'.format(proxies))
def Out_file(alive_ip=[]):
    global dir_path
    with open(dir_path+'alive_ip.txt','a+') as f:
        for ip in alive_ip:
            f.write(str(ip)+'\n')
        print('写完了')
def test(filename='blank.txt'):
    with open(dir_path+filename,'r') as f:
        lines=f.readlines()
        proxys=list(map(lambda x:x.strip(),[y for y in lines]))
        test_alive(proxys)
    Out_file(alive_ip)
test('kdlspider.txt')
    

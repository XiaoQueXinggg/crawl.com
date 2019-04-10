from selenium import webdriver
from PIL import Image
from selenium.webdriver.common.action_chains import ActionChains
import requests
import time,re
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import numpy as np
import math
def is_similar_color(cpx,fpx):
    for i,pixel in enumerate(cpx):
        if abs(fpx[i]-pixel)>50:
            return False
    return True
def get_offset_distance(img1,img2):
    for x in range(img1.width):
        for y in range(img1.height):
            cpx=img1.getpixel((x,y))
            fpx=img2.getpixel((x,y))
            if not is_similar_color(cpx,fpx):
                return x
#获得url和验证码集合

def get_image(label,name):
    link=re.compile('background-image: url\("(.*?)"\); background-position: (.*?)px (.*?)px;')
    position=[]
    elements=driver.find_elements_by_xpath(label)
    img_url=str
    for element in elements:
        style=element.get_attribute('style')
        group=link.search(style)
        img_url=group.group(1)
        x_position=group.group(2)
        y_position=group.group(3)
        position.append((abs(int(x_position)),abs(int(y_position))))
    response=requests.get(img_url).content
    file='C:/Users/576670267/Desktop/'+name+'.jpg'
    with open(file,'wb') as f:
        f.write(response)
    image=Image.open(file)
    upper_img=[]
    down_img=[]
    for per in position:
        if per[1]==0:
            down_img.append(image.crop((per[0],0,per[0]+10,58)))
        else:
            upper_img.append(image.crop((per[0],58,per[0]+10,image.height)))
    newImage=Image.new('RGB',(260,116))
    x_offset=0
    y_offset=0
    for upper in upper_img:
        newImage.paste(upper,(x_offset,0))
        x_offset+=10
    for down in down_img:
        newImage.paste(down,(y_offset,58))
        y_offset+=10    
    return newImage
def slide_capth(tracks):
    button=driver.find_element_by_css_selector('.gt_slider_knob.gt_show')
    ActionChains(driver).click_and_hold(button).perform()
    print(tracks)
    for x in tracks:
        ActionChains(driver).move_by_offset(x,0).perform()
    ActionChains(driver).release().perform()
def ease_func(x):
    return 1-(1-x)*(1-x)
def get_tracks(x,seconds,ease_func):
    tracks=[0]
    offsets=[0]
    ease=globals()[ease_func]
    for t in np.arange(0.0,seconds,0.1):
        offset=round(ease(t/seconds)*x)
        tracks.append(offset-offsets[-1])
        offsets.append(offset)
    return offsets,tracks
if __name__=='__main__':    
    driver=webdriver.Firefox()
    time.sleep(3)
    driver.get('https://passport.bilibili.com/login')
    driver.implicitly_wait(10)                               
    use_name=driver.find_element_by_id('login-username')
    use_name.send_keys('18839112505')
    pass_port=driver.find_element_by_id('login-passwd')
    pass_port.send_keys('a18839112505')
    button=driver.find_element_by_css_selector('.gt_slider_knob.gt_show')
    ActionChains(driver).move_to_element(button).perform()
    img1=get_image('//div[@class="gt_cut_fullbg_slice"]','ture_image')
    print('第二张')
    img2=get_image('//div[@class="gt_cut_bg_slice"]','hide_image')
    x=get_offset_distance(img1,img2)
    #x-=button.size['width']/2
    x-=6
    seconds=2
    offset,tracks=get_tracks(x,seconds,'ease_func')
    slide_capth(tracks)
#img_order=driver.find_element_by_css_selector('gt_fullbg gt_show')

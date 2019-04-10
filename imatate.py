from selenium import webdriver
import time

browser=webdriver.Firefox()
browser.get('https://www.taobao.com')
input_first=browser.find_element_by_id('q')
input_first.send_keys('xiaomi')
button=browser.find_element_by_class_name('submit icon-btn-search')
button.click()

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException

driver=webdriver.Firefox()
driver.get("https://www.suning.com/?utm_source=union&utm_medium=14&adtype=5&utm_campaign=08c3d474-5857-481f-81bc-a3266b82403f&union_place=un")
driver.implicit(10)
login_button=driver.find_element_by_css_selector('.login')
login_button.click()
pass_login=driver.find_element_by_xpath('//a[@class="tab-item"]/span')
pss_login.click()
check_button=driver.find_element_by_css_selector('.sncaptcha-init-button-text')
check_button.click()

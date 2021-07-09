# encoding=utf-8
from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

driver=webdriver.Chrome()
driver.get('https://www.baidu.com/')
driver.maximize_window()
element=driver.find_element_by_id('kw')
element.send_keys('白月黑羽')
driver.close()
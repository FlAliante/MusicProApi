from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import time
driver = webdriver.Chrome(executable_path="C:\chromedriver_win32\chromedriver.exe")
driver.get('https://music-pro-develop.herokuapp.com/guitarras.html')


time.sleep(2)
usuario = driver.find_element(by='class name',value='button2')
usuario.click()
time.sleep(2)
driver.get('https://music-pro-develop.herokuapp.com/checkout.html')
time.sleep(10)
usuario = driver.find_element(by='id',value='btn_usd')
usuario.click()
time.sleep(10)
usuario = driver.find_element(by='id',value='btn_clp')
usuario.click()
time.sleep(10)


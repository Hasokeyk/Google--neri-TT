# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time
import random

linkS = 1
PROXY = 'https://proxy-server.herokuapp.com/'
kelimeler = [
    'akbaşlar tekstil bursa iş başvurusu',
    'akbaşlar tekstil iş başvuru formu',
    'bursa akbaşlar tekstil staj',
    'akbaşlar tekstil doğalgaz santrali',
    'akbaşlar tekstil iş başvuru formu',
    'akbaşlar tekstil gürsu iş başvurusu',
]

options = webdriver.ChromeOptions()
#options.add_argument('--ignore-certificate-errors')
#options.add_argument("--test-type")
options.add_argument("--no-sandbox")
options.add_argument('headless')
options.add_argument('--data-reduction-proxy-http-proxies=%s' % PROXY)

while True:
    driver = webdriver.Chrome(chrome_options=options,executable_path="C:/chromedriver.exe")
    driver.get('https://www.google.com')
    
    kelimeBul = kelimeler[random.randint(0,(len(kelimeler)-1))]
    
    text_area = driver.find_element_by_class_name('gsfi')
    text_area.send_keys(kelimeBul)
    time.sleep(1)

    text_area.send_keys(Keys.ENTER)
    time.sleep(2)
    print(kelimeBul,' aratıldı')

    html = driver.page_source

    ilk_link = driver.find_element(By.XPATH, '//*[@id="rso"]/div[1]/div/div['+str(linkS)+']/div/div/div[1]/a[1]')
    ilk_link.click()
    time.sleep(3)
    print('1. link tıklandı')

    driver.back()
    time.sleep(1)
    print('Geri gelindi')

    ilk_link = driver.find_element(By.XPATH, '//*[@id="rso"]/div/div/div['+str(random.randint(4, 9))+']/div/div/div[1]/a[1]')
    ilk_link.click()
    time.sleep(2)
    print('2. link tıklandı')

    driver.close()
    print('Tarayıcı Kapandı')
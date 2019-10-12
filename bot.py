from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from urllib.request import urlopen
import time
import random
import json
import pickle
import glob
import re
import datetime

an = datetime.datetime.now()
linkS = 1
kelimeler = [
    'akbaş holding bursa',
    'akbaş holding bursa adres',
    'akbaş holding iş başvurusu',
    'akbaşlar holding bursa',
    'akbaşlar holding bursa adres',
    'akbaşlar holding iş başvurusu',
    # 'akbaş holding iletişim',
    # 'akbaş holding adres',
    # 'akbaş holding haberleri',
    'akbaş holding iş ilanları',
    'akbaşlar holding iş ilanları',
    # 'akbaş holding kariyer',
    # 'akbaş holding kimin',
    # 'akbaş holding yönetim kurulu',
    'akbaş holding insan kaynakları',
    'akbaşlar holding insan kaynakları',

    # 'akbaş holding tel',
    # 'akbaş holding fabrika',
    # 'akbaş holding fabrikası',
    # 'akbaş holding facebook',
    # 'akbaş holding firmaları',
    # 'akbaş holding firma adresi',
    # 'akbaş holding firma sahibi',
    # 'akbaş holding fuar',
    # 'akbaş holding firma isimleri',
    # 'akbaş holding fiyatları',

    # 'webtures kariyer',
    # 'Webtures Nedir',
    # 'webtures capital',
    # 'webtures kitap',
    # 'webtures fiyat',
    #
    # 'Kaan gülten sözleri',
    #
    # 'seo hocası seo araçları',
    # 'seo hocası site içi optimizasyon',
    # 'seo hocası iletişim',
    # 'seo hocasi soru cevap',
    # 'seo hocasi seo araçları',
    # 'seo hocasi site içi optimizasyon',
    # 'seo hocasi iletişim',
    # 'seohocası soru cevap',
    # 'seohocası seo araçları',
    # 'seohocası site içi optimizasyon',
    # 'seohocası iletişim',
    # 'seohocasi soru cevap',
    # 'seohocasi seo araçları',
    # 'seohocasi site içi optimizasyon',
    # 'seohocasi iletişim',
]

options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
# options.add_argument("--test-type")
options.add_argument("--no-sandbox")
# options.add_argument("--host-resolver-rules=MAP www.google-analytics.com 127.0.0.1")
options.add_argument("--incognito")
# options.add_argument('headless')
# options.add_argument("--user-data-dir=C:/Users/User/AppData/Local/Google/Chrome/User Data")
# options.add_argument("--User-Agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36")

# keyboard = Controller()

driver = webdriver.Chrome(executable_path='C:\chromedriver.exe')

while True:
    for filename in glob.iglob('cookies/*.txt', recursive=True):
        try:
            # keyboard.press(Key.shift)
            # with keyboard.pressed(Key.shift):
            # keyboard.press(Key.f9)

            # options.add_argument('--proxy-server=%s' % proxyList[proxySkip])

            # driver.set_window_position(2835,71)

            driver.get(
                'https://www.google.com.tr/search?q=Akba%C5%9F%20Holding%20Bursa%20Adres&gl=tr&hl=tr&uule=w+CAIQICIFZ3Vyc3U')
            driver.set_page_load_timeout(10)

            print(str(driver.get_cookies()))
            #
            f = open("cookies/guest-cookies.txt", "w")
            f.write(str(driver.get_cookies()).replace("True", "true").replace("False", "false").replace("'", '"'))

            cookies = json.load(open(filename, "r"))
            for cookie in cookies:
                driver.add_cookie(cookie)

            driver.refresh()

            kelimeBul = kelimeler[random.randint(0, (len(kelimeler) - 1))]
            try:
                text_area = driver.find_element_by_class_name('gLFyf')
                text_area.clear()
                for c in kelimeBul:
                    text_area.send_keys(c)
                    time.sleep(random.uniform(0, 0.2))
                text_area.send_keys(kelimeBul)
                time.sleep(10)

                text_area.send_keys(Keys.ENTER)
                time.sleep(10)

                html = driver.page_source

                ilk_link = driver.find_element_by_css_selector('#rso .srg .g a')
                ilk_link.click()
                time.sleep(30)

                log = open('log.txt', 'a')
                data = str(urlopen('http://checkip.dyndns.com/').read())
                ip = re.compile(r'Address: (\d+\.\d+\.\d+\.\d+)').search(data).group(1)
                logStr = str(datetime.datetime.ctime(
                    an) + ' - "' + kelimeBul + '" kelimesi aratıldı. Cookie Sahibi ' + filename + ' IP:' + ip + "\n")
                log.write(logStr)
                print(logStr)

                driver.close()
            except Exception as hata:
                print(hata)
                driver.close()
                pass
        except Exception as hata:
            print(hata)
            driver.close()
            pass

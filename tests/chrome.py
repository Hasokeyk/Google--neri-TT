import datetime
import glob
import json
import random
import re
import time
from urllib.request import urlopen

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument("--no-sandbox")
options.add_extension('C:/Users/Seldos/Desktop/Google-TT/tests/extensions/vpn.crx');
#options.add_argument("--incognito")
#options.add_argument("--User-Agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36")
# options.add_argument('headless')

browser = webdriver.Chrome(options=options,executable_path='C:\chromedriver.exe')

searchWordList = [
    'Murat Yüksektepe',
    'Murat Yüksektepe Kimdir?',
]
googleSearch = "https://www.google.com/search?q="
now = datetime.datetime.now()
#while True:
for filename in glob.iglob('C:/Users/Seldos/Desktop/Google-TT/cookies/murat.txt', recursive=True):
    try:

        # Kelime listesinden rastgele birini seç
        searchWord = searchWordList[random.randint(0, (len(searchWordList) - 1))]

        # Google arama url'i ile birleştir
        url = googleSearch + searchWord

        # Oluşan url'i tarayıcıda aç
        browser.get(url)

        # Tarayıcı yükleme aşım süresi 10sn
        browser.set_page_load_timeout(1000)

        # Misafir çerezi
        f = open("C:/Users/Seldos/Desktop/Google-TT/cookies/guest-cookies.txt", "w")

        # Tarayıcıya atanan çerezi güncelle
        f.write(str(browser.get_cookies()).replace("True", "true").replace("False", "false").replace("'", '"'))

        # Çerezleri getir
        cookies = json.load(open(filename, "r"))

        # Çerezler
        for cookie in cookies:
            # Tarayıcıya çerez ata
            browser.add_cookie(cookie)

        # Tarayıcıyı yenile
        browser.refresh()

        # Kelime listesinden rastgele birini seç
        searchWord = searchWordList[random.randint(0, (len(searchWordList) - 1))]

        # Dene babacım!
        try:
            text_area = browser.find_element_by_class_name('gLFyf')
            text_area.clear()
            for c in searchWord:
                text_area.send_keys(c)
                time.sleep(random.uniform(0, 0.2))

            text_area.send_keys(Keys.ENTER)
            time.sleep(3)

            html = browser.page_source

            ilk_link = browser.find_element_by_css_selector('#rso .srg .g a')
            ilk_link.click()
            time.sleep(30)

            log = open('log.txt', 'a')
            data = str(urlopen('http://checkip.dyndns.com/').read())
            ip = re.compile(r'Address: (\d+\.\d+\.\d+\.\d+)').search(data).group(1)
            logStr = str(datetime.datetime.ctime(now) + ' - "' + searchWord + '" kelimesi aratıldı. Cookie Sahibi ' + filename + ' IP:' + ip + "\n")
            log.write(logStr)
            print(logStr)

            browser.quit()

        except Exception as e:
            print("Try 2: ")
            print(e)
            browser.quit()
            pass

    except Exception as e:
        print("Try 1: ")
        print(e)
        #browser.quit()
        pass
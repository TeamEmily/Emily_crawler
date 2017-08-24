from selenium import webdriver
from urllib.request import urlopen
from bs4 import BeautifulSoup
import telegram
import os
import lxml
import time

bot = telegram.Bot(token='346845203:AAHZO2zdCwQzro_7DphpCxxIoPKXlLPTcqM')
chat_id = bot.getUpdates()[-1].message.chat.id

options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_argument('window-size=1920x1080')

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

base_url = 'http://gall.dcinside.com/'
url = 'http://gall.dcinside.com/mgallery/board/lists/?id=pebble&page=1&exception_mode=recommend'
driver = webdriver.Chrome('C:\hyunwoo_workspace\python\chromedriver', chrome_options=options)

while True:
    driver.get(url)

    content = driver.page_source
    soup = BeautifulSoup(content, 'lxml')

    all_a = soup.find_all('a')
    is_first = 1
    for s in all_a:
        try:
            prop = s.get('class')
            if prop != None and prop[0] == 'icon_pic_b':
                if is_first == 1:
                    latest = s.get_text()
                    link = s.get('href')
                    print(link)
                    is_first = 0

            # print("%s" % (s.get_text()))

        except UnicodeEncodeError:
            print("Error : %d" % (idx))

    with open(os.path.join(BASE_DIR, 'latest.txt'), 'r+') as f_read:
        before = f_read.readline()
        if before != latest:
            latest_text = '제목: ' + latest
            latest_link = base_url + link
            bot.sendMessage(chat_id=chat_id, text='새 글 알림 \n' + latest_text + '\n' + latest_link)

        f_read.close()

    with open(os.path.join(BASE_DIR, 'latest.txt'), 'w+') as f_write:
        f_write.write(latest)
        f_write.close()

    print("SLEEP FOR 60 SECONDS")
    time.sleep(60)


driver.quit()
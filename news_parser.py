from selenium import webdriver
from urllib.request import urlopen
from bs4 import BeautifulSoup
import json
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

base_url = 'http://news.naver.com/'
url = 'http://news.naver.com/'
driver = webdriver.Chrome('C:\hyunwoo_workspace\python\chromedriver', chrome_options=options)

driver.get(url)
content = driver.page_source
soup = BeautifulSoup(content, 'lxml')

news_titles = soup.find_all('a')
# news_titles = soup.select('#text_today_main_news_428288 > li > div > a')

with open(os.path.join(BASE_DIR, 'new_titles.txt'), 'w+') as f_write:
    for s in news_titles:
        f_write.write(s.get_text() + '\n')

    f_write.close()

HasClassName = soup.find_all('class')

with open(os.path.join(BASE_DIR, 'news_classNames.json'), 'w+') as json_file:
    json.dump(HasClassName, json_file)
driver.close()

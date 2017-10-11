from crawler import Crawler
import lxml
from bs4 import BeautifulSoup
import urllib.request

category_URL = ["http://news.naver.com/main/main.nhn?mode=LSD&mid=shm&sid1=100",
                "http://news.naver.com/main/main.nhn?mode=LSD&mid=shm&sid1=101",
                "http://news.naver.com/main/main.nhn?mode=LSD&mid=shm&sid1=102",
                "http://news.naver.com/main/main.nhn?mode=LSD&mid=shm&sid1=103",
                "http://news.naver.com/main/main.nhn?mode=LSD&mid=shm&sid1=104",
                "http://news.naver.com/main/main.nhn?mode=LSD&mid=shm&sid1=105",
                ]

politics_URL = "http://news.naver.com/main/main.nhn?mode=LSD&mid=shm&sid1=100"
source_code_from_URL = urllib.request.urlopen(politics_URL)
soup = BeautifulSoup(source_code_from_URL, 'lxml', from_encoding='UTF8')


div_maincontent = soup.find('div', attrs={'id':'main_content'})
politics_URL_list = []
for link in div_maincontent.findAll('a'):
    if 'href' in link.attrs:
        if "http://news.naver.com/main/read.nhn?" in link.attrs['href']:
            politics_URL_list.append(link.attrs['href'])


for link in politics_URL_list:
    Crawler.crawler(link)
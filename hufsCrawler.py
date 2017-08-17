import requests
from bs4 import BeautifulSoup as bs

req = requests.get('http://www.hufs.ac.kr/user/indexSub.action?codyMenuSeq=37079&siteId=hufs&menuType=T&uId=4&sortChar=AB&linkUrl=04_0202.html&mainFrame=right')
html = req.text
soup = bs(html, 'html.parser')
notice_list = soup.select('td.title > a')
for notice in notice_list:
    print(notice.text.strip())
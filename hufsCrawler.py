import requests
from bs4 import BeautifulSoup as bs

targetUri = 'http://www.hufs.ac.kr/user/indexSub.action?codyMenuSeq=37079&siteId=hufs'
req = requests.get(targetUri)
html = req.text
soup = bs(html, 'html.parser')
notice_list = soup.select('td.title > a')
for notice in notice_list:
    print(notice.text.strip())
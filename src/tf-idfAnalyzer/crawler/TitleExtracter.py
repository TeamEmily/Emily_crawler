import lxml
from bs4 import BeautifulSoup
import urllib.request

def titleExtracter(URL):
    title = ""
    source_code_from_URL = urllib.request.urlopen(URL)
    soup = BeautifulSoup(source_code_from_URL, 'lxml', from_encoding='utf-8')

    for item in soup.find_all('h3', id='articleTitle'):
        title = title + str(item.find_all(text=True))

    return title

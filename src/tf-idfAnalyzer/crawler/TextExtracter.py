import lxml
from bs4 import BeautifulSoup
import urllib.request

def textExtracter(URL):
    text = ""
    source_code_from_URL = urllib.request.urlopen(URL)
    soup = BeautifulSoup(source_code_from_URL, 'lxml', from_encoding='utf-8')

    for item in soup.find_all('div', id='articleBodyContents'):
        text = text + str(item.find_all(text=True))

    return text
import lxml
from bs4 import BeautifulSoup
import urllib.request

def articleDataExtracter(URL):

    htmlcode = urllib.request.urlopen(URL)
    soup = BeautifulSoup(htmlcode, 'lxml', from_encoding='utf-8')
    text = textExtracter(soup)
    title = titleExtracter(soup)
    id = IDExtracter(URL)

    return (text, title, id)

def textExtracter(soup):
    text = ""
    for item in soup.find_all('div', id='articleBodyContents'):
        text = text + str(item.find_all(text=True))
    return text


def titleExtracter(soup):
    title = ""
    for item in soup.find_all('h3', id='articleTitle'):
        title = title + str(item.find_all(text=True))
    return title


def IDExtracter(URL):
    URL_param = URL.split("?")
    URL_param2 = URL_param[1].split("&")
    for n in URL_param2:
        if n[0:3] == 'aid':
            URL_iid = n
    id = URL_iid.split("=")[1]
    return id
#-*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import urllib.request
import os
import lxml

def getArticle(URI):
    source_code_from_URL = urllib.request.urlopen(URI)
    soup = BeautifulSoup(source_code_from_URL, 'lxml', from_encoding='utf-8')
    text = ''

    for item in soup.find_all('div', id='articleBodyContents'):
        text = text + str(item.find_all(text=True))

    return text
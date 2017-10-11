import lxml
from bs4 import BeautifulSoup
import urllib.request
from konlpy.tag import Twitter
from articleDataExtracter import textExtracter
import os
import json
import math


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = BASE_DIR + "\data"

with open(os.path.join(DATA_DIR, 'articleDict.json'), 'r') as f:
    article_list = json.load(f)

def num_container(word):
    count = 1
    currentWordDict = {}
    article_keys = article_list.keys()
    for i in article_keys:
        currentWordDict = article_list[i]
        try:
            currentWordDict[word]
            count = count + 1
        except KeyError:
            continue
    return count

def test(word1, word2):
    count = 1
    currentWorDict = {}
    article_keys = article_list.keys()
    for i in article_keys:
        currentWordDict = article_list[i]
        try:
            currentWordDict[word1]
            try:
                currentWordDict[word2]
                count = count + 1
            except KeyError:
                continue
        except KeyError:
            continue
    return count

URL = "http://news.naver.com/main/read.nhn?mode=LSD&mid=shm&sid1=100&oid=001&aid=0009598735"
htmlcode = urllib.request.urlopen(URL)
soup = BeautifulSoup(htmlcode, 'lxml', from_encoding='utf-8')
text = textExtracter(soup)

twitter = Twitter()
tokens = twitter.pos(text)

tupleList = []
for i in range(0, len(tokens)):
    if tokens[i][1] == 'Noun':
        if tokens[i+1][1] == 'Noun':
            tuple = (tokens[i][0], tokens[i+1][0])
            tupleList.append(tuple)

PMI_list = []
for i in tupleList:
    P_X = num_container(i[0]) / len(article_list)
    P_Y = num_container(i[1]) / len(article_list)
    P_XY = test(i[0], i[1]) / len(article_list)
    PMI = math.log( P_XY / (P_X * P_Y))
    temp_a = i[0]+","+i[1]
    PMI_tuple = (temp_a, PMI)
    PMI_list.append(PMI_tuple)

def score(s):
    return s[1]
PMI_list.sort(key=score, reverse=True)
print(PMI_list)
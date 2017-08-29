import tokenizer
import crawler
import dictManager
import math
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
URL = "http://news.naver.com/main/hotissue/read.nhn?mid=hot&sid1=100&cid=1049580&iid=1233048&oid=001&aid=0009505529&ptype=052"
article = crawler.getArticle(URL)
wordFrecDict = tokenizer.getWordFrequencyDict(article)
dictManager.newArticleDict(wordFrecDict, URL)

accumDict = {}
with open(os.path.join(BASE_DIR, 'freq_all.json'), 'r', encoding='UTF8') as w:
    json.dump(accumDict, w)

def get_tf(word):
    print (wordFrequencyDict[word], len(wordFrequencyDict))
    return wordFrequencyDict[word]/len(wordFrequencyDict)

def num_container(word):
    with open(os.path.join(BASE_DIR, 'articleDict.json'), 'r+', encoding='UTF8') as r:
        listData = json.load(r)

    keyList = listData.keys()
    num = 1
    for n in keyList:
        if listData[n] is word:
            num = num + 1
    return num


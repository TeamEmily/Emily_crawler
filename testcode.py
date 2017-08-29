import dictManager
import crawler
import tokenizer
import json
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
URL = "http://news.naver.com/main/hotissue/read.nhn?mid=hot&sid1=100&cid=1049580&iid=1233150&oid=003&aid=0008146852&ptype=052"
text = crawler.getArticle(URL)
wordFreqDict = tokenizer.getWordFrequencyDict(text)
dictManager.newArticleDict(wordFreqDict, URL)
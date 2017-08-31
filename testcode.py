import json
import os
import crawler
import tokenizer
import dictManager
import sys
import time

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
URL_list = ["http://news.naver.com/main/read.nhn?mode=LSD&mid=shm&sid1=102&oid=001&aid=0009511671",
            "http://news.naver.com/main/read.nhn?mode=LSD&mid=shm&sid1=102&oid=003&aid=0008152728",
            "http://news.naver.com/main/read.nhn?mode=LSD&mid=shm&sid1=102&oid=005&aid=0001022404",
            "http://news.naver.com/main/read.nhn?mode=LSD&mid=shm&sid1=102&oid=001&aid=0009511629",
            "http://news.naver.com/main/read.nhn?mode=LSD&mid=shm&sid1=102&oid=001&aid=0009512069",
            "http://news.naver.com/main/read.nhn?mode=LSD&mid=shm&sid1=102&oid=277&aid=0004065624",
            "http://news.naver.com/main/read.nhn?mode=LSD&mid=shm&sid1=102&oid=001&aid=0009511426",
            "http://news.naver.com/main/read.nhn?mode=LSD&mid=shm&sid1=102&oid=277&aid=0004065675",
            "http://news.naver.com/main/read.nhn?mode=LSD&mid=shm&sid1=102&oid=005&aid=0001022403",
            "http://news.naver.com/main/read.nhn?mode=LSD&mid=shm&sid1=102&oid=003&aid=0008152696",
            "http://news.naver.com/main/read.nhn?mode=LSD&mid=shm&sid1=102&oid=016&aid=0001284263",
            "http://news.naver.com/main/read.nhn?mode=LSD&mid=shm&sid1=102&oid=003&aid=0008151574",
            "http://news.naver.com/main/read.nhn?mode=LSD&mid=shm&sid1=102&oid=001&aid=0009511597",
            "http://news.naver.com/main/read.nhn?mode=LSD&mid=shm&sid1=102&oid=008&aid=0003927643",
            "http://news.naver.com/main/read.nhn?mode=LSD&mid=shm&sid1=102&oid=001&aid=0009512045",
            "http://news.naver.com/main/read.nhn?mode=LSD&mid=shm&sid1=102&oid=001&aid=0009511544",
            "http://news.naver.com/main/read.nhn?mode=LSD&mid=shm&sid1=102&oid=021&aid=0002325959",
            "http://news.naver.com/main/read.nhn?mode=LSD&mid=shm&sid1=102&oid=001&aid=0009511415",
            "http://news.naver.com/main/read.nhn?mode=LSD&mid=shm&sid1=102&oid=001&aid=0009511406"
            ]

for n in URL_list:
    text = crawler.getArticle(n)
    wordFreqDict = tokenizer.getWordFrequencyDict(text)
    dictManager.newArticleDict(wordFreqDict, n)
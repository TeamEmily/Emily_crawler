import tokenizer
import crawler
import dictManager
import math
import os
import json

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
with open(os.path.join(BASE_DIR, 'articleDict.json'), 'r') as f:
    article_list = json.load(f)
with open(os.path.join(BASE_DIR, 'freq_all.json'), 'r') as f:
    accumulatedDict = json.load(f)

def get_tf(word):
    return dict[word]/len(dict)

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

def num_articles():
    return len(article_list)

def get_idf(word):
    return math.log(num_articles() / num_container(word))

def get_tfidf(word):
    return get_tf(word) * get_idf(word)
URL = "http://news.naver.com/main/read.nhn?mode=LSD&mid=shm&sid1=102&oid=277&aid=0004065488"
text = crawler.getArticle(URL)
dict = tokenizer.getWordFrequencyDict(text)

result = {}
for word in dict.keys():
    result[word] = get_tfidf(word)

sorted_result = sorted(result, key=result.get, reverse=True)
result_sorted = {}

for n in sorted_result:
    result_sorted[n] = result[n]

print(result_sorted)
import math
import os
import json
from collections import Counter

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = BASE_DIR + "\data"

with open(os.path.join(DATA_DIR, 'articleDict.json'), 'r') as f:
    article_list = json.load(f)
with open(os.path.join(DATA_DIR, 'freq_all.json'), 'r') as f:
    accumulatedDict = json.load(f)

def get_tf(word, wordDict):
    return wordDict[word]/len(wordDict)

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

def get_tfidf(word, wordDict):
    return get_tf(word, wordDict) * get_idf(word)


def TFIDF_Analyzer(WordFrequencyDictionary):
    result = {}
    for word in WordFrequencyDictionary.keys():
        result[word] = get_tfidf(word, WordFrequencyDictionary)

    sorted_result = sorted(result, key=result.get, reverse=True)
    result_sorted = {}

    for n in sorted_result:
        result_sorted[n] = result[n]

    c = Counter(result_sorted)
    Keywords = c.most_common(10)
    print(Keywords)
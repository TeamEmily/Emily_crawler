import json
import os
import getURL_ID

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
def freqAccumulator(wordFreqDict):
    data = {}
    with open(os.path.join(BASE_DIR, 'freq_all.json'), 'r', encoding='UTF8') as f:
        data = json.load(f)

    key_list = wordFreqDict.keys()
    for n in key_list:
        try:
            data[n]
        except KeyError:
            data[n] = wordFreqDict[n]
            continue
        data[n] = data[n] + wordFreqDict[n]

    with open(os.path.join(BASE_DIR, 'freq_all.json'), 'w', encoding='UTF8') as f:
        json.dump(data, f)

def newArticleDict(wordFreqDict, URI):
    data = {}
    with open(os.path.join(BASE_DIR, 'articleDict.json'), 'r') as f:
        data = json.load(f)

    URL_ID = getURL_ID.getID(URI)

    keyExists = 0
    key_list = data.keys()
    for n in key_list:
        if n == URL_ID:
            keyExists = 1
            break

    if keyExists is 0:
        data[URL_ID] = wordFreqDict
        freqAccumulator(wordFreqDict)
    else:
        print("YOU ALREADY ACCUMULATED THIS WORD FREQUENCY DICTIONARY")

    with open(os.path.join(BASE_DIR, 'articleDict.json'), 'w', encoding='UTF8') as f:
        json.dump(data, f)
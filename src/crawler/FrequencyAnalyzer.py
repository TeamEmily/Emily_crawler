from konlpy.tag import Twitter
import nltk

def FreqAnalyzer(text):
    twitter = Twitter()
    tokens_ko = twitter.nouns(text)
    ko = nltk.Text(tokens_ko, name='뉴스기사')

    frequency = {}
    for n in tokens_ko:
        frequency[n] = ko.count(n)
    sorted_word = sorted(frequency, key=frequency.get, reverse=True)
    frequency_sorted = {}

    for n in sorted_word:
        frequency_sorted[n] = frequency[n]

    return frequency_sorted
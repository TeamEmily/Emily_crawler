from .DictionaryManager import newArticleDict
from .FrequencyAnalyzer import FreqAnalyzer
from .IDExtracter import IDExtracter
from .TextExtracter import textExtracter
from .KeywordExtracter import TFIDF_Analyzer


def crawler(URL):
    print("START EMILY CRAWLER")
    text = textExtracter(URL)
    articleID = IDExtracter(URL)
    wordFrequencyDictionary = FreqAnalyzer(text)
    newArticleDict(wordFrequencyDictionary, articleID)
    TFIDF_Analyzer(wordFrequencyDictionary)
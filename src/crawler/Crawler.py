from .DictionaryManager import newArticleDict
from .FrequencyAnalyzer import FreqAnalyzer
from .articleDataExtracter import articleDataExtracter
from .KeywordExtracter import TFIDF_Analyzer
import pymysql.cursors
import time

conn = pymysql.connect(host='175.208.189.127', port=3306, user='admin', password='1234', db='emily', charset='utf8mb4')

def crawler(URL):
    dataTuple = articleDataExtracter(URL)
    text = dataTuple[0]
    title = dataTuple[1]
    articleID = dataTuple[2]
    articleLink = URL
    wordFrequencyDictionary = FreqAnalyzer(text)
    newArticleDict(wordFrequencyDictionary, articleID)
    keyword_list = TFIDF_Analyzer(wordFrequencyDictionary)
    #
    # try:
    #     with conn.cursor() as cursor:
    #         sql = 'INSERT INTO test (id, test) VALUES (%s, %s) ON DUPLICATE KEY UPDATE id=VALUES(id)'
    #         cursor.execute(sql, (articleID, )
    #     conn.commit()
    # finally:
    #     print("DB UPDATED")
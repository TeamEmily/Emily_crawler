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
    wordFrequencyDictionary = FreqAnalyzer(text)
    newArticleDict(wordFrequencyDictionary, articleID)
    keyword_list = TFIDF_Analyzer(wordFrequencyDictionary)

    time.sleep(3)

    try:
        with conn.cursor() as cursor:
            sql = 'INSERT INTO articles (id, title, keyword1, keyword2, keyword3, keyword4, keyword5, category) VALUES (%s, %s, %s, %s, %s, %s, %s, %s) ON DUPLICATE KEY UPDATE id = VALUES(id)'
            cursor.execute(sql, (articleID, title, keyword_list[0][0], keyword_list[1][0], keyword_list[2][0], keyword_list[3][0], keyword_list[4][0], '정치'))
        conn.commit()
    finally:
        print("DB UPDATED")
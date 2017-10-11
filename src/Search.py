import pymysql.cursors

conn = pymysql.connect(host='175.208.189.127', port=3306, user='admin', password='1234', db='emily', charset='utf8mb4')
searchWord = "일병"

try:
    with conn.cursor(pymysql.cursors.DictCursor) as cursor:
        sql = 'SELECT * FROM articles WHERE keyword1=%s or keyword2=%s or keyword3=%s or keyword4=%s or keyword5=%s'
        cursor.execute(sql, (searchWord,searchWord,searchWord,searchWord,searchWord))
        result = cursor.fetchall()

        print( "SEARCH WORD is ", searchWord)
        for i in result:
            print(i['title'], i['category'])
finally:
    print("IM DONE!")
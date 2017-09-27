import pymysql.cursors

conn = pymysql.connect(host='175.208.189.127', port=3306, user='admin', password='1234', db='emily', charset='utf8mb4')

try:
    with conn.cursor(pymysql.cursors.DictCursor) as cursor:
        sql = 'DELETE FROM articles WHERE date(updatedate)=date(subdate(now(), INTERVAL 3 DAY))'
        cursor.execute(sql)

    conn.commit()
    print(cursor.rowcount)
finally:
    conn.close()
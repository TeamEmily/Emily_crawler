import pymysql.cursors
import sys
conn = pymysql.connect(host='125.132.213.135', user='root', password='1234', db='emily', charset='utf8mb4')

def WeatherSearch(Date, City):
    searchWord = City
    if (Date=='오늘'):
        try:
            with conn.cursor(pymysql.cursors.DictCursor) as cursor:
                sql = 'SELECT * FROM Weather_Today WHERE city_name=%s'
                cursor.execute(sql, (searchWord))
                result = cursor.fetchall()

                print( "SEARCH WORD is ", searchWord)
                for i in result:
                    replyMessage = searchWord + "의 오늘 오전 기온은" + i['morn_temp'] +  "도 이며," + i['morn_weather'] + "이며, " + i['morn_precipi'] + "의 강수량이 예상됩니다. "
                    replyMessage2 = "또한 오후는" + i['noon_temp'] + "도 이며, " + i['morn_weather'] + "이며," + i['morn_precipi'] + "의 강수량이 예상됩니다."
                    FinalMessage = replyMessage + replyMessage2
        finally:
            print("IM DONE!")

    if (Date == '내일'):
        try:
            with conn.cursor(pymysql.cursors.DictCursor) as cursor:
                sql = 'SELECT * FROM Weather_Tomorrow WHERE city_name=%s'
                cursor.execute(sql, (searchWord))
                result = cursor.fetchall()

                print( "SEARCH WORD is ", searchWord)
                for i in result:
                    replyMessage = searchWord + "의 내일 오전 기온은" + i['morn_temp'] + "도 이며," + i['morn_weather'] + "이며, " + i['morn_precipi'] + "의 강수량이 예상됩니다. "
                    replyMessage2 = "또한 오후는" + i['noon_temp'] + "도 이며, " + i['morn_weather'] + "이며," + i['morn_precipi'] + "의 강수량이 예상됩니다."
                    FinalMessage = replyMessage + replyMessage2
        finally:
            print("IM DONE!")

    return FinalMessage
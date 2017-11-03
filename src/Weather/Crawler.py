#-*- coding: utf-8 -*-

import lxml
from bs4 import BeautifulSoup
import urllib.request
import pymysql.cursors
import os
import json

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
conn = pymysql.connect(host='125.132.213.135', user='emily', password='1234', db='emily', charset='utf8mb4')
with open(os.path.join(BASE_DIR, 'city_code.json'), 'r', encoding='UTF8') as f:
    data = json.load(f)

BASE_URL = "http://weather.naver.com/rgn/cityWetrCity.nhn?cityRgnCd=CT"

def WeatherCrawler(URL):
    htmlcode = urllib.request.urlopen(URL)
    soup = BeautifulSoup(htmlcode, 'lxml', from_encoding='utf-8')
    item = soup.find_all("div", {"class": "cell"})
    weatherlist = []
    for i in item:
        text = i.find_all(text=True)
        for j in range(0, len(text)):
            if (text.count("\n")==0):
                break
            text.remove("\n")

        for j in range(0, len(text)):
            if (text.count(" ")==0):
                break
            text.remove(" ")
        weatherlist.append(text)

    return weatherlist


# 0 - today.morning (1-temp, 3-weather, 5-precip)
# 1 - today.noon (1-temp, 3-weather, 5-precip)
# 2 - tomorrow.morning (1-temp, 3-weather, 5-precip)
# 3 - tomorrow.noon (1-temp, 3-weather, 5-precip)
# 4 - ...
try:
    with conn.cursor() as cursor:
        sql = 'DELETE FROM Weather_Today'
        cursor.execute(sql)
    conn.commit()
finally:
    print("ALL ROWS DELETED")

for i in data:
    URL = BASE_URL + i["city_code"]
    temp = WeatherCrawler(URL)
    try:
        with conn.cursor() as cursor:
            sql = 'INSERT INTO Weather_Today (city_name, morn_temp, morn_weather, morn_precipi, noon_temp, noon_weather, noon_precipi) VALUES (%s, %s, %s, %s, %s, %s, %s)'
            cursor.execute(sql,(i["city_name"], temp[0][1], temp[0][3], temp[0][5], temp[1][1], temp[1][3], temp[1][5]))
        conn.commit()
    finally:
        print("TODAY WEATHER UPDATED")

    try:
        with conn.cursor() as cursor:
            sql = 'INSERT INTO Weather_Tomorrow (city_name, morn_temp, morn_weather, morn_precipi, noon_temp, noon_weather, noon_precipi) VALUES (%s, %s, %s, %s, %s, %s, %s)'
            cursor.execute(sql,(i["city_name"], temp[2][1], temp[2][3], temp[2][5], temp[3][1], temp[3][3], temp[3][5]))
        conn.commit()
    finally:
        print("TOMORROW WEATHER UPDATED")

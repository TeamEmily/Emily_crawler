import pymysql.cursors
import json
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = BASE_DIR

conn = pymysql.connect(host='192.168.0.13', user='root', password='1234', db='emily', charset='utf8mb4')

data = {}
with open(os.path.join(DATA_DIR, 'teaminfo.json'), 'r', encoding='UTF8') as f:
    data = json.load(f)



tuple = data['teaminfo']
for i in range(0, len(tuple)):
    try:
        with conn.cursor() as cursor:
            sql = 'INSERT INTO teams (team_id, team_name, team_stadium, team_manager) VALUES (%s, %s, %s, %s)'
            cursor.execute(sql, (i, tuple[i]['team'], tuple[i]['stadium'], tuple[i]['manager']))
        conn.commit()
    finally:
        print(tuple[i]['team'] + " - INFORMATION UPDATED!!")
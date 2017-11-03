import pymysql.cursors
import json
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = BASE_DIR

conn = pymysql.connect(host='125.132.213.135', user='emily', password='1234', db='emily', charset='utf8mb4')

with open(os.path.join(DATA_DIR, 'players.json'), 'r', encoding='UTF8') as f:
    players = json.load(f)

count = 0

for i in range(0, len(players)):
    a = list(players[i].keys())
    b = players[i][a[0]]

    for j in range(0, len(b)):
        try:
            with conn.cursor() as cursor:
                sql = 'INSERT INTO players SET pl_id = %s, pl_name = %s, pl_position = %s, team_id = (SELECT team_id FROM teams WHERE team_name = %s) on duplicate key update pl_id = %s'
                cursor.execute(sql, (count, b[j]['playerName'], b[j]['position'], a[0], count))
            conn.commit()
        finally:
            print("GOOD")
        count = count+1
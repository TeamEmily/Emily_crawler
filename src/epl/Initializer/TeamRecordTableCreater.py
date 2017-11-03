import pymysql.cursors

conn = pymysql.connect(host='192.168.0.13', user='root', password='1234', db='emily', charset='utf8mb4')

Teamlist = ["Arsenal", "Bournemouth", "Brighton", "Burnley", "Chelsea", "C.Palace", "Everton", "Huddersfield", "Leicester", "Liverpool", "Man City", "Man UTD", "Newcastle", "So'ton", "Stoke", "Swansea", "Tottenham", "Watford", "West BA", "West Ham"]
Gamenum = 10
WinscoreList = [19, 7, 12, 16, 19, 4, 8, 12, 12, 16, 28, 23, 14, 13, 11, 8, 20, 15, 10, 9]
WinnumList = [6, 2, 3, 4, 6, 1, 2, 3, 3, 4, 9, 7, 4, 3, 3, 2, 6, 4, 2, 2]
LosenumList = [3, 7, 4, 2, 3, 8, 6, 4, 4, 2, 0, 1, 4, 3, 5, 6, 2, 3, 4, 5]
DrawnumList = [1, 1, 3, 4, 1, 1, 2, 3, 3, 4, 1, 2, 2, 4, 2, 2, 2, 3, 4, 3]
GoalscoreList = [19, 6, 10, 9, 18, 4, 7, 7, 14, 17, 35, 23, 10, 9, 11, 7, 19, 15, 9, 10]
LosescoreList = [13, 14, 11, 9, 10, 21, 20, 13, 14, 16, 6, 4, 9, 10, 20, 12, 7, 18, 13, 19]
DifgoalloseList = [6, -8, -1, 0, 8, -17, -13, -6, 0, 1, 29, 19, 1, -1, -9, -5, 12, -3, -4, -9]


for i in range(0, 19):
    try:
        with conn.cursor() as cursor:
            sql = 'INSERT INTO teamrecord (Teamname, Winscore, Playedgames, Winnum, Losenum, Drawnum, Goalscore, Losepoint, Difgoallose) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)'
            cursor.execute(sql, (Teamlist[i], WinscoreList[i], Gamenum, WinnumList[i], LosenumList[i], DrawnumList[i], GoalscoreList[i], LosescoreList[i], DifgoalloseList[i]))
        conn.commit()
    finally:
        print(Teamlist[i] + " - Record UPDATED!!")
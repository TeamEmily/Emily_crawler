import time
import telepot
from Weather.WeatherSearch import WeatherSearch
import requests
import json

URL = "http://125.132.213.135:8080/search/?str="

def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    if content_type == 'text':
        text = msg['text']
        temp = URL + text
        res = requests.get(temp)


        obj = json.loads(res.text)
        intent = obj["intent"]


        if intent == "rank_team":
            data = obj["data"]

            for a in data:
                str1 = "------ About : " + a['teamname'] + "  Record ------ \n"
                str2 = "Winscore : " + str(a['winscore']) + "\n"
                str3 = "Playedgames : " + str(a['playedgames']) + "\n"
                str4 = str(a['winnum']) + " - " + str(a['losenum']) + " - " + str(a['drawnum']) + "\n"
                str5 = "Goal Score : " + str(a['goalscore']) + "\n"
                str6 = "Lost Goal Score : " + str(a['losepoint']) + "\n"
                str7 = "Difference of Goal and Lose : " + str(a['difgoallose']) + "\n"
                FinalMessage = str1+str2+str3+str4+str5+str6+str7
                bot.sendMessage(chat_id, FinalMessage)
        if intent == "weather":
            Date = obj["params"]["Date"]
            City = obj["params"]["City"]
            replyMessage = WeatherSearch(Date[0], City[0])
            bot.sendMessage(chat_id, replyMessage)


TOKEN = '346845203:AAHZO2zdCwQzro_7DphpCxxIoPKXlLPTcqM'

bot = telepot.Bot(TOKEN)
bot.message_loop(handle)
print('Listening...')

while 1:
    time.sleep(10)
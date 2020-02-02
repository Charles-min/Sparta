import requests
from bs4 import BeautifulSoup

from pymongo import MongoClient           # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)
client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.dbsparta                      # 'dbsparta'라는 이름의 db를 만듭니다

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://www.genie.co.kr/chart/top200?ditc=D&rtm=N&ymd=20190908',headers=headers)


soup = BeautifulSoup(data.text, 'html.parser')

# select를 이용해서, tr들을 불러오기

music_info = soup.select('#wrap-main > #wrap-body > #body-content > .newest-list > .music-list-wrap > .list-wrap > tbody > tr')
rank = 1

for music in music_info:
    # movie 안에 a 가 있으면, console 우클릭 copy selector로 확인
    music_tag = music.select_one('tr.list > td.info')

    if music_tag is not None:
        artist = music.select_one('a.artist').text
        title = music.select_one('a.title').text.strip()

        doc = {
            'rank': rank,
            'title': title,
            'artist': artist
        }
        db.music_info.insert_one(doc)
        rank += 1


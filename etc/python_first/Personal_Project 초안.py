import requests
from bs4 import BeautifulSoup

from pymongo import MongoClient           # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)
client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.dbsparta

url = 'http://www.law.go.kr/DRF/lawService.do?OC=tkdals1879&target=prec&ID={}&type=XML'
def request_url(precedent_num):
    return url.format(precedent_num)

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}

def scarping_raw_precedent(precedent_num):

    data = requests.get(request_url(precedent_num), headers=headers)
    soup = BeautifulSoup(data.text, 'html.parser')


import requests

r = requests.get('https://api.stlouisfed.org/fred/series/observations?series_id=NASDAQCOM&api_key=85426e6b38e5d2dc8391645531093de2&file_type=json&observation_start=2020-01-01')

rjson = r.json()

dates = rjson['observations']

for i in dates:
    dic_dates = i.get('date')
    dic_values = i.get('value')

    if dic_dates == '2020-01-02':
        print(dic_values)


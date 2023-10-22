import requests
import json


headers = {
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Language': 'ru,en;q=0.9',
    'Connection': 'keep-alive',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 YaBrowser/23.7.5.739 Yowser/2.5 Safari/537.36',
    'X-Current-UID': '1793348404',
    'X-Requested-With': 'XMLHttpRequest',
    'X-Retpath-Y': 'https://music.yandex.ru/chart',
    'X-Yandex-Music-Client-Now': '2023-09-21T13:27:42+03:00',
    'Y-Browser-Experiments': 'NjczMTM3LDAsMzE=',
    'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "YaBrowser";v="23"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

params = {
    'what': 'chart',
    'lang': 'ru',
    'external-domain': 'music.yandex.ru',
    'overembed': 'false',
    'ncrnd': '0.8599263673920186',
}

response = requests.get(
    'https://music.yandex.ru/handlers/main.jsx',
    params=params,  headers=headers
)


res = {}
for chart in response.json()['chartPositions']:
    track = chart['track']
    res[chart['chartPosition']['position']] = {
        track['title']: [artist['name'] for artist in track['artists']]
    }

with open('ya_mus_parsed_data.json', 'w', encoding='utf-8') as outfile:
    json.dump(res, outfile, ensure_ascii=False)
    
from bs4 import BeautifulSoup
import json
import time
import requests

games_prices = {}
zaka_url = 'https://zaka-zaka.com/game/new'

for page_num in range(1, 21):
    url = zaka_url + "/page{}".format(page_num)
    response = requests.get(url)
    print('Collecting data from page {}...'.format(page_num))

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'lxml')
        containers = soup.find_all(class_='game-block')
        for container in containers:
            if "game-block-more" in container.get("class"):
                continue
            name = container.find(class_="game-block-name")
            price = container.find(class_="game-block-price")
            games_prices[name.text] = {"price": float(price.text[:-1])}
    else:
        print('Error:', response.status_code)


with open("zaka_parsed_data.json", "w") as json_file:
    json.dump(games_prices, json_file)

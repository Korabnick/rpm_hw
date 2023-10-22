from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from time import sleep
from time import time
from sys import exit

print('Введите любой символ, кроме числа, чтобы выйти.')
input_time = input('Введите количество времени (в секундах), которое будет работать бот: ')
try:
    input_time = float(input_time)
except ValueError:
    print('Вы вышли из бота!')
    exit()

options = Options()
options.binary_location = r"C:\Program Files\Mozilla Firefox\firefox.exe"
driver = webdriver.Firefox(options=options)

driver.get("https://www.invokergame.com/")
sleep(1)
survival_find = driver.find_element(By.XPATH, "/html/body/form/div[3]/div[6]/div[2]/div[2]/div/table/tbody/tr[2]/td[1]/input")
survival_find.click()

sleep(1)
survival_find = driver.find_element(By.XPATH, "/html/body/form/div[3]/div[3]/div/table/tbody/tr/td[3]/a")
survival_find.click()

sleep(1)
startgame = driver.find_element(By.XPATH, "/html/body/form/div[3]/div[6]/div[2]/div[3]/div[1]/nobr/table/tbody/tr/td/input")
startgame.click()

spell_combinations = {
    "Cold Snap": ["q", "q", "q", "r", "d", "f"],
    "Ghost Walk": ["q", "q", "w", "r", "d", "f"],
    "Ice Wall": ["q", "q", "e", "r", "d", "f"],
    "EMP": ["w", "w", "w", "r", "d", "f"],
    "Tornado": ["w", "w", "q", "r", "d", "f"],
    "Alacrity": ["w", "w", "e", "r", "d", "f"],
    "Sun Strike": ["e", "e", "e", "r", "d", "f"],
    "Forge Spirit": ["e", "e", "q", "r", "d", "f"],
    "Chaos Meteor": ["e", "e", "w", "r", "d", "f"],
    "Deafening Blast": ["q", "w", "e", "r", "d", "f"],}

stop_flag = time() + float(input_time)

while stop_flag > time():
    for spell, combination in spell_combinations.items():
        xpath = f'//*[@id="Spell_{list(spell_combinations.keys()).index(spell)}"]'

        try:
            spell_element = driver.find_element(By.XPATH, xpath)
            if spell_element.text == spell:
                for key in combination:
                    driver.find_element(By.TAG_NAME, 'body').send_keys(key)
        except:
            pass

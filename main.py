import requests
from bs4 import BeautifulSoup as BS

r = requests.get('https://stopgame.ru/topgames?p=1')

html = BS(r.content, 'html.parser')

for el in html.select(".items > .item game-summary game-summary-horiz"):
    title = el.select(".caption > .a")
    print(title[0].text)
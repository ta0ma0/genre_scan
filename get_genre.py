import requests
from bs4 import BeautifulSoup
import time
import enchant
import json

base_url = "https://everynoise.com/lookup.cgi"

list_of_artits = []

with open("list_of_artists.txt") as f:
    data_artistes = f.read()
    list_of_artits = data_artistes.split(";")
d = enchant.Dict("en_US")


genre_dict = {}

with open("dump_of_genres.json") as genres_f:
    genre_dict = json.load(genres_f)

with open("last_position.txt") as lp:
    last_position = lp.read()

position = list_of_artits.index(last_position)
count = position

for el in list_of_artits[position:]:
    count += 1
    genre_list = []
    params = {'who': el, 'mode':'map'}
    response = requests.get(base_url, params=params)
    soup = BeautifulSoup(response.text, "html.parser")
    body = soup.find('body')
    try:
        genres = body.div.find_all('a', href=True)
    except AttributeError:
        pass
    print(el, f"Left {len(list_of_artits) - count} genres or \
          ~ {((len(list_of_artits) - count) * 3) / 60} minutes")
    with open('last_position.txt', 'w') as lp:
        lp.write(el)
    for item in genres:
        try:
            genres_clean = item.text
            genre_list.append(genres_clean)
        except TypeError:
            pass
    genre_dict.update({el: genre_list[:-2]})
    with open('dump_of_genres.json', 'w') as dump:
        json.dump(genre_dict, dump)        
    time.sleep(3)

print(genre_dict)
import requests
from bs4 import BeautifulSoup
import time
import enchant
import json

base_url = "https://everynoise.com/lookup.cgi"

list_of_artits = []


def is_latin(word):
    for char in word:
        if unicodedata.name(char).startswith('LATIN'):
            return True
    return True

with open("list_of_artists_sample.txt") as f:
    data_artistes = f.read()
    list_of_artits = data_artistes.split(";")
# print(list_of_artits)

d = enchant.Dict("en_US")

genre_dict = {}

for el in list_of_artits:
    genre_list = []
    params = {'who': el, 'mode':'map'}
    response = requests.get(base_url, params=params)
    soup = BeautifulSoup(response.text, "html.parser")
    body = soup.find('body')
    genres = body.div.find_all('a', href=True)
    print(el)
    # print(genres)
    for item in genres:
        try:
            genres_clean = item.text
            genre_list.append(genres_clean)
            # print(genres_clean + ';')
        except TypeError as er:
            pass
    genre_dict.update({el:genre_list[:-2]})
    with open('dump_of_genres.json', 'w') as dump:
        json.dump(genre_dict, dump)        
    time.sleep(1)

print(genre_dict)



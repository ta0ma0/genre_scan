import json
import sys

genre = sys.argv[1]

with open("dump_of_genres.json") as f:
    data_genres = json.load(f)

for el in data_genres:
    for item in data_genres[el]:
        if item == genre:
            print(el)
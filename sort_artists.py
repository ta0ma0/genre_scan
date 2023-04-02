import enchant
import unicodedata
import json

def is_latin(word):
    for char in word:
        if unicodedata.name(char).startswith('LATIN'):
            return True
    return False

def is_cyrillic(word):
    for char in word:
        if unicodedata.name(char).startswith('CYRILLIC'):
            return True
    return False




artists_list = []

with open('uniq_artists.txt') as f:
    line = f.readline()
    while line:
        line_clean = line.split(':')[1].strip()
        # print(line_clean)
        line = f.readline()
        if len(line_clean) == 0:
            pass
        else:
            if is_latin(line_clean):
                # print(f"Latin {line_clean}")
                artists_list.append(line_clean)
            elif is_cyrillic(f"Cyrillic {line_clean}"):
                # print(f"Is cyrillic")
                artists_list.append(line_clean)
            else:
                print(f"I don't now")

with open('list_of_artists.txt', 'w') as df:
    df.writelines([word + ';' for word in artists_list])

# print(artists_list)
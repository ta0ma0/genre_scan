import json
from collections import Counter
import csv

with open("dump_of_genres.json") as f:
    data_genres = json.load(f)
# print(data_genres)

unsorted_gen_list = []

for el in data_genres:
    one_list = data_genres[el]
    unsorted_gen_list.extend(one_list)

unsorted_gen_list.sort()
counted_genres = Counter(unsorted_gen_list)

# sort the items in descending order
sorted_items = counted_genres.most_common()

# open a CSV file for writing
with open('output.csv', 'w', newline='') as csvfile:
    # create a CSV writer object
    csvwriter = csv.writer(csvfile)

    # write the header row
    csvwriter.writerow(['genre', 'count'])

    # write each row of data
    for item, count in sorted_items:
        csvwriter.writerow([item, count])


# print(counted_genres)
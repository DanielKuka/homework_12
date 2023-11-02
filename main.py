import pprint
import os
import csv
import json

from ganres_list import ganres
from data_films import films_data

ganres_dict = json.loads(ganres)
print(type(ganres_dict))
pprint.pprint(ganres_dict)


for genre_info in ganres_dict['results']:
    genre_name = genre_info['genre']
    directory_path = os.path.join(os.getcwd(), genre_name)
    os.makedirs(directory_path, exist_ok=True)

    csv_file_path = os.path.join(directory_path, f'{genre_name}_movies.csv')

    with open(csv_file_path, mode='w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['title', 'year', 'rating', 'type', 'genres']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

for film in films_data:
    title = film['title']
    year = film['year']
    rating = film['rating']
    film_type = film['type']
    genres = ";".join([genre['genre'] for genre in film['gen']])

    for genre in film['gen']:
        genre_name = genre['genre']
        directory_path = os.path.join(os.getcwd(), genre_name)
        os.makedirs(directory_path, exist_ok=True)

        csv_file_path = os.path.join(directory_path, f'{genre_name}_movies.csv')

        with open(csv_file_path, mode='a', newline='', encoding='utf-8') as csvfile:
            fieldnames = ['title', 'year', 'rating', 'type', 'genres']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writerow({'title': title, 'year': year, 'rating': rating, 'type': film_type, 'genres': genres})
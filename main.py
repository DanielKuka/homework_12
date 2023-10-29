import os 
import string
import pprint

from hide_code_1 import films_titles
from hide_code_2 import  films_awards

os.mkdir("Harry Potter")


for film in films_titles["results"]:
    directory_name = film["title"]
    directory_name = directory_name.replace(" ", "_").replace("'", "")
    os.mkdir(os.path.join("Harry Potter", directory_name))

letters = string.ascii_uppercase

for film in films_titles["results"]:
    directory_name = film["title"]
    directory_name = directory_name.replace(" ", "_").replace("'", "")
    film_directory = os.path.join("Harry Potter", directory_name)
    
    for letter in letters:
        os.mkdir(os.path.join(film_directory, letter))

film_awards_list = []

for film_info in films_awards[0]['results']:
    movie_title = film_info['movie']['title']
    award_name = film_info['award_name']
    award_type = film_info['type']
    award = film_info['award']
    
    award_dict = {'type': award_type, 'award_name': award_name, 'award': award}
    
    film_awards_list.append(award_dict)

# pprint.pprint(film_awards_list)

film_awards_list = sorted(film_awards_list, key=lambda x: x['award_name'])

# for film_awards in film_awards_list:
#     pprint.pprint(film_awards)


for film in films_titles["results"]:
    movie_title = film["title"]
    directory_name = movie_title.replace(" ", "_").replace("'", "")
    film_directory = os.path.join("Harry Potter", directory_name)
    
    for film_info in films_awards[0]['results']:
        award_name = film_info['award_name']
        award_type = film_info['type']
        award = film_info['award']

        award_dict = {'type': award_type, 'award_name': award_name, 'award': award}

        for letter in letters:
            letter_directory = os.path.join(film_directory, letter)

            if award_name.startswith(letter):
                os.makedirs(letter_directory, exist_ok=True)

                award_file_name = os.path.join(letter_directory, f"{award_name}.txt")
                with open(award_file_name, 'w') as award_file:
                    award_file.write(f"Фільм: {movie_title}\n")
                    award_file.write(f"Тип нагороди: {award_type}\n")
                    award_file.write(f"Нагорода: {award}\n")

for film in films_titles["results"]:
    movie_title = film["title"]
    directory_name = movie_title.replace(" ", "_").replace("'", "")
    film_directory = os.path.join("Harry Potter", directory_name)
    
    for letter in letters:
        letter_directory = os.path.join(film_directory, letter)
        
        for award_info in films_awards[0]['results']:
            award_name = award_info['award_name']
            award_type = award_info['type']
            award = award_info['award']
            
            if award_info['movie']['title'] == movie_title:
                if award_name.startswith(letter):
                    award_file_name = os.path.join(letter_directory, f"{award_name}.txt")
                    with open(award_file_name, 'a') as award_file:
                        if award not in open(award_file_name).read():
                            award_file.write(f"{award}\n")
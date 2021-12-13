import csv
import random
import json

film_list = ["Random", "Follow", "Snow", "Red", "Oblivion", "Lost", "Miracle", "Sound", "Madness", "Sickness",
             "Hollow", "Sun", "Son", "Doctor", "Cat", "Gold", "Silver", "Green", "Dark"]
film_list2 = [ "I", "must", "explain", "to you", "how", "all", "this", "mistaken",
               "idea", "and praising", "pain", "complete", "system", "dog", "light", "car", "movie", "siren"]
genres = ["Thriller", "Horror", "Comedy", "Action", "Fantastic", "Sci-Fi", "Fantasy", "Melodrama", "Drama", "Documentary"]
countries = ["Russia", "USA", "France", "Italy", "German", "Great Britain", "China", "Japan", "South Korea"]
a = 1
films = []

while a <= 30:
    film = {}
    film_id = random.randint(124871, 9348633)
    film['ID'] = film_id
    film['Name'] = random.choice(film_list) + " " + random.choice(film_list2)
    mark = random.uniform(3, 10)
    mark = round(mark, 2)
    film['Mark'] = mark
    film['Year'] = random.randint(1895, 2021)
    film['Genre'] = list(random.sample(genres, random.randint(1, 3)))
    film['Country'] = list(random.sample(countries, random.randint(1, 4)))
    films.append(film)
    a += 1

print(films)

what = input("Enter year or genre or country or mark: ")
save_path = input("Enter save path: ")
file_format = input("Enter file format(txt, csv, json): ")
save_result_movies = input("Enter save path for sorted films: ")

def json_finder(where, what):
    list = where.read()
    where = json.loads(list)
    end_list = []
    for i in where:
        if what.isalpha():
            if what in i["Genre"]:
                end_list.append(i)
            elif what in i["Country"]:
                end_list.append(i)
        if what.isdigit():
            if int(i["Year"]) >= int(what) and int(what) >= 1895:
                end_list.append(i)
            elif float(i["Mark"]) >= float(what):
                end_list.append(i)
    return end_list

def finder_csv(where, what):
    read = csv.DictReader(where)
    print_list = []
    for i in read:
        if what.isalpha():
            if what in i["Genre"]:
                print_list.append(i)
            elif what in i["Country"]:
                print_list.append(i)
        if what.isdigit():
            if int(i["Year"]) >= int(what) and int(what) > 1895:
                print_list.append(i)
            elif float(i["Mark"]) >= float(what):
                print_list.append(i)
    return print_list
def fileWrite(format, file, what):
    if format == "json":
        json.dump(what, file)
    elif format == "csv":
        columns = ["ID", "Name", "Mark", "Year", "Genre", "Country"]
        write = csv.DictWriter(file, fieldnames=columns)
        write.writeheader()
        write.writerows(what)
    elif format == "txt":
        for key in what:
            file.write(f"{key}\n")

try:
    with open(f"{save_path}/movies.{file_format}", 'w', encoding='utf-8') as write_file:
        fileWrite(file_format, write_file, films)
except FileNotFoundError:
    with open(f"movies.{file_format}", 'w', newline='') as write_file:
        fileWrite(file_format, write_file, films)

with open(f"{save_path}/movies.{file_format}", 'r', newline='') as read_file:
    if file_format == "txt":
        for i in read_file.readlines():
            if what in i:
                with open(f"{save_result_movies}/result_movies.txt", 'a+', encoding='utf-8') as text:
                    text.write(i)
    else:
        with open(f"{save_result_movies}/result_movies.{file_format}", 'w', encoding='utf-8') as file:
            if file_format == "json":
                fileWrite(file_format, file, json_finder(read_file, what))
            elif file_format == "csv":
                fileWrite(file_format, file, finder_csv(read_file, what))

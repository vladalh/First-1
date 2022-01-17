import json
import csv

cars_list = []

with open("cars.csv", 'r', encoding='utf-8') as csvfile:
    file = csv.DictReader(csvfile, delimiter=';')
    for line in file:
        cars_list.append(line)

cars_list.sort(key=lambda x: x['Origin'])

user_input = input("Europe, US, Japan?: ")


def countrySort(cars):
    return list(filter(lambda x: x['Origin'] == user_input, cars))

print(countrySort(cars_list))


with open("cars_sort.csv", 'w', encoding='utf-8') as csv_file:
    columns = ["Car", "MPG", "Cylinders", "Displacement", "Horsepower", "Weight", "Acceleration", "Model", "Origin"]
    write = csv.DictWriter(csv_file, fieldnames=columns)
    write.writeheader()
    write.writerows(countrySort(cars_list))

with open("cars.json", 'w', encoding='utf-8') as jsonfile:
    for i in countrySort(cars_list):
        json.dump(i, jsonfile, indent=4)
        print(i)

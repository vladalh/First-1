import json
import csv


def file_reader():
    interval_list = []
    with open("cars.csv", 'r', encoding='utf-8') as file:
        csv_file = csv.DictReader(file, delimiter=';')
        for line in csv_file:
            interval_list.append(line)
            interval_list.sort(key=lambda x: x["Origin"])
    return interval_list


def countrySort(cars):
    return list(filter(lambda x: x['Origin'] == user_input, cars))


def file_write_csv(user_input, car_list):
    with open(f"cars_sort{user_input}.csv", 'w', encoding='utf-8') as file:
        columns = ["Car", "MPG", "Cylinders", "Displacement", "Horsepower", "Weight", "Acceleration", "Model", "Origin"]
        csv_file = csv.DictWriter(file, fieldnames=columns)
        csv_file.writeheader()
        csv_file.writerows(countrySort(car_list))


def file_write_json(user_input, car_list):
    with open(f"cars_sort{user_input}.json", "w", encoding='utf-8') as file:
        for i in countrySort(car_list):
            json_file = json.dump(i, file, indent=4)


user_input = input("Europe, US, Japan?: ")

file_write_csv(user_input, file_reader())
file_write_json(user_input, file_reader())

import random

technical = ["Math", "Physic", "Chemistry", "Biology", "Computer science", "Mechanic", "Astronomy"]
hum_science = ["Psychology", "History", "Literature", " Economics", "Global politics", "Geography"]
students_name = ["Marina", "Pavel", "Andrei", "Alexander", "Svetlana", "Alina", "Nikolai", "Maria", "Artem", "Anastasia"]

def Student(students_name, hum_science, technical):
    student_list = []
    student_list.append(random.choice(students_name))
    student_list.append(random.randint(17848, 239875))
    b = 0

    for i in range(1, 7):
        b += random.randint(1, 11)

    aver_mark = round(b / 6, 2)
    student_list.append(aver_mark)

    random_count = random.randint(1, 6)
    count = 6 - random_count
    subj_set = set(random.sample(technical, random_count))
    subj_set.update(random.sample(hum_science, count))
    student_list.append(subj_set)
    student_list = tuple(student_list)

    return student_list

students_list = [Student(students_name, hum_science, technical) for i in range(11)]

for i in students_list:
    print(i)

technical_set = set(technical)
hum_science_set = set(hum_science)

print()

def Intersec(students_list):
    user_task = input("Technical or Human science?(Enter 1 or 2): ")
    mark = float(input("Enter grade: "))
    grade_list = []
    for k in students_list:
        a = k[3].intersection(technical_set)
        b = k[3].intersection(hum_science_set)
        if user_task == "1":
            if len(a) > len(b):
                print(k)
        elif user_task == "2":
            if len(b) > len(a):
                print(k)

    print()

    for l in students_list:
        if l[2] > mark:
            grade_list.append(l)

    if len(grade_list) > 0:
        print(grade_list)
    else:
        print("Nothing")

Intersec(students_list)


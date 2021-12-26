import random

random_numbers = [random.randint(-20, 50) for i in range(30)]

print(random_numbers)

def sortedByInc(list):
    for i in range(len(list) - 1):
        for j in range(i + 1, len(list)):
            if list[i] > list[j]:
                list[i], list[j] = list[j], list[i]
    return list

def sortedByDec(list):
    for i in range(len(list) - 1):
        for j in range(i + 1, len(list)):
            if list[i] < list[j]:
                list[i], list[j] = list[j], list[i]
    return list

print(sortedByInc(random_numbers), "sorted by increasing")
print(sortedByDec(random_numbers), "sorted by decreasing")

second_random = [random.randint(-20, 50) for l in range(30)]

print(second_random)

def unique(first, second):
    cross = []
    for i in first:
        if i in second:
            cross.append(i)

    print(cross, " :same elements in both lists")

    for i in cross:
        if i in first:
            first.remove(i)

    for i in cross:
        if i in second:
            second.remove(i)

    print(first, " :unique in firs list")
    print(second, " :unique in second list")

unique(random_numbers, second_random)
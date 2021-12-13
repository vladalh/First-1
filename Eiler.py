# Eiler 5

list = [i for i in range(2, 21)]
list1 = [i for i in range(2, 21)]
list3 = []
k = 2

for i in list:
    while k <= 20 ** 0.5:
        for j in list:
            if j % k == 0 and j / k != 1:
                list.remove(j)
        k += 1

for l in list:
    if l in list1:
        list1.remove(l)

for k in list1:
    for c in list:
        if k % c == 0:
            list3.append(c)

list4 = list + list3
rez = 1

for m in list4:
    rez *= m

print(rez)

#Eiler 6

sum = 0
sqaure_sum = 0

for i in range(1, 101):
    sum += i

for j in range(1, 101):
    j *= j
    sqaure_sum += j

square = sum ** 2
difference = square - sqaure_sum

print(difference)

#Eiler 7

number = 120001
numbers = [i for i in range(2, number + 1)]
k = 2
j = 2

for h in numbers:
    while k <= number ** 0.5:
        for j in numbers:
            if j % k == 0 and j / k != 1:
                numbers.remove(j)
            j += 2
        k += 1

print(numbers[10000])

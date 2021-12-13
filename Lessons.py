import random

random_numbers1 = []
for i in range(0, 30):
    random_numbers1.append(random.randint(-20, 50))
print(random_numbers1)

c = 1
b = -1
divisors = 0
div = []
for i in random_numbers1:
    if i > 0:
        while c <= i:
            if i % c == 0:
                divisors += 1
            c += 1
        div.append(divisors)
        divisors = 0
    c = 1
    if i < 0:
        while b >= i:
            if i % b == 0:
                divisors += 1
            b -= 1
        div.append(divisors)
        divisors = 0
    b = -1
print(div)

sortByDiv = [i for _, i in sorted(zip(div, random_numbers1))]
print(sortByDiv, "sorted by number of divisors")

import random

random_numbers1 = [random.randint(-20, 50) for i in range(30)]

def sortedByDivisors(list):
    c = 1
    b = -1
    divisors = 0
    diction = {}
    for i in list:
        if i > 0:
            while c <= i:
                if i % c == 0:
                    divisors += 1
                c += 1
            diction[i] = divisors
            divisors = 0
        c = 1
        if i < 0:
            while b >= i:
                if i % b == 0:
                    divisors += 1
                b -= 1
            diction[i] = divisors
            divisors = 0
        b = -1

    return sorted(diction.items(), key=lambda x: x[1])

print(sortedByDivisors(random_numbers1))
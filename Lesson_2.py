import random

numbers = [random.randint(-100, 100) for i in range(1, 11)]

print(numbers)

def EvOd(list):
    neg = 0
    pos = 0
    even = 0
    odd = 0
    for i in list:
        if i >= 0:
            pos += 1
        else:
            neg += 1
        if i % 2 == 0:
            even += 1
        else:
            odd += 1
    print(f"Evens: {even}; Odds: {odd}; Positive: {pos}; Negative: {neg}")

EvOd(numbers)

positive = []
negative = []

for i in numbers:
    if i > 0:
      positive.append(i)
    else:
        negative.append(i)

min_pos = positive[0]

for i in positive:
    if i < min_pos:
        min_pos = i

min_neg = negative[0]

for i in negative:
    if i > min_neg:
        min_neg = i

print(f"Minimum of positive: {min_pos}")
print(f"Maximum of negative: {min_neg}")
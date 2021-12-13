number = int(input("Enter number: "))
numbers = []
k = 2

for i in range(2, number + 1):
    numbers.append(i)
print(numbers)

for h in numbers:
    while k <= number ** 0.5:
        for j in numbers:
            if j % k == 0 and j / k != 1:
                numbers.remove(j)
        k += 1
print(numbers)

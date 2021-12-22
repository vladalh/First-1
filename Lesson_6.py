number = int(input("Enter number: "))

def eratosphen(number):
    numbers = [i for i in range(2, number + 1)]
    k = 2
    while k <= number ** 0.5:
        for j in numbers:
            if j % k == 0 and j / k != 1:
                numbers.remove(j)
        k += 1
    return numbers

print(eratosphen(number))

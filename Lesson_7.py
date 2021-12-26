from fractions import Fraction

num1 = int(input('enter numerator 1:'))
den1 = int(input('enter denominator 1:'))
num2 = int(input('enter numerator 2:'))
den2 = int(input('enter denominator 2:'))

def frac(num1, den1, num2, den2):
    result = 0
    action = input('enter operator:')
    if action == '+':
        result = Fraction(num1, den1) + Fraction(num2, den2)
    elif action == '-':
        result = Fraction(num1, den1) - Fraction(num2, den2)
    elif action == '/':
        result = Fraction(num1, den1) / Fraction(num2, den2)
    elif action == '*':
        result = Fraction(num1, den1) * Fraction(num2, den2)

    return result

print(frac(num1, den1, num2, den2))
print()


text = "Who's to know if your soul will fade at all The one you sold to fool the world".lower().split()
text = "".join(text)

def unique_symbols(text):
    dict_letters = {}

    for i in text:
        dict_letters[i] = text.count(i)

    print(dict_letters)

    for key, value in dict_letters.items():
        if dict_letters[key] == 1:
            print(f"Unique: {key} - {value}")

unique_symbols(text)

print()

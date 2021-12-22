
def Cashbox():
    summa = 0
    price = []
    running = True
    while running:
        a = input("Enter price or enter 'end' to exit: ")
        try:
            summa += float(a)
            price.append(a)
        except ValueError:
            running = False
    print("Buy list: ", price)
    print("Total price: ", summa)

Cashbox()

first_number = int(input("First number: "))
second_number = int(input("Second number: "))

def ComDiv(num1, num2):
    divider_list1 = []
    divider_list2 = []
    if num1 <= 0:
        print("Wrong number!!!")
    else:
        for i in range(2, num1 + 1):
            if num1 % i == 0:
                divider_list1.append(i)

    if num2 <= 0:
        print("Wrong number!!!")
    else:
        for i in range(2, num2 + 1):
            if num2 % i == 0:
                divider_list2.append(i)

    general = set(divider_list1).intersection(set(divider_list2))
    common = sorted(list(general))

    print(f"Dividers for first number: {divider_list2}")
    print(f"Dividers for second number: {divider_list2}")
    print(f"Common divisors: {common}")
    print(f"Max common divisor {max(common)}")

ComDiv(first_number, second_number)

phrase = input("Enter symbols and number: ")

def CounterSym(symbols):
    result_num = " "
    result_sym = " "
    counter_num = 0
    counter_sym = 0
    for i in range(len(symbols)):
        if symbols[i].isdigit():
            result_num += symbols[i]
            counter_num += 1
        if symbols[i].isalnum() is False:
            result_sym += symbols[i]
            counter_sym += 1

    if counter_num == 0:
        print("Numbers not found")
    if counter_sym == 0:
        print("Symbols not found")
    if counter_num == 0 and counter_sym == 0:
        print("Nothing found")

    print(f"Numbers: {result_num} \nCount: {counter_num}")
    print(f"Symbols: {result_sym} \nCount: {counter_sym}")

CounterSym(phrase)

phrase = input("Enter phrase: ").lower().split()

def WhilePalindrome(phrase):
    phrase1 = "".join(phrase)
    phrase_rev = ""
    a = len(phrase1) - 1
    while a >= 0:
        phrase_rev += phrase1[a]
        a -= 1
    print(phrase_rev)
    if phrase1 == phrase_rev:
        print(f"Palindrom: {phrase1}")
    else:
        print(f"Not palindrome: {phrase1}")

WhilePalindrome(phrase)

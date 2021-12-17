input_str = input("Input string: ").split(" ")
b = "".join(input_str)
c = b.lower()
input_num = input("Input number: ")
pal_a = c[::-1]


if c == pal_a:
    print("Yes, that string is palindrome")
else:
    print("No, is not")

if input_num == input_num[::-1]:
    print("Yes, that number is palindrome")
else:
    print("No, is not palindrome")
text = """Story of the Door Mr. Utterson the lawyer was a man of a rugged countenance 
that was never lighted by a smile; cold, scanty and embarrassed in discourse;
backward in sentiment; lean, long, dusty, dreary and yet somehow lovable."""

print(text)

text_split = text.split()
words = text.split()

count = 0

for sp in range(len(text_split)):
    count = int(sp)
    count += 1

print(f"{count} words in text")

print()

text_only = text.replace(";", "").replace(",", "").replace(".", "")
third_letter = text_only[::3].replace(" ", "").replace("\n", "")
fool = [char for char in third_letter]

print(fool)

for symbol in fool:
    print(ord(symbol), end=' ')

print()

text_without = " "
letters = ["a", "o", "e", "u", "i", "y"]

for letter in letters:
    if letter in text:
        text = text.replace(letter, '')
        text_without = text

print(text_without)
print()

number = int(input("Number: "))
num2 = chr(number)
print(num2)
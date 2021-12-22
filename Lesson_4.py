
phrase = input("Enter phrase: ").lower()
shift = int(input("Enter shift: "))

def Cesar(phrase, shift):
    alphabet = "abcdefghijklmnoprstquwvxyz"
    cesar = " "
    for i in phrase:
        if i in alphabet:
            new = ord(i) + shift
            if new > ord("z"):
                new -= 26
            new2 = chr(new)
            cesar += new2
        else:
            cesar += i
            cesar = "and nothing happens"
    return cesar

print(Cesar(phrase, shift))

print()


text = """Story of the Door Mr. Utterson the lawyer was a man of a rugged countenance
that was never lighted by a smile; cold, scanty and embarrassed in discourse;
backward in sentiment; lean, long, dusty, dreary and yet somehow lovable."""

for i in text:
    if not i.isalnum():
        text = text.replace(i, " ")

text = text.lower().split()

print(text)

find_word = input("What you need to find?: ").lower()

def finder(word, where):
    msg = " "

    if word in where:
        msg = f"found a match! --> {word}"
    else:
        msg = "no match!"
    return msg

print(finder(find_word, text))



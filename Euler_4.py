# Eiler 4

x = 999
y = 999
list = []
v = 1

while x >= 100:
    while y >= 100:
        v = x * y
        h = str(v)
        if h == h[::-1]:
            list.append(v)
            break
        y -= 1
    x -= 1
    y = 999

print(max(list))

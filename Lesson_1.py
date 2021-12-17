import math


triangle_a = float(input("Triangle side A: "))
triangle_b = float(input("Triangle side B: "))
triangle_c = float(input("Triangle side C: "))
square = float(input("Square side: "))
circ = float(input("Circle radius: "))
sphere = float(input("Sphere radius: "))
cube = float(input("Cube side: "))

def main():

    per1 = triangle_a + triangle_b + triangle_c
    semiper = (triangle_a + triangle_b + triangle_c) / 2
    area1 = math.sqrt(semiper * ((semiper - triangle_a) * (semiper - triangle_b) * (semiper - triangle_c)))
    print(f"Triangle perimeter: {per1}, Triangle area: {area1}")

    per2 = square * 4
    area2 = square ** 2
    print(f"Square perimeter: {per2}; Square area: {area2}")

    per3 = 2 * math.pi * circ
    area3 = math.pi * (circ ** 2)
    print(f"Circle perimter: {per3}; Circle area: {area3}")

    area4 = 4 * math.pi * (sphere ** 2)
    capacity1 = 4/3 * math.pi * (sphere ** 3)
    print(f"Sphere area: {area4}; Sphere capacity: {capacity1}")

    per4 = cube * 12
    area5 = cube ** 2 * 6
    capacity2 = cube ** 3
    print(f"Cube perimeter: {per4}; Cube area: {area5}; Cube capacity: {capacity2}")

    total_area = area1 + area2 + area3 + area4 + area5
    print(total_area)

if __name__ == '__main__':
    main()
import math
def myPerimeter(shape):
    #Perimeter of Circle
    if shape == 1:
        radius = float(input("Circle radius: "))
        while True:
            if radius < 0:
                radius = float(input("Enter a positive number: "))
            else:
                break
        perimeter = 2 * math.pi * radius
        print(f'Circle perimeter = {perimeter:.2f}')
        return

    #Perimeter of Rectangle
    if shape == 2:
        length = float(input("Rectangle length: "))
        while True:
            if length < 0:
                length = float(input("Enter a positive number: "))
            else:
                break
            width = float(input("Rectangle width: "))
        while True:
            if width < 0:
                width = float(input("Enter a positive number: "))
            else:
                break
        perimeter = (2 *length) + (2 * width)
        print(f'Rectangle area = {perimeter:.2f}')
        return
    #Perimeter of Square
    elif shape == 3:
        length = float(input("Square length: "))
        while True:
            if length < 0:
                length = float(input("Enter a positive number: "))
            else:
                break
        perimeter = length * 4
        print(f'Square area = {perimeter:.2f}')
        return

    #Perimeter of Triangle
    elif shape == 4:
        side1 = float(input("Triangle side 1: "))
        while True:
            if side1 < 0:
                side1 = float(input("Enter a positive number: "))
            else:
                break
        side2 = float(input("Triangle side 2: "))
        while True:
            if side2 < 0:
                side2 = float(input("Enter a positive number: "))
            else:
                break
        side3 = float(input("Triangle side 3: "))
        while True:
            if side3 < 0:
                side3 = float(input("Enter a positive number: "))
            else:
                break
        perimeter = side1 + side2 + side3
        print(f'Triangle area = {perimeter:.2f}')
        return
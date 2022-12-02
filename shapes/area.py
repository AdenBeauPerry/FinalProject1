import math
def myArea(shape):
    #Area of Circle
    if shape == 1:
        radius = float(input("Circle radius: "))
        while True:
            if radius < 0:
                radius = float(input("Enter a positive number: "))
            else:
                break
        area = math.pi * radius**2
        print(f'Circle area = {area:.2f}')
        return
    #Area of Rectangle
    elif shape == 2:
        length= float(input("Rectangle length: "))
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
        area = length * width
        print(f'Rectangle area = {area:.2f}')
        return

    #Area of Square
    elif shape == 3:
        length = float(input("Square length: "))
        while True:
            if length < 0:
                length = float(input("Enter a positive number: "))
            else:
                break
        area = length**2
        print(f'Square area = {area:.2f}')
        return

    #Area of Triangle
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
        area = (side1 * side2)/2
        print(f'Triangle area = {area:.2f}')
        return
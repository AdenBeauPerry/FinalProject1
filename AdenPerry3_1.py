from shapes import area,perimeter

def selection():
    print('----------------------')
    print('SELECT SHAPE')
    print('----------------------')
    print('1 - Circle')
    print('2 - Rectangle')
    print('3 - Square')
    print('4 - Triangle')

    shape = int(input('Shape number: '))
    while shape < 1 or shape > 4:
        shape = int(input('Shape number (1-4): '))
    return shape

def formula():
    operation = int(input("Computation(Area = 1 or Perimeter = 2: "))
    while operation < 1 or operation > 2:
        operation = int(input('Enter 1 or 2: '))
    return operation

def breakLoop():
    answer = input("Continue (y/n): ").strip()
    while True:
        if answer == 'y' or answer == 'n' or answer == 'Y' or answer == 'N':
            break
        else:
            answer = input("Enter y or n: ").strip()
    return answer

def main():
    while True:
        myShape = selection()

        myFormula = formula()
        if myFormula == 1:
            area.myArea(myShape)
        elif myFormula == 2:
            perimeter.myPerimeter(myShape)

        proceed = breakLoop()
        if proceed == 'n' or proceed == 'N':
            print("PROGRAM DONE")
            break

if __name__ == '__main__':
    main()
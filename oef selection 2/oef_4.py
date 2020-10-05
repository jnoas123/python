number1 = int(input('number 1: '))
number2 = int(input('number 2: '))
number3 = int(input('number 3: '))
if number1 + number2 == number3:
    print('This works')
elif number2 + number3 == number1:
    print('This works')
elif number1 + number3 == number2:
    print('This works')
else:
    print("This won't work")
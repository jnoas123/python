number1 = int(input('First number: '))
number2 = int(input('Second number: '))
if number1 < 0:
    number1 = -number1
if number2 < 0:
    number2 = -number2
if number1 == number2:
    print('The answer for', number1, 'and', number2, '= 0')
elif number1 % 5 == 0 and number2 % 5 == 0:
    if number1 < number2:
        print('The answer for', number1, 'and', number2, '=', number1)
    else:
        print('The answer for', number1, 'and', number2, '=', number2)
elif number1 > number2:
    print('The answer for', number1, 'and', number2, '=', number1)
else:
    print('The answer for', number1, 'and', number2, '=', number2)

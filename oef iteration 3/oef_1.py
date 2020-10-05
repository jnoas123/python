number1 = int(input('Enter a number, stop by enter a zero: '))
number2 = 1
count = 0
while number2 != 0:
    number1 = number1 * number2
    count += 1
    number2 = int(input('Enter a number, stop by enter a zero: '))
print('The product of the', count, 'numbers is', number1)

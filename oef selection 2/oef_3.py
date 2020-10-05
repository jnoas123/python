number1 = int(input('number 1: '))
number2 = int(input('number 2: '))
number3 = int(input('number 3: '))
if number1 <= number2:
    smallest_number = number1
else:
    smallest_number = number2
if smallest_number <= number3:
    print('The smallest number =', smallest_number)
else:
    print('The smallest number =', number3)
#smallest = number1
#if number2 < smallest:
#      smallest = number2
#if number3 < smallest:
#      smallest = number3
# print(smallest)
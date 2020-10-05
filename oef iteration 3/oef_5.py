smallest = largest = int(input('Enter a number: '))
if smallest != 0:
    number = int(input('Enter a number: '))
    while number != 0:
        if number > smallest:
            largest = number
        elif number < smallest:
            smallest = number
        number = int(input('Enter a number: '))
    print('The difference between the largest number', largest, 'and the smallest', smallest, '=', '', end='')
    if smallest < 0 and largest < 0 or smallest > 0:
        difference = largest - smallest
    else:
        difference = -smallest + largest
    print(difference)
else:
    print('No numbers entered')

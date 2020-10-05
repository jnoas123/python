number = int(input('Enter a number: '))
if number > 0:
    last_digit = int(input('What final digit do you want to test with: '))
    last = number % 10
    if last_digit == last:
        print(number, 'ends with', last_digit)
    else:
        print(number, 'does not end with', last_digit)
else:
    print('Negative numbers will not be tested')
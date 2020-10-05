name = input('Enter your name : ')
first_numbers = int(input('Enter the first 9 digits of your national number : '))
last_numbers = int(input('Enter the last 2 digits of your national number : '))
rest = first_numbers % 97
check = 97 - rest
if last_numbers == check:
    first_6 = first_numbers // 1000
    day = first_6 % 100
    month = (first_6 // 100) % 100
    year = first_6 // 100000
    last_3 = first_numbers % 1000
    if last_3 % 2 == 0:
        gender = ', your gender is female'
    else:
        gender = ', your gender is male'
    print('Hello ' + str(name) + gender)
    print('You were born on ' + str(day) + '/' + str(month) + '/' + str(year))
else:
    print('Hello ' + str(name) + ', the national number you gave is not correct')

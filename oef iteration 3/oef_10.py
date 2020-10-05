for x in range(4):
    print('Information for member', x + 1)
    name = input('Name: ')
    age = int(input('Age: '))
    years = int(input('Member for how many years: '))
    if age <= 12:
        price = 20
    elif 12 < age <= 18:
        price = 50
    else:
        price = 95
    if years >= 5:
        price = price * 0.9
    print('Member fee for', name, '=', price)
    print('')

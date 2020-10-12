name = input('Your name (press enter to stop):')
while name != '':
    print()
    print('*' * 5)
    print('U Uppercase')
    print('L Lowercase')
    print('A Alternate')
    choice = input('Make a choice (U-L-A):')
    choice = choice.upper()
#    while choice != 'U' or choice != 'L' or choice != 'A':
#        choice = input('Make a choice (U-L-A):')
 #       choice = choice.upper()
    if choice == 'U':
        print(name.upper())
    if choice == 'L':
        print(name.lower())
    if choice == 'A':
        name = name.lower()
        name[1::2].upper()
        print(name)
    name = input('Your name (press enter to stop):')

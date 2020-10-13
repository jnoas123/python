name = input('Your name (press enter to stop):')
while name != '':
    print()
    print('*' * 5)
    print('U Uppercase')
    print('L Lowercase')
    print('A Alternate')
    choice = input('Make a choice (U-L-A):').upper()
    while choice not in ['U', 'L', 'A']:
        choice = input('Make a choice (U-L-A):').upper()
    if choice == 'U':
        print(name.upper())
    if choice == 'L':
        print(name.lower())
    if choice == 'A':
        name_in_two = len(name) // 2
        over = len(name) % 2
        lower_name = name[1:name_in_two*2:2].lower()
        upper_name = name[0:name_in_two*2:2].upper()
        for i in range(len(upper_name)):
            print(upper_name[i], end="")
            print(lower_name[i], end="")
        if over == 1:
            print(name[-1], end='')
        print()
    name = input('Your name (press enter to stop):')

with open('first_names.txt') as file:
    lines = file.readlines()
    x = 0
    for line in lines[0:]:
        print(line.rstrip().ljust(13), end='')
        x += 1
        if x == 10:
            print('\n')
            x = 0

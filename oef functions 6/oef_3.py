def press_square(n, char):
    for i in range(n):
        print(char * n)


# main
character = input('Which character must be used to form the lines (enter = stop): ')
times = int(input('Number of characters per line = numbers of lines = '))
while character != '':
    press_square(times, character)
    character = input('Which character must be used to form the lines (enter = stop): ')
    if character != '':
        times = int(input('Number of characters per line = numbers of lines = '))

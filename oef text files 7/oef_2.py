with open('first_names.txt') as file:
    lines = file.readlines()
    for line in lines[-1::-1]:
        if line != '\n':
            print(line, end='')
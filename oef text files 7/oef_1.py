with open('first_names.txt') as file:
    line = file.readline()
    counter = 0
    while line:
        if line != '\n':
            print(line.rstrip())
            counter += 1
        line = file.readline()
print('There are', counter, 'first names in the file.')
with open('first_names.txt') as file:
    line = file.readline()
    counter = 0
    counter_z = 0
    while line:
        if line != '\n':
            counter += 1
            for i in line:
                i = i.lower()
                if i == 'z':
                    print(line.rstrip())
                    counter_z += 1
        line = file.readline()
print('There are', counter, 'first names in the file.')
print(counter_z, 'of which contain a letter z')

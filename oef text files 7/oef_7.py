with open('playlist.txt') as file:
    lines = file.readlines()
    for line in lines[-1::-1]:
            record = line.split(';')
            print(record[0].rstrip(), '\t', record[1], '(' + str(record[2].rstrip()) + ')')

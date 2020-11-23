boys = []
girls = []
boy_count = 0
girl_count = 0
with open('contacts.csv') as file:
    line = file.readline()
    while line:
        if line != '\n':
            record = line.split(';')
            if record[3].rstrip() == 'M':
                boy_count += 1
                boys.append('\t' + record[1] + ' ' + record[0])
            if record[3].rstrip() == 'V':
                girl_count += 1
                girls.append('\t' + record[1] + ' ' + record[0])
        line = file.readline()
girls.sort()
boys.sort()
print(girl_count, 'girls:')
print(*girls, sep='\n')
print(boy_count, 'boys:')
print(*boys, sep='\n')

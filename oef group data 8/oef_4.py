print('Overview gifts')
print('Number \t Sponsor')
i = 0
counter = 0
with open('sponsors.txt') as file:
    lines = file.readlines()
    lines.sort()
    while i < len(lines):
        record = lines[i].split('*')
        number = record[0]
        total = 0
        print(record[0] + '\t' + record[1] + ' ' + record[2], end='\t')
        while i < len(lines) and record[0] == number:
            total += int(record[3])
            i += 1
            if i < len(lines):  #zien dat je niet buiten range gaat
                record = lines[i].split('*')
        print(total, end='')
        if int(total) >= 50:
            print('\t **')
            counter += 1
        else:
            print()
print('There are', counter, 'tax certificates to be sent')

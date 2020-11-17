count = 2
with open('books.txt') as file:
    line = file.readline().rstrip()
    print('1.', line, '->', end=' ')
    line = file.readline().rstrip()
    print(line)
    while line:
        if line != '\n':
            line = file.readline().rstrip()
            print(str(count) + '.', line, '->', end=' ')
            line = file.readline().rstrip()
            print(line)
            count += 1
        else:
            line.readline().rstrip()

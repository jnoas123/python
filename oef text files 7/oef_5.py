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

# betere oplossing
# with open('books.txt', encoding='UTF-8') as file:
#   book = file.readline()
#   counter = 1
#   while book:
#       author =file.readline()
#       print(str(counter + ".", book.rstrip(), '->', author.rstrip())
#       counter += 1
#       book = file.readline()
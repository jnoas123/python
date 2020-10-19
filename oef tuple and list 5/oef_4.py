numbers_1 = (1, 2, 3, 4, 5, 6, 7, 8, 9)
numbers = (4, 2, 3, 9, 1, 4, 5)
numbers_2 = (2, 3, 7, 5, 6, 1, 9)
if 4 in numbers:
    i = numbers.index(4)
    new = numbers[i + 1:]
    while 4 in new:
        i = new.index(4)
        new = numbers[i + 1:]
    print(new)
else:
    print('The number 4 does not appear in the tuple')

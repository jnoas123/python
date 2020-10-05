number_a = 0
number_b = 1
number_c = 0
limit = int(input('Up to which limit would you like to print the sequence of Fibonacci? '))
if limit > 1:
    print(str(number_a) + ', ' + str(number_b), end='')
    while number_c < limit:
        number_c = number_b
        number_b += number_a
        number_a = number_c
        number_c = number_a + number_b
        print(', ' + str(number_b), end='')
else:
    print(number_a)
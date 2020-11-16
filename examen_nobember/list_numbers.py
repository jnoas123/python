number_1 = int(input('Enter the first number: '))
number_2 = int(input('Enter the second number: '))
if number_1 == number_2:
    print('Sorry, we can not create a list for you!')
else:
    if number_2 < number_1:
        x = number_2
        number_2 = number_1
        number_1 = x
    list = []
    for i in range(number_1, number_2):
        list.append(i)
    print(list)

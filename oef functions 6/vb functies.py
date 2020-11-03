# no parameter, no return
def task1():
    print(30*'-')
    print(30*'+')

# 1 number-parameter, return number
def task2(age):
    return 65-age

# 1 string-parameter, return string
def task3(name):
    new_name = ''
    for i in range(len(name)):
        if i % 2 == 0:
            new_name += name[i].lower()
        else:
            new_name += name[i].upper()
    return new_name

# 1 list-parameter, return number
def task4(my_list):
    return max(my_list) - min(my_list)

# 2 parameters, return list
def task5(letter, number):
    if number > 0:
        return number * [letter]
    return []

# main
task1()
my_age = task2(25)
print(my_age)
print(task2(36))
print(task3('AnneMarie'))
this_list = [12, 56, 2, 89, 45]
amount = task4(this_list)
print(amount)
character = input('Enter letter: ')
how_many = int(input('Enter number: '))
my_list = task5(character, how_many)
print(my_list)
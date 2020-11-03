import random
def generate_list(n, min, max):
    list = []
    for i in range(n):
        list.append(random.randint(min, max))
    return list


def filter(unfiltered_list):
    filtered_list = []
    for i in unfiltered_list:
        if i not in filtered_list:
            filtered_list.append(i)
    return filtered_list


# main
dice = int(input('How many dice do you want to roll? '))
rolls = generate_list(dice, 1, 6)
print('You threw:', rolls)
unique = filter(rolls)
print('Your unique rolls were:', unique)

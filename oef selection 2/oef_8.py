wine = int(input('How many bottles of wine are there: '))
pizza = int(input('How many pizzas are there: '))
if wine >= 5 and pizza >= 5:
    if wine >= 2 * pizza:
        print('This is a fantastic party')
    elif pizza >= 2 * wine:
        print('This is a fantastic party')
    else:
        print('This is a good party')
else:
    print('This is just a stupid party')
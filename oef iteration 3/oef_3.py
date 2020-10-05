age_son = int(input('How old are you: '))
age_father = int(input('How old is your father: '))
years = 0
if age_son < age_father / 2:
    while age_son != age_father / 2:
        age_son += 1
        age_father += 1
        years += 1
    print('Within', years, 'years your father will have twice your age')
    print('Your father will be', age_father, 'and you will be', age_son)
else:
    print('The situation is no longer possible for your ages')

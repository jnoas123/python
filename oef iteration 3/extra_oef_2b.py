strikers = 0
counting = True
print('Press Enter for each new striker you see.')
print('If you want to pass a group, enter the number of strikers')
print('If you want to stop, type s and press Enter')
action = input()
while counting:
    if action == '':
        strikers += 1
        action = input()
    elif action == 's':
        answer = input('Do you really want to stop y/n? ')
        if answer == 'y':
            counting = False
        else:
            action = input()
    else:
        action = int(action)
        strikers += action
        action = input()
print('Total number of strikers', strikers)

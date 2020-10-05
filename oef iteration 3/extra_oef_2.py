strikers = 0
print('Press Enter for each new striker you see.')
print('If you want to pass a group, enter the number of strikers')
print('If you want to stop, type s and press Enter')
action = input()
while action != 'a':
    if action == '':
        strikers += 1
    elif action == 's':
        answer = input('Do you really want to stop y/n? ')
        if answer == 'y':
            break
    else:
        action = int(action)
        strikers += action
    action = input()
print('Total number of strikers', strikers)

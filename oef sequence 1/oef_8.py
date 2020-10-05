current_hour = int(input('Enter the current hour : '))
wait = int(input('How long do you want to wait'))
wait = wait % 24
tot = wait + current_hour
juist = tot % 24
print('the alarm will sound at ' + str(juist) + 'h')
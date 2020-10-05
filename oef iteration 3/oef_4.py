number = int(input('Enter a positive number: '))
guesses = 1
while number != 15:
    if number > 15:
        print('Lower!')
    if number < 15:
        print('Higher!')
    guesses += 1
    number = int(input('Enter a positive number: '))
print('You have guessed the number 15 in', guesses, 'turns.')

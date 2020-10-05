choice = input('What do you choose: paper, rock or scissors? ')
if choice in ['paper', 'rock', 'scissors']:
    if choice == 'paper':
        print('You chose paper')
        print('I chose rock')
        print('You win :-)')
    elif choice == 'rock':
        print('You chose rock')
        print('I chose rock')
        print("It's a tie :-/")
    elif choice == 'scissors':
        print('You chose scissors')
        print('I chose rock')
        print('I win :-(')
else:
    print('Invalid choice')

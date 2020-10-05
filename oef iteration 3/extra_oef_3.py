import random
pile_1 = random.randint(20, 41)
pile_2 = random.randint(20, 41)
game_running = True
while game_running:
    pile = int(input('From witch pile do you take? '))
    matches = int(input('How many matches (between 3 and 8) do you take? '))
    if pile == 1:
        pile_1 -= matches
    else:
        pile_2 -= matches
    if pile_1 <= 0 or pile_2 <= 0:
        print('I win')
        game_running = False
    else:
        pile = random.randint(0, 1)
        matches = random.randint(3, 8)
        if pile == 0:
            pile_1 -= matches
        else:
            pile_2 -= matches
        if pile_1 <= 0 or pile_2 <= 0:
            print('you win')
            game_running = False

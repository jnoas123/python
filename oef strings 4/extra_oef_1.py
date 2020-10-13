sentence = "keep looking up"
board = "#### ####### ##"
print('You have to guess this quote:', board)
answer = input('Guess a letter or press / if you think you know the quote: ')
while answer != '/':
    if answer in sentence:
        board2 = ''
        position = 0
        for i in sentence:
            if i == answer:
                board2 = board2 + str(answer)
                position += 1
            else:
                board2 = board2 + board[position]
                position += 1
        board = board2
    print('You already have this result:', board)
    answer = input('Guess another letter: ')
answer = input('OK. You think you know, just say it. ')
if answer == "keep looking up":
    print('Yes, you win!')
else:
    print('you lose')

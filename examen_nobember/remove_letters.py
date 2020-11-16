lijst = ['Jonas', 'Jana', 'Leo', 'Henry', 'Michael']
print(lijst)
print()
letter = input('Enter the letter you want to remove. Press Enter if you want to stop: ')
while letter != '':
    lijst_2 = []
    for x in range(5):
        word = ''
        for i in lijst[x]:
            if i != letter:
                word = word + i
        lijst_2.append(word)
    lijst = lijst_2
    print(lijst)
    letter = input('Enter the letter you want to remove. Press Enter if you want to stop: ')
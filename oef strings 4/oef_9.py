word = input('What do you eat fo lunch: ')
count = word.count('sandwhich')
if count >= 2:
    word = word.replace('sandwhich', '')
    print(word)

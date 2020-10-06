word = input('Enter a word: ')
if 'in' in word:
    if word.find('in') == 0 or word.find('in') == 1:
        print("'in' appears in the first or second place")
    else:
        print("'in' appears in the word, but not in the front")
else:
    print("This word does not contain 'in'")

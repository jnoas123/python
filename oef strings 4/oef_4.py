word = input('Enter a word: ')
if word[0:] == word[::-1]:
    print(word, 'is a palindrome.')
else:
    print(word, 'is not a palindrome.')

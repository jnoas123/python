pets = ['cat', 'dog', 'mouse', 'rat', 'squirrel', 'owl', 'rabbit']
print('original list:', '\t', pets)
first = pets[0]
pets.remove(first)
pets.append(first)
print('After sliding:', '\t', pets)

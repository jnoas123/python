colour = input('What is your favorite colour: ')
print(colour[0], colour[2], sep='')
print('This colour consists of', len(colour), 'letters')
print()
for i in colour:
    print(i, '=', ord(i))
print()
x = 0
while x < len(colour):
    print('#' + colour[x] + '#')
    x += 1
    print('**' + colour[x] + '**')
    x += 1

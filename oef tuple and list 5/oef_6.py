text = input('Enter a text: ')
lijst = []
for i in text:
    if i != ' ':
        lijst.append(i)
print(lijst)
print()
print(*lijst)
print()
print(*lijst, sep='\t')

text = input('Enter a text: ')
lijst = []
for i in text:
    if i not in lijst and i != ' ':
        lijst.append(i)
lijst.sort()
print(lijst)
print()
print(*lijst)
print()
print(*lijst, sep='\t')
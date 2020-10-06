text = input('Enter a text: ')
triple = 0
for i in range(len(text)-2):
    if text[i] == text[i+1] and text[i] == text[i+2]:
        triple += 1
print('There is', triple, 'in this text')

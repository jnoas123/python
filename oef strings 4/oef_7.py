text = input('Enter a text: ')
largest = 1
for i in range(len(text)-1):
    block = 1
    while text[i] == text[i+1]:
        block += 1
        i += 1
    if block > largest:
        largest = block
print('The length of the largest block in this text is', largest)
#try not to use while in a for loop
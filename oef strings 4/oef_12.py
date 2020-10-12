string = input('Enter a string:')
for i in range(string.count('*')):
    position = string.find('*')
    remove = string[position-1:position+2]
    string = string.replace(remove, '')
print(string)

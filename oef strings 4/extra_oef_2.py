lower_alfa = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
upper_alfa = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
text = input('Enter the text to be encrypted:')
rotate = input('Enter the number of characters you want ro rotate with: ')
encryptie =''
for x in text:
    if x in lower_alfa:
        index = lower_alfa.index(x)
        new = index + rotate
        if new > 25:
            new = new - 26
    encryptie = encryptie + lower_alfa[new]
    if x in upper_alfa:
        index = upper_alfa.index(x)
        new = index + rotate
        if new > 25:
            new = new - 26
    encryptie = encryptie + upper_alfa[new]
    if x == ' ':
        #ascii tabel not a list!!!

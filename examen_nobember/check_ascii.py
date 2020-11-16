x = 0
for i in range(1, 6):
    print(str(i) + ')', end='')
    code = input()
    first_char = ord(code[0])
    if str(first_char) != code[1:]:
        print(code[0], '<-->', code[1:])
    else:
        x += 1
print(x, 'codes were OK')

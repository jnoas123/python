string = input('Enter a string: ')
len1 = len(string) // 3
lengte_in_3 = len1 * 3
over = len(string) % 3
for i in range(0, lengte_in_3, 3):
    print(string[i+1], string[i+2], string[i], sep='', end='')
if over == 1:
    print(string[-1])
if over == 2:
    print(string[-2:])


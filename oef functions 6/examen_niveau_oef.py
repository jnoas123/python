my_adress = 'kleinhoefstraat 4 geel'
list_1 = []
for i in my_adress[::5]:
    if i != ' ' and i not in list_1:
        list_1.append(i)
print(list_1)
x = 4
list_2 = []
while x != 0:
    print('still', x, 'letters to go:', end='')
    gues = input()
    if gues in list_1 and gues not in list_2:
        list_2.append(gues)
        x = x - 1
print('Yes, you did it!')

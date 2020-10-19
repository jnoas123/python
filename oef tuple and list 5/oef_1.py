dieren = ['cat', 'dog', 'mouse', 'rat', 'squirrel', 'owl', 'rabbit']
print('original list', '\t\t', dieren)
element_1 = dieren[0]
dieren[0] = dieren[-1]
dieren[-1] = element_1
print('After the switch', '\t', dieren)

import random
randomnunber = random.randint(1, 10)
namefile = 'table_'+str(randomnunber)+'.txt'
print('table_', randomnunber, '\n')
output_file = open(namefile, 'w')
for i in range(1, 11):
    solution = i * randomnunber
    output_file.write(str(i) + 'x' + str(randomnunber) + '=' + str(solution) + '\n')
output_file.close()

import random
randomnunber = random.randint(1, 10)
namefile = 'wish'+str(randomnunber)+'.txt'
print('wish', randomnunber, '\n')
with open(namefile) as file:
    line = file.readline().rstrip()
    while line:
        if line != '\n':
            print(line)
        line = file.readline().rstrip()

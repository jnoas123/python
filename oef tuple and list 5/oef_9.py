students = []
distances = []
amount = 0
total = 0
print('Enter your name and the distance to school.')
print('Type stop when you want to close the entry.')
name = input('Your name: ')
while name != 'stop':
    students.append(name)
    distance = float(input('Distance to school: '))
    distances.append(distance)
    total += distance
    amount += 1
    name = input('Your name: ')
if students == []:
    print('no name given')
else:
    print('overview')
    for i in range(len(students)):
        print(students[i], '\t', distances[i])
    farthest = max(distances)
    position = distances.index(farthest)
    print(students[position], 'lives farthest, namely', farthest, 'km')
    print('The average distance is', total/amount)

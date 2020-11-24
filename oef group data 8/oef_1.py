with open('classrooms.txt') as file:
    line = file.readline().rstrip()
    record = line.split(';')
    while line:
        counter = 0
        classroom = record[2]
        print(classroom)
        while line and record[2] == classroom:
            counter += 1
            print('\t', record[1], record[0])
            line = file.readline().rstrip()
            record = line.split(';')
        print('Number of students in classroom', classroom, '=', counter)

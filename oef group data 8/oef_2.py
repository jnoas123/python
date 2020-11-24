with open('courses.csv') as file:
    line = file.readline()  # titel lezen en niets mee doen
    line = file.readline().rstrip()
    record = line.split(';')
    while line:
        z_number = record[0]
        print(record[3] + ';' + record[4] + ';' + record[5], end='')
        while line and record[0] == z_number:
            print(';' + record[1] + ' (' + record[2] + ')')
            line = file.readline().rstrip()
            record = line.split(';')

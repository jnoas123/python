output_file = open('hamlet2.txt', 'w')
with open('hamlet.txt') as file:
    line = file.readline().rstrip()
    while line:
        output_file.write(' '.join(line.split()))
        output_file.write('\n')
        line = file.readline().rstrip()
output_file.close()

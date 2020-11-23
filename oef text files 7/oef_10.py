counter = 1
file = open('oef_4.py')
output_file = open('oef_4_output.txt', 'w')
line = file.readline()
while line:
    output_file.write(str(counter) + ' ' + line)
    line = file.readline()
    counter += 1
file.close()
output_file.close()

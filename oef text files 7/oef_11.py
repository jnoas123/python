output_file = open('oef_4_output.py', 'w')
with open('oef_4_output.txt') as file:
    lines = file.readlines()
    for line in lines:
        output_file.write(line[2:])
        line = file.readline()
output_file.close()

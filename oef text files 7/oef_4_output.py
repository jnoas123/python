with open('irish_song.txt') as file:
    line = file.readline().rstrip()
    shortest = len(line)
    zin = line
    line = file.readline().rstrip()
    while line:
        if line != '\n':
            length = len(line)
        if length < shortest:
            shortest = length
            zin = line
        line = file.readline().rstrip()
print('The shortest line has', shortest, 'characters')
print(zin)

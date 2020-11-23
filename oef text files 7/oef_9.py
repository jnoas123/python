with open('weather_2018 08.csv') as file:
    line = file.readline() # inlezen niets mee doen
    line = file.readline()
    record = line.split(';')
    highest_temp = record[1]
    line = file.readline()
    while line:
        record = line.split(';')
        if record[1] > highest_temp:
            highest_temp = record[1]
        line = file.readline()
print('The highest temperature in this period =', highest_temp, '°C')

print('average temperatures')
with open('weather_2018 10.csv') as file:
    line = file.readline()
    line = file.readline().rstrip()
    record = line.split(';')
    while line:
        counter = 0
        total = 0
        datum = record[0]
        datum_zonder_uur = datum[0:10]
        dzu = datum_zonder_uur
        print(datum_zonder_uur, end=' ')
        while line and dzu == datum_zonder_uur:
            counter += 1
            total += float(record[1])
            line = file.readline().rstrip()
            record = line.split(';')
            datum = record[0]
            dzu = datum[0:10]
        average = total / counter
        print('number of measurments =', counter, '\t average =', average.__round__(2))
print('>'*70)

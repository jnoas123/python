def convert(celsius):
    f = celsius * (9 / 5) + 32
    return f


# main
degrees = float(input('degrees Celsius: '))
fahrenheit = convert(degrees)
print(degrees, 'degrees Celsius =', fahrenheit, 'degrees Fahrenheit')

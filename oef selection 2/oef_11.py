kg = int(input('Your weight in kilograms: '))
length = int(input('Your length in centimeters: '))
bmi = (kg / length ** 2) * 10000
if bmi < 18:
    print(bmi)
    print('underweight')
elif 18 <= bmi < 25:
    print(bmi)
    print('normal weight')
elif 25 <= bmi < 27:
    print(bmi)
    print('slightly overweight')
elif 27 <= bmi < 30:
    print(bmi)
    print('moderate overweight')
elif 30 <= bmi < 40:
    print(bmi)
    print('obese')
elif bmi >= 40:
    print(bmi)
    print('sickly obese')
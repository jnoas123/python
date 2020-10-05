number1 = int(input('First number: '))
number2 = int(input('Second number: '))
if 30 <= number1 <= 40 and 30 <= number2 <= 40:
    print('Both numbers are OK')
elif number1 in [65, 72, 83, 90] and number2 in [65, 72, 83, 90]:
    print('Both numbers are OK')
else:
    print('They are NOT OK')
# use or in place of elif
birthyear = int(input('Enter your year of birth: '))
age = 2020 - birthyear
print('Your age =', age)
if age >= 18:
    print("So you're an adult")
else:
    print("You're not an adult yet")
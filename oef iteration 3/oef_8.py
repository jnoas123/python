last_digit = int(input('What final digit do you want to check the numbers on: '))
x = 0
counter = 0
for x in range(10):
    number = int(input('Enter a number: '))
    if last_digit == number % 10:
        counter += 1
print(counter, 'out of 10 numbers end on', last_digit)

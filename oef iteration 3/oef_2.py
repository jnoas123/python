number = int(input('Enter a number: '))
six_count = 0
zero_count = 0
while number // 10 != 0:
    last_digit = number % 10
    if last_digit == 6:
        six_count += 1
    if last_digit == 0:
        zero_count += 1
    number = number // 10
last_digit = number % 10
if last_digit == 6:
    six_count += 1
if last_digit == 0:
    zero_count += 1
print('the number consists of', zero_count, 'zeros and', six_count, 'sixes')

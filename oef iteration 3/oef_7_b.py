total = number = int(input('Initial limit: '))
end = int(input('Final limit: '))
print('sum of numbers from', number, 'till', end)
if number == end:
    print(number)
while number != end:
    number += 1
    total += number
    print('+', number, '-->', total)

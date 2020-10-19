numbers = [0, 42, 18, 17, 0, 2, 19, 10, 5, 14]
largest_odd = numbers[0]
for i in numbers:
    if i > largest_odd and i % 2 != 0:
        largest_odd = i
for i in range(len(numbers)):
    if numbers[i] == 0:
        numbers.remove(0)
        numbers.insert(i, largest_odd)
print(numbers)

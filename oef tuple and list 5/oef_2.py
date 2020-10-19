numbers = [9, 17, 25, 4, 12, 7]
numbers_2 = [23, 12, 54, 85, 46, 30, 26, 64, 91]
lijst_juist = []
for i in numbers_2:
    if i % 2 == 0:
        lijst_juist.insert(0, i)
    else:
        lijst_juist.append(i)
print(lijst_juist)

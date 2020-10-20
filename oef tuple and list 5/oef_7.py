lijst_1 = [2, 4, 5, 9]
lijst_2 = []
for i in range(((len(lijst_1))*2)-1):
    lijst_2.append(0)
lijst_2.append(lijst_1[-1])
print(lijst_2)

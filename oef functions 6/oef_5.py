def up_low_count(string):
    up = 0
    low = 0
    for i in string:
        if i.islower():
            low += 1
        if i.isupper():
            up += 1
    return [up, low]



# main
text = input('Your string: ')
times = up_low_count(text)
print('Number of capitals:', times[0])
print('Number of capitals:', times[1])
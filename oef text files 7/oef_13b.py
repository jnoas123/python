# remove vowels
def remove_vowels(string):
    newstr = string
    vowels = ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U');
    for i in newstr:
        if i in vowels:
            newstr = newstr.replace(i, "");
    return newstr


# main
output_file = open('hamlet3.txt', 'w')
with open('hamlet2.txt') as file:
    line = file.readline()
    while line:
        new = remove_vowels(line)
        output_file.write(new)
        line = file.readline()
output_file.close()

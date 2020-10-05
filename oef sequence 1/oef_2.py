yes = int(input('Hoeveel mensen hebben ja gestemt: '))
no = int(input('Hoeveel mensen hebben nee gestemt: '))
blank = int(input('Hoeveel mensen hebben niet gestemt: '))
totaal = yes + no + blank
percent_yes = (yes / totaal) * 100
percent_no = (no / totaal) * 100
percent_blank = (blank / totaal) * 100
print('YES: ' + str(percent_yes) + '%')
print('NO: ' + str(percent_no) + '%')
print('BLANK: ' + str(percent_blank) + '%')
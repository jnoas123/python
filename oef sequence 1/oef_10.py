day_consumption = int(input('Power consumption during the day (kilowatt per hour): '))
night_consumption = int(input('Power consumption at night (kilowatt per hour): '))
day_cost = day_consumption * 0.068
night_cost = night_consumption * 0.035
totaal = 83.6 + day_cost + night_cost
vat = totaal * 1.21
print('invoice')
print('*' * 7)
print('Fixed cost: €83.6')
print('Daily consumption: €', day_cost)
print('Night consumption: €', night_cost)
print('Total excluding VAT: €', totaal)
print('Total including VAT: €', vat)

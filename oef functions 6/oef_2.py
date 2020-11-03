def convert(ex, euro):
    dol = ex * euro
    return dol


# main
exchange_rate = float(input('Current dollar rate (€ - > $): '))
amount = float(input('Your amount in Euro: '))
dollar = convert(exchange_rate, amount)
print('€', amount, '= $', dollar)

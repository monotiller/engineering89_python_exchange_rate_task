import json

from app.bureau_de_change import BureauDeChange

rates = open("exchange_rates.json", "r")
rates_data = json.load(rates)

print(BureauDeChange.exchange_base(rates_data))
BureauDeChange.exchange_list(rates_data)

currency1 = str(input("What currency would you like to convert from: "))
amount = int(input("...and how much of that currency do you have: "))
currency2 = str(input("What currency would you like to convert to: "))

BureauDeChange.exchange_convert(rates_data, currency1, amount, currency2)
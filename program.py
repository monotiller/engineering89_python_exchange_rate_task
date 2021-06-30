import json

from app.bureau_de_change import BureauDeChange

currency_base = str(input("What currency would you like as your base: "))

BureauDeChange.exchange_list(currency_base)

amount = int(input("How much would you like to change: "))
currency_change = str(input("What currency would you like to change too: "))
BureauDeChange.exchange_convert(currency_base, amount, currency_change)
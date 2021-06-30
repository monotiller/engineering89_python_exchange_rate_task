import json
import requests
import secrets

class BureauDeChange:
    def __init__(self, currency_base):
        self.currency_rates(currency_base)
        self.currency_base = currency_base

    def exchange_list(currency_base):
        url = "https://v6.exchangerate-api.com/v6/" + secrets.exchange_api() + "/latest/" + currency_base.strip().upper()
        check_response_rates = requests.get(url)

        try:
            check_response_rates.status_code == 200
            response_dict = check_response_rates.json()
            file = open('rates.json', 'w')
            print(f"1 {currency_base} is equivalent to:\n")
            file.write('{\n    "rates": {\n')
            for key in response_dict['conversion_rates'].keys():
                file.write(f'        "{key}": {response_dict["conversion_rates"][key]},\n')
                print(f"{key}: {response_dict['conversion_rates'][key]}")
            file.write('        "null": 0\n    }\n}')
        except:
            print(f"{currency_base} is not available")

    def exchange_convert(currency_base, amount, currency_change):
        file = open('rates.json', 'r')
        json_loader = json.load(file)
        currency_list = json_loader["rates"]
        value1 = currency_list.get(currency_base.strip().upper())
        value2 = currency_list.get(currency_change.strip().upper()) / value1
        rate = value2 / value1
        print(f"{amount} {currency_base.strip().upper()} is worth {value1 * rate * amount:.2f} {currency_change.strip().upper()}.")
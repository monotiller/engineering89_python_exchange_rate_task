class BureauDeChange:
    def exchange_base(rates_data):
        currency_base = rates_data['base']
        print(f"Base currency: {currency_base}")

    def exchange_list(rates_data):
        currency_base = rates_data['base']
        currency_list = rates_data['rates']
        currency_updated = rates_data['date']
        print(f"1 {currency_base} is equivalent to:\n")
        for key, value in currency_list.items():
            print(f"{key}: {value}")
        print(f"\nData last updated: {currency_updated}\n")

    def exchange_convert(rates_data, currency1, amount, currency2):
        currency_list = rates_data['rates']
        value1 = currency_list.get(currency1.strip().upper())
        value2 = currency_list.get(currency2.strip().upper()) / value1
        rate = value2 / value1
        print(f"{amount} {currency1.strip().upper()} is worth {value1 * rate * amount:.2f} {currency2.strip().upper()}.")
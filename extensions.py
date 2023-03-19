import json
import requests
from config import exchenges

class ApiException(Exception):
    pass

class Convertor:
    @staticmethod
    def get_price(base, sym, amount):
        try:
            base_key = exchenges[base.lower()]
        except KeyError:
            return ApiException(f"Валюта {base} не найдена!")
        try:
            sym_key = exchenges[sym.lower()]
        except KeyError:
            return ApiException(f"Валюта {sym} не найдена!")
        if base_key == sym_key:
            raise ApiException(f"Невозможно перевести одинаковые валюты -> {base}!")

        try:
            amount = float(amount.replace(",", "."))
        except ValueError:
            raise ApiException(f"Не удалось обработать количество {amount}!")


        url = f"https://api.apilayer.com/exchangerates_data/latest?symbols={sym_key}&base={base_key}"
        headers = {
            "apikey": "fEOlPZGgsrfXZSnVueWZVtNlpXfyKqOn"
        }
        response = requests.request("GET", url, headers=headers)
        resp = json.loads(response.content)
        new_price = resp['rates'][sym_key] * float(amount)

        return round(new_price, 2)
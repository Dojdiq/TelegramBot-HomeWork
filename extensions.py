import json
import requests
from config import keys


class ExchangeException(Exception):
    pass


class Exchange:
    @staticmethod
    def get_price(quote: str, base: str, amount: str):

        if quote == base:
            raise ExchangeException(f"Can't exchange same currency {base}.")

        try:
            quote_ticker = keys[quote]
        except KeyError:
            raise ExchangeException(f"Failed to process currency {quote}.")

        try:
            base_ticker = keys[base]
        except KeyError:
            raise ExchangeException(f"Failed to process currency {base}.")

        try:
            amount = float(amount)
        except ValueError:
            raise ExchangeException(f"Couldn't process amount {amount}.")

        r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={base_ticker}&tsyms={quote_ticker}')
        total_base = json.loads(r.content)[keys[quote]]

        return total_base

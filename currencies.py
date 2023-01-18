import pandas as pd
from requests import get


class Currencies:
    def __init__(self):
        self.resp = get('http://api.nbp.pl/api/exchangerates/tables/A')
        self.date = self.resp.json()[0]['effectiveDate']
        self.table = pd.DataFrame(self.resp.json()[0]['rates'])

    def convert_to_pln(self, currency_code, amount):
        try:
            result = amount * self.table[self.table['code'] == currency_code]['mid'].values[0]
            curr_name = self.table[self.table['code'] == currency_code]['currency'].values[0]
            return f"{amount} {currency_code} ({curr_name}) to {result} PLN"
        except IndexError as e:
            return e, f"Sprawdź poprawność kodu waluty."
        except TypeError as e:
            return e, "Ilość podajemy za pomocą liczb"
        except:
            return "Wystąpił błąd, sprawdź dane i spróbuj ponownie"

    def rate(self, currency_code):
        try:
            result = self.table[self.table['code'] == currency_code]['mid'].values[0]
            return f"Kurs PLN/{currency_code} na dzień {self.date} to {result}"
        except IndexError as e:
            return e, f"Sprawdź poprawność kodu waluty."
        except TypeError as e:
            return e, "Ilość podajemy za pomocą liczb"
        except:
            return "Wystąpił błąd, sprawdź dane i spróbuj ponownie"

    def __str__(self):
        return str(self.table)


if __name__ == '__main__':
    curr = Currencies()

    print(curr)
    print(curr.convert_to_pln('USD', 20))
    print(curr.rate("USD"))

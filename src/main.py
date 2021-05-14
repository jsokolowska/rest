import requests
from pprint import pprint


def get_quotes(num) -> []:
    print("Getting your Kanye quotes....")
    quotes = []
    while len(quotes) < num:
        quote = requests.get("https://api.kanye.rest").json()["quote"]
        if quote not in quotes:
            quotes.append(quote)
    return quotes


def read_and_validate() -> int:
    num = 0
    while num < 5 or num > 20:
        num = int(input("Please enter number between 5 and 20: "))
    return num


n = read_and_validate()
q = get_quotes(n)
print("Quotes: ")
pprint(q)

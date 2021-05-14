import requests


def get_quotes(num) -> []:
    quotes = []

    while len(quotes) < num:
        quote = requests.get("https://api.kanye.rest").json()["quote"]
        if quote not in quotes:
            quotes.append(quote)
    return quotes


quotes = get_quotes(4)
print(quotes)

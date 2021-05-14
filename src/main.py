import requests
from pprint import pprint
import timeit
import json


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


def get_sentiment(quotes) -> []:
    print("Getting sentiment rating...")
    headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
    sentiments = []
    for quote in quotes:
        response = requests.post("https://sentim-api.herokuapp.com/api/v1/", data=json.dumps({"text": quote}), headers=headers)
        sentiment = response.json()["result"]["polarity"]
        sentiments.append(sentiment)
    return sentiments


n = read_and_validate()
q = get_quotes(n)
print("Quotes: ")
pprint(q)
s = get_sentiment(q)
for i in range(len(s)):
    print(f'{s[i]} :\t {q[i]}')






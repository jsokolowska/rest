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


def present_quotes(quotes):
    for i in range(len(quotes)):
        print(f'{i}. {quotes[i]}')
    print("\n")


def present_sentiment(quotes, sentiments):
    for i in range(len(quotes)):
        print(f'{sentiments[i]}\t\t{quotes[i]}')
    print("\n")


def present_best (quotes, sentiment):
    abs_s = [abs(entry) for entry in sentiment]
    idx = abs_s.index(max(abs_s))
    print("Most polarizing Kanye quote\n", abs_s[idx], ":", quotes[idx])


n = read_and_validate()
q = get_quotes(n)
present_quotes(q)
s = get_sentiment(q)
present_sentiment(q, s)
present_best(q,s)

import requests
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
        try:
            num = int(input("Please enter integer number between 5 and 20: "))
        except ValueError:
            print("Input not valid. Try again.")
    return num


def get_sentiment(quotes) -> []:
    print("Getting sentiment rating...")
    headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
    sentiments = []
    for quote in quotes:
        response = requests.post("https://sentim-api.herokuapp.com/api/v1/", data=json.dumps({"text": quote}),
                                 headers=headers)
        sentiment = response.json()["result"]["polarity"]
        sentiments.append(sentiment)
    return sentiments


def present_quotes(quotes):
    for i in range(len(quotes)):
        print(f'{i+1}. {quotes[i]}')
    print("\n")


def present_sentiment(quotes, sentiments):
    pos = sum(1 for x in sentiments if x > 0)
    neu = sum(1 for x in sentiments if x == 0)
    neg = sum(1 for x in sentiments if x<0)
    print(f"positive: {pos}, negative: {neg}, neutral:{neu}")
    abs_s = [abs(entry) for entry in sentiments]
    idx = abs_s.index(max(abs_s))
    print("Most polarizing Kanye quote\n", sentiments[idx], ":", quotes[idx])


n = read_and_validate()
q = get_quotes(n)
present_quotes(q)
s = get_sentiment(q)
present_sentiment(q, s)

from fastapi import FastAPI
import random

app = FastAPI()

side_hustles = [
    "Solving bounties on Replit for rewards",
    "Creating custom themes to sell on Shopify",
    "Writing technical e-books on Amazon KDP",
    "Creating digital goods for Creative Market",
    "Freelancing opportunities with Upwork",
    "Finding bugs with Bugcrowd",
    "Selling digital products with Gumroad",
    "Coding for projects on Fiverr",
    "Mentoring as a side hustle on CodeMentor",
    "Selling APIs on RapidAPI"
]

money_quotes = [
    "\"Money is a terrible master but an excellent servant.\" – P.T. Barnum",
    "\"Spend your money on the things money can buy. Spend your time on the things money can't buy.\" – Haruki Murakami",
    "\"Time is more valuable than money. You can get more money, but you cannot get more time.\" – Jim Rohn",
    "\"Wealth is not about having a lot of money; it's about having a lot of options.\" – Chris Rock",
    "\"Money grows on the trees of patience.\" – Japanese Proverb",
    "\"Wealth is the ability to fully experience life.\" – Henry David Thoreau",
    "\"Happiness is not in the mere possession of money; it lies in the joy of achievement, in the thrill of creative effort.\" – Franklin D. Roosevelt",
    "\"Wealth consists not in having great possessions, but in having few wants.\" – Epictetus",
    "\"All riches have their origin in mind. Wealth is in ideas – not money.\" – Robert Collier",
    "\"Money can't buy you happiness, but it does bring you a more pleasant form of misery.\" – Spike Milligan"
]

@app.get("/side_hustles")
def get_side_hustles(apiKey:str):
    """Returns a random side-hustles idea"""
    if apiKey != "12345678":
        return {"error":"Invalid API Key"}
    return {"side_hustles": random.choice(side_hustles) }

@app.get("/money_quotes")
def get_money_quotes(apiKey: str):
    """Returns a random money quote"""
    if apiKay != "12345678":
        return {"error":"Invalid API Key"}

    return {"money_quotes": random.choice(money_quotes) }
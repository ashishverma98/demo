from art import *
from game_data import *
import random


def format_data(account):
    """format the account data inot printable format."""
    account_name = account["name"]
    account_descr = account["description"]
    account_country = account["country"]
    return (f"{account_name}, a {account_descr}, from {account_country}") 

print(logo)

account_a = random.choice(data)
account_b = random.choice(data)

if account_a == account_b:
    account_b == random.choice(data)

print(f"compare A: {format_data(account_a)}.")
print(vs)
print(f"compare B: {format_data(account_b)}.")

guess = input("who has more follower? type 'A' or 'B': ").lower()


a_followeer_account = account_a["follower_count"]
b_followeer_account = account_b["follower_count"]
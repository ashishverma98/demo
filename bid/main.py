import os

bids = {}

bidding_finished = False

while not bidding_finished:
    name = input("enter your name: ")
    price = int(input("enter your bid: "))
    bids[name] = price
    should_continue = input("are there any more biders? type 'yes' or 'no'.")
    if should_continue == "no":
        bidding_finished = True
    elif should_continue == "yes":
        os.system('cls')
        
print(bids)

max_bid = 0
winner = " "

for bidder in bids:
    if max_bid<= bids[bidder]:
        max_bid = bids[bidder]
        winner = bidder  ## while looping it will loop through each key/name of the bidder the moment it find the max bid that person will be set as the winner
print(f"the winner is {winner}, with the bidding ammout of {max_bid}")



# from auction-art import logo
# print(logo)

bids = {}


def find_heighest_bid(biding_record):
    heighest_bid = 0
    winner = ""
    for bidder in biding_record:
        bid_amount = biding_record[bidder]
        if bid_amount > heighest_bid:
            heighest_bid = bid_amount
            winner = bidder
    print(f"{winner} is the winner with a bid of ${heighest_bid}")


while True:
    name = input("What is your name?:   ")
    price = int(input("What is your bid?: $"))
    bids[name] = price

    more_bid = input("Are there any other bidders? type yes or no\n").lower()
    if more_bid == "no":
        break
    # else:
        # clear()

find_heighest_bid(bids)

from art import logo
print(logo)
# TODO-1: Ask the user for input
auction_is_live = True
entries = {}
while auction_is_live:
    names = input("What is your name? ")
    bids = input("What's your bid? $")
# TODO-2: Save data into dictionary {name: price}

    entries[names] = bids

    more_names = input("Any other bidders? (yes/no) ").lower()
# TODO-3: Whether if new bids need to be added
    if more_names == "yes":
        print("\n" * 100)
        continue
    else:
        auction_is_live = False


# TODO-4: Compare bids in dictionary
winner = max(entries, key=lambda k: entries[k])
print(f"the winner is {winner} with a bid of ${entries[winner]}")

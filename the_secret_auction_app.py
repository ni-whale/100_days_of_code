import os


logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''

bids_log = []
different_bidder = True


def highest_bid(new_name, new_bid):
    new_dict = {"name": new_name, "bid": new_bid}
    print(f"new dict: {new_dict}")
    bids_log.append(new_dict)
    print(f"bids log: {bids_log}")
    print(f"bid: {bids_log[0]['bid']}")
    top_bid = 0
    for bid in bids_log:
        if int(bid['bid']) > top_bid:
            top_bid = int(bid['bid'])
    print(f"THe highest_bid is {top_bid}")


# print(logo)
print("Welcome to the secret auction program.")

while different_bidder:
    name = input("What is your name?: ")
    bid = input("What is your bid?: ")
    highest_bid(new_name=name, new_bid=bid)
    condition = input("Are there any other bidders? Type 'yes' or 'no': ")
    if condition == 'no':
        different_bidder = False
        print("Bye")
    elif condition == 'yes':
        print("okido")
        different_bidder = True
    # else:
    #     print("Please, try again.")

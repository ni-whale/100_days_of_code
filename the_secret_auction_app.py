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
result = []
test = True
# def highest_bid(new_name, new_bid):
#     new_dict = {"name": new_name, "bid": new_bid}
#     bids_log.append(new_dict)
#     top_bid = 0
#     for value in bids_log:
#         if int(value['bid']) > top_bid:
#             top_bid = int(value['bid'])
#     return top_bid

def highest_bid(new_name, new_bid):
    new_dict = {"name": new_name, "bid": new_bid}
    bids_log.append(new_dict)
    top_bid = [0, '', ]
    for value in bids_log:
        if int(value['bid']) > int(top_bid[0]):
            top_bid[0] = int(value['bid'])
            top_bid[1] = value['name']
    return top_bid


print(logo)
print("Welcome to the secret auction program.")

while different_bidder:
    name = input("What is your name?: ")
    bid = input("What is your bid?: ")
    result = highest_bid(new_name=name, new_bid=bid)
    print(f'result is {result}')
    while test:
        condition = input("Are there any other bidders? Type 'yes' or 'no': ")
        if condition == 'no':
            different_bidder = False
            test = False
            print(f"The highest bid is {result[0]}. Congrats {result[1]} with it!")
            print("Bye")
        elif condition == 'yes':
            print("okido")
            different_bidder = True
            test = False
        else:
            continue




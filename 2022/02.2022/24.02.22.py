import math
import random
# Q04


def two_d_array():
    ships = [["Seabulk Pride", 204184, 390, 50, 2018],
             ["USS Sherman", 61748, 400, 55, 1992],
             ["MSC Carmen", 220518, 390, 60, 1993],
             ["MT Sidsel Knutsen", 72774, 398, 57, 1983],
             ["Salem", 97105, 397, 54, 1991],
             ["MCP Altona", 42452, 393, 53, 2005],
             ["MV Star Osakana", 56210, 396, 55, 1985],
             ["MSC Pamela", 201985, 400, 59, 1982],
             ["MSC Carouge", 140758, 400, 60, 1968],
             ["MV Southern Lily", 178872, 392, 52, 1977],
             ["MSC Sabrina", 147799, 394, 52, 1997],
             ["SS Fredericksburg", 115460, 392, 50, 2007],
             ["MV Sirius Star", 113883, 391, 54, 2012],
             ["MSC Nuria", 201665, 396, 52, 2007],
             ["MS Star Clipper", 43364, 394, 51, 1979],
             ["MSC Monterey", 176953, 397, 53, 1996],
             ["MSC Napoli", 21953, 400, 55, 1979],
             ["Shuttle tanker", 194383, 399, 58, 1967],
             ["MSC Geneva", 183986, 395, 59, 2015],
             ["MSC Rosaria", 150530, 394, 54, 1968],
             ["MSC Cordoba", 63222, 399, 60, 2002],
             ["MV Sea Empress", 199487, 392, 56, 2008],
             ["MSC Leigh", 155215, 400, 60, 1986],
             ["MV Sea Star", 159402, 398, 58, 1992],
             ["Sitakund", 21887, 394, 57, 1972]]

    shipLabels = []   # Put the new labels into this structure

    # ----------------------------------------------
    # Write your code below this line

    smallest = -1
    smallest_name = ''
    largest = 0
    largest_name = ''
    for ship in ships:
        name = ship[0]
        gross_tonnage = ship[1]
        length = ship[2]
        width = ship[3]
        YoM = ship[4]

        max_containers = math.floor(gross_tonnage / 2 / 30)
        useable_area = int(length * width / 2)
        label = f"{name} - Length : {length}m - Area : {useable_area}m^2 - Max containers : {max_containers} - Year : {YoM}"

        shipLabels.append(label)

        if max_containers > largest:
            largest = max_containers
            largest_name = name
        if smallest == -1:
            smallest = max_containers
            smallest_name = name
        elif max_containers < smallest:
            smallest = max_containers
            smallest_name = name

    for label in shipLabels:
        print(label)
    print(f"{smallest_name} could hold the least containers with only {smallest} being the limit")
    print(f"{largest_name} could hold the least containers with {largest} containers being the limit")


def functions():

    def validate(question, type):
        valid = False
        while valid == False:
            user_input = input(question)
            if type == str:
                if user_input.isalnum():
                    valid = True
                    return user_input
            elif type == int:
                if user_input.isnumeric():
                    valid = True
                    return int(user_input)
    class Item:
        """Item in the auction house"""

        def __init__(self, name, number, description, reserve_price):
            """Takes arguments and uses them to declare features about the item"""
            self.name = name
            self.item_number = number
            self.number_of_bids = 0
            self.highest_bid = 0
            self.highest_bidder = 'NO ONE'
            self.description = description
            self.reserve_price = reserve_price
            self.sold = False

        def __str__(self):
            """String representation gives some detail about Item"""
            return f'>> ITEM NUMBER {str(item.item_number).rjust(math.floor(math.log(len(AH.items), 10))+1, "0")} <<>> {self.name} <<'

    class AuctionHouse:
        """Auction house with items, users and various functions related to both"""

        def __init__(self):
            """Declares empty list and dictionary for items and users"""
            self.items = []
            self.users = {}

        def create_user(self, username):
            """Takes argument for username and create a user with an user ID and the username"""
            user_id = len(self.users)
            self.users[user_id] = username

        def list_users(self):
            """Output list of users with their user ID and username"""
            print()
            for user_id in self.users.keys():
                print(f'>> USER ID {str(user_id).rjust(math.floor(math.log(len(AH.users), 10))+1, "0")} <<>> {self.users[user_id]} <<')
            print()
        def create_item(self, Item):
            """Takes Item object passed as argument and adds it to list of items"""
            self.items.append(Item)

        def new_bid(self):
            """Creates a new bid after validating correct data
            - a valid user ID
            - a valid item number
            - a bid that is greater than the existing greatest bid
            """


            user_id = validate('\nPLEASE INPUT YOUR USER ID\n', int)
            if user_id not in self.users.keys():
                print('\nERROR! YOUR USER ID IS NOT VALID\n')
            else:
                item_number = validate('\nPLEASE INPUT THE ITEM NUMBER OF THE ITEM YOU WANT TO BID ON\n', int)
                if item_number not in [item.item_number for item in self.items]:
                    print('\nERROR! THE ITEM IS NOT VALID\n')
                else:
                    bid = validate('\nPLEASE INPUT YOUR BID\n', int)
                    if bid <= [item.highest_bid for item in self.items if item.item_number == item_number][0]:
                        print('\nERROR! YOUR BID IS NOT ENOUGH\n')

                    else:
                        for item in self.items:
                            if item.item_number == item_number:
                                item.highest_bid = bid
                                item.number_of_bids += 1
                                if bid >= item.reserve_price:
                                    item.sold = True

    AH = AuctionHouse()
    
    #list of 10 test items created
    test_items = [
        ['Putin\'s hat', 1, 'a', 2000000],
        ['Biden\'s chair', 2, 'b', 1500000],
        ['2005 US Dollar Bill',  3, 'c', 10000],
        ['Remains of shell', 4,  'd', 1000],
        ['Makeup kit', 5,  'e', 500],
        ['Apple II', 6, 'f', 10000],
        ['Big Whopper', 7, 'g', 50000],
        ['King Arthur\'s sword', 8, 'h', 10000000000],
        ['1871 Gold Reserve 1 Carat', 9, 'i', '15000'],
        ['1 Bitcoin', 10, 'j', 100000000]
    ]

    for test_item in test_items:
        AH.create_item(Item(*test_item))

    while True:
        action = input(
            'PLEASE SELECT ACTION FROM <BID>, <VIEW USERS>, <VIEW ITEMS>, <NEW USER>, <NEW ITEM>, <END AUCTION>, <QUIT> : ')
        
        if action == 'QUIT' or action == '<QUIT>' or len(action) > 20:
            print('\nQUITTING\n')
            break

        elif action == 'BID' or action == '<BID>':
            AH.new_bid()

        elif action == 'VIEW USERS' or action == '<VIEW USERS>':
            AH.list_users()

        elif action == 'VIEW ITEMS' or action == '<VIEW ITEMS>':
            print()
            for item in AH.items:
                #outputs string representation of item with some detail about each item
                print(str(item))
            print()

        elif action == 'NEW USER' or action == '<NEW USER>':
            username = input('\nPLEASE INPUT USERNAME\n')
            AH.create_user(username)
            print('\nNEW USER CREATED!\n')

        elif action == 'NEW ITEM' or action == '<NEW ITEM>':
            AH.create_item(Item(str(random.randint(1, 100)), random.randint(1, 100), str(
                random.randint(1, 100)), random.randint(1, 100)))
            print('\nNEW ITEM CREATED!\n')

        
        elif action == 'END AUCTION' or action == '<END AUCTION>':
            # SCAN ITEMS FOR BID
            sold = []
            bid_not_sold = []
            no_bid = []
            highest_number_bids = 0
            highest_bid = 0
            total_fee = 0
            for item in AH.items:
                if item.sold == True:
                    sold.append(item)
                elif item.number_of_bids > 0:
                    bid_not_sold.append(item)
                else:
                    no_bid.append(item)

                if item.number_of_bids > highest_number_bids:
                    highest_number_bids = item.number_of_bids
                
                if item.highest_bid > highest_bid:
                    highest_bid = item.highest_bid
            
            if highest_bid != 0:
                bid_max_digits = len(str(format(highest_bid, ".2f")))
            else:
                bid_max_digits = 3
            
            if len(AH.items) != 0:
                item_number_max_digits = math.floor(math.log(len(AH.items), 10))+1
            else:
                item_number_max_digits = 0
            
            if highest_number_bids != 0:
                number_of_bids_max_digits = math.floor(math.log(highest_number_bids, 10))+1
            else:
                number_of_bids_max_digits = 1
            
            bid_max_digits = len(str(format(highest_bid, ".2f")))
            print('\n')
            if len(sold) != 0:
                print(f'ITEM{int(len(sold) > 1) * "S"} SOLD')
                for item in sold:
                    print(
                        f'>>     SOLD <<>> ITEM NUMBER {str(item.item_number).rjust(item_number_max_digits, "0")} <<>> {str(item.number_of_bids).rjust(number_of_bids_max_digits)} BID{int(item.number_of_bids != 1) * "s" + int(item.number_of_bids == 1) * " "} <<>> FINAL BID ${str(format(item.highest_bid, ".2f")).rjust(bid_max_digits)} <<')
                    total_fee = total_fee + item.highest_bid * 0.1
                print()


            if len(bid_not_sold) != 0:
                print(f'ITEM{int(len(bid_not_sold) > 1) * "S"} THAT DIDN\'T MEET THE RESERVED PRICE')
                for item in bid_not_sold:
                    print(
                        f'>> NOT SOLD <<>> ITEM NUMBER {str(item.item_number).rjust(item_number_max_digits, "0")} <<>> {str(item.number_of_bids).rjust(number_of_bids_max_digits)} BID{int(item.number_of_bids != 1) * "s" + int(item.number_of_bids == 1) * " "} <<>> FINAL BID ${str(format(item.highest_bid, ".2f")).rjust(bid_max_digits)} <<')
                print()

            if len(no_bid) != 0:
                print(f'ITEM{int(len(no_bid) > 1) * "S"} WITH NO BIDS')
                for item in no_bid:
                    print(
                        f'>> NOT SOLD <<>> ITEM NUMBER {str(item.item_number).rjust(item_number_max_digits, "0")} <<>> {str(0).rjust(number_of_bids_max_digits)} BIDS <<>> FINAL BID ${str(0.00).rjust(bid_max_digits)} <<')
                print()
            print(f'THERE ARE {len(sold)} ITEMS SOLD')
            print(
                f'THERE ARE {len(bid_not_sold)} ITEMS THAT DID NOT MEET THE RESERVE PRICE')
            print(f'THERE ARE {len(no_bid)} ITEMS THAT HAVE 0 BIDS\n')

            print('DING! DING! DING! THE AUCTION HAS ENDED')
            print(f'TOTAL FEE EARNED IS $ {total_fee}')
            break
        else:
            print('\nERROR! COMMAND NOT FOUND\n')

functions()

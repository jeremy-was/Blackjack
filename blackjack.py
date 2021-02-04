import random
suits = ('Hearts','Diamonds','Clubs','Spades')
ranks = ('Two','Three','Four','Five','Six','Seven','Eight','Nine','Ten','Jack','Queen','King','Ace')
values = {'Two':2,'Three':3,'Four':4,'Five':5,'Six':6,'Seven':7,'Eight':8,'Nine':9,'Ten':10,'Jack':10,'Queen':10,'King':10,'Ace':11}
player_funds = 1000

class Card:

    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        return self.rank + " of " + self.suit

class Deck:

    def __init__(self):

        self.all_cards = []

        for suit in suits:
            for rank in ranks:
                created_card = Card(suit,rank)

                self.all_cards.append(created_card)

    def shuffle(self):
        random.shuffle(self.all_cards)

    def deal_one(self):
        return self.all_cards.pop()

    def deal_another(self):
        return self.all_cards.pop()

    def __str__(self):
        return self.all_cards

class Dealer:

    dealer_hand = []

    def __init__(self):

        self.hand = hand

    def hand_value(self):
        self.h_value = h_value

    def __str__(self):
        return "Dealer currently has " + self.hand + ", with a value of " + self.hand_value

class Player:

    def __init__(self):

        self.name = input('Please enter your name:  ')
        self.allcards = []
        self.allcards_value = []

    def bet(self):
        self.bet_amount = bet_amount

    # def funds(self):
    #    self.funds = funds

    def __str__(self):
        return self.name #+ " has " + "$" + self.player_funds + " remaining."

# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@ FUNCTIONS @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

def bet_func():
    global player_funds

    while True:
        try:
            if player_funds <=0:
                print('No money left, playing just for fun now')
                break
            if player_funds > 0:
                Player.bet = int(input(f"You have ${player_funds} remining, how much you betting?:   "))

            if Player.bet > player_funds:
                Player.bet = int(input(f"Not enough money, you have ${player_funds} remining, how much you betting?:   "))
        except:
            print('please enter a number')
            continue
        else:
            print(f'${Player.bet} bet placed successfully')
            break
#         finally:
#             if Player.bet <= player_funds:
#                 pfunds_func()

# def pfunds_func():
#     global player_funds
#     player_funds -= Player.bet
#     print(f"you have ${player_funds} remaining")

def ace_check():
    if player_card_list[-1].value == 11:
        player_card_list[-1].value = int(input("Please choose 11 or 1 for your Ace:  "))
        player_value.append(player_card_list[-1].value)
        player_card_names.append(player_card_list[-1])
    else:
        player_value.append(player_card_list[-1].value)
        player_card_names.append(player_card_list[-1])

def two_ace_check():
    if player_card_list[0].value == 11 and player_card_list[1].value == 11:
        player_card_list[0].value = 1
        player_value.append(player_card_list[0].value)
        player_value.append(player_card_list[1].value)
        player_card_names.append(player_card_list[0])
        player_card_names.append(player_card_list[1])
    else:
        player_value.append(player_card_list[0].value)
        player_value.append(player_card_list[1].value)
        player_card_names.append(player_card_list[0])
        player_card_names.append(player_card_list[1])

def player_addvalue_func():
    global player_value
    global player_card_names
    global player_card_list
    # for x in player_card_list:
    #     print(x.value)
    
    # if len(player_value) == 2: (looks like this was an error)
    if len(player_card_list) == 2:
        two_ace_check()
    else:
        ace_check()
        

def dealer_addvalue_func():
    global dealer_value
    global dealer_card_names
    global dealer_card_list
    # for x in dealer_card_list:
    #     print(x.value)
   
    # if len(dealer_value) == 2:
    if len(dealer_card_list) == 2:
        dealer_value.append(dealer_card_list[0].value)
        dealer_value.append(dealer_card_list[1].value)
        dealer_card_names.append(dealer_card_list[0])
        dealer_card_names.append(dealer_card_list[1])
    else:
        dealer_value.append(dealer_card_list[-1].value)
        dealer_card_names.append(dealer_card_list[-1])

def gameon_player_func():
    global player_value

    gameon = True
    while gameon:

        print(f"\n{currentplayer}'s cards:")
        for c in player_card_names: print(c)
        print(f"\n{currentplayer}'s card values:")
        print(player_value)
        print(f"\n{currentplayer}'s hand value:")
        print(sum(player_value))
        print("* * * * * * *")

        if sum(player_value) >21:
            print("\n* * * * * * * * * * * * * * * * * * * * *")
            print(f"{currentplayer} is Bust!")
            print("* * * * * * * * * * * * * * * * * * * * *\n")
            gameon = False
            gameon_dealer_finish_func()

        elif sum(player_value) <= 19:
            while True:
                player_choice = (input("\nHit or stay?  "))          
                if player_choice == ("hit") or player_choice == ("Hit") or player_choice == ("H") or player_choice == ("h"):
                    player_one_card_deal()
                    player_addvalue_func()
                    break
                elif player_choice == ("stay") or player_choice == ("Stay") or player_choice == ("S") or player_choice == ("s"):
                    gameon = False
                    print(f'\nGood luck {currentplayer}. Staying! Total value:')
                    print(sum(player_value))
                    print("* * * * * * * * * * * * * * * * * * * * *\n")
                    gameon_dealer_finish_func()
                    break
                else:
                    print("Bad input, please try again")
                        
        elif sum(player_value) == 20:
            print("\n* * * * * * * * * * * * * * * * * * * * * * * * * *")
            print(f"{currentplayer} is on 20. Can't take another card")
            print("* * * * * * * * * * * * * * * * * * * * * * * * * * *\n")
            gameon = False
            gameon_dealer_finish_func()
        else:
            print("\n* * * * * * * * * * * * * * * * * * * * *")
            print(f"{currentplayer} has Black Jack!!")
            print("* * * * * * * * * * * * * * * * * * * * *\n")
            gameon = False
            gameon_dealer_finish_func()

def gameon_dealer_func():
    global dealer_value

    print("\nDealer cards:")
    for c in dealer_card_names: print(c)
    print("\nDealer card values:")
    print(dealer_value)
    print('\nDealer total value:')
    print(sum(dealer_value))
    print("* * * * * * *")

# Functions for (two cards each) - to the dealer and to the player
def dealer_two_card_deal():
    dealer_card_list.append(whole_deck.deal_one())
    dealer_card_list.append(whole_deck.deal_another())

def player_two_card_deal():
    player_card_list.append(whole_deck.deal_one())
    player_card_list.append(whole_deck.deal_another())

def gameon_dealer_finish_func():
    global dealer_value

    gameon = True
    while gameon:

        print("\nDealer cards:")
        for c in dealer_card_names: print(c)
        print("\nDealer card values:")
        print(dealer_value)
        print('\nDealer total value:')
        print(sum(dealer_value))
        print("* * * * * * *\n")

        if sum(dealer_value) >21:
            print("\n* * * * * * * * * * * * * * * * * * * * *")
            print("Dealer is Bust!")
            print("* * * * * * * * * * * * * * * * * * * * *\n")
            gameon = False
            end_of_game()
            break

        elif sum(dealer_value) <= 18:
            dealer_one_card_deal()
            dealer_addvalue_func()
                        
        elif sum(dealer_value) == 19 or sum(dealer_value) ==20:
            print("\n* * * * * * * * * * * * * * * * * * * * *")
            print("Dealer on 19+. Staying!")
            print("* * * * * * * * * * * * * * * * * * * * *\n")
            gameon = False
            end_of_game()
            break

        else:
            print("\n* * * * * * * * * * * * * * * * * * * * *")
            print("Dealer has Black Jack!")
            print("* * * * * * * * * * * * * * * * * * * * *\n")
            gameon = False
            end_of_game()
            break

def end_of_game():
    global player_funds
    if sum(dealer_value) == sum(player_value) and sum(dealer_value) <= 21 and sum(player_value) <= 21:
        print(f"The scores are: \n{currentplayer}: {sum(player_value)} \nDealer: {sum(dealer_value)}")
        print(f"\nIt's a draw! {currentplayer} still has ${player_funds} remaining\n")
        play_again_check()
    if sum(dealer_value) == sum(player_value) and sum(dealer_value) > 21 and sum(player_value) > 21:
        print(f"The scores are: \n{currentplayer}: {sum(player_value)} \nDealer: {sum(dealer_value)}")
        player_funds -= Player.bet
        print(f"\nYou both went bust! with the same score {currentplayer} lost ${Player.bet}! and now has ${player_funds} remaining\n")
        play_again_check()
    if sum(dealer_value) != sum(player_value) and sum(dealer_value) > 21 and sum(player_value) > 21:
        print(f"The scores are: \n{currentplayer}: {sum(player_value)} \nDealer: {sum(dealer_value)}")
        player_funds -= Player.bet
        print(f"\nYou both went bust! {currentplayer} lost ${Player.bet}! and now has ${player_funds} remaining\n")
        play_again_check()
    if sum(dealer_value) > sum(player_value) and sum(dealer_value) <= 21:
        print(f"The scores are: \n{currentplayer}: {sum(player_value)} \nDealer: {sum(dealer_value)}")
        player_funds -= Player.bet
        print(f"Dealer won! {currentplayer} lost ${Player.bet}! and now has ${player_funds} remaining")
        play_again_check()
    if sum(dealer_value) < sum(player_value) and sum(player_value) <= 21:
        print(f"The scores are: \n{currentplayer}: {sum(player_value)} \nDealer: {sum(dealer_value)}")
        player_funds += Player.bet
        print(f"{currentplayer} is the winner! {currentplayer} won ${Player.bet}! and now has ${player_funds} remaining")
        play_again_check()
    if sum(dealer_value) <=21 and sum(player_value) >21: 
        print(f"The scores are: \n{currentplayer}: {sum(player_value)} \nDealer: {sum(dealer_value)}")
        player_funds -= Player.bet
        print(f"\nDealer won! and {currentplayer} went bust. {currentplayer} lost ${Player.bet}! and now has ${player_funds} remaining\n")
        play_again_check()
    if sum(player_value) <=21 and sum(dealer_value) >21: 
        print(f"The scores are: \n{currentplayer}: {sum(player_value)} \nDealer: {sum(dealer_value)}")
        player_funds += Player.bet
        print(f"\n{currentplayer} is the winner and dealer went bust! {currentplayer} won ${Player.bet}! and now has ${player_funds} remaining\n")
        play_again_check()
        pass

# @@@@@@@@@@@@@@@@@@@@@@
#
# ADD TO THIS FUNCTION 
# SO GAME STATS CAN BE ADDED TO A FILE
# AND PLAYER FUNDS CAN BE UPDATED READY FOR NEXT GAME
#
# @@@@@@@@@@@@@@@@@@@@@@

# All Subsequent deals of ONE card to the DEALER
def dealer_one_card_deal():
    dealer_card_list.append(whole_deck.deal_one())

# All Subsequent deals of ONE card to the PLAYER
def player_one_card_deal():
    player_card_list.append(whole_deck.deal_one())

def play_again_check():
    while True:
        playagain = input("\nPlay again? y/n   \n")
        if playagain == ("y") or playagain == ("Y"):
            repeat_game()
            break
        elif playagain == ("n") or playagain == ("N"):
            print("\nThanks for playing!\n")
            break
        else:
            print("\nbad input, please try again\n")

def repeat_game():
    player_card_list.clear()
    player_card_names.clear()
    player_value.clear()
    dealer_card_list.clear()
    dealer_card_names.clear()
    dealer_value.clear()
    whole_deck = Deck()
    random.shuffle(whole_deck.all_cards)
    for j in whole_deck.all_cards: original_shuffle.append(j)

    #currentplayer = Player()
    print(f"\nHello again {currentplayer}\n")

    bet_func()

    # Execute the First deal (two cards each)
    dealer_two_card_deal()
    player_two_card_deal()

    # DEALER GAME PLAY & CALCULATIONS
    # add the dealt card(s) value to a list for value calculation
    dealer_addvalue_func()
    # Run the calc for 21 etc
    gameon_dealer_func()

    # PLAYER GAME PLAY & CALCULATIONS
    # add the dealt card(s) value to a list for value calculation
    player_addvalue_func()
    # Run the calc for 21 etc
    gameon_player_func()


player_value = []
dealer_value = []

player_card_names = []
dealer_card_names = []

player_card_list = []
dealer_card_list = []
original_shuffle = []

# 
# Uncomment these if/when I start to pull card list from Classes above
# 

# player_card_list = Player.player_hand
# dealer_card_list = Dealer.dealer_hand



# @@@@@@@@@@@@@@@@@@@@@@@ Game play script @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

whole_deck = Deck()
random.shuffle(whole_deck.all_cards)
for j in whole_deck.all_cards: original_shuffle.append(j)

currentplayer = Player()
print(f"Welcome {currentplayer}\n")

bet_func()

# Execute the First deal (two cards each)
dealer_two_card_deal()
player_two_card_deal()

# DEALER GAME PLAY & CALCULATIONS
# add the dealt card(s) value to a list for value calculation
dealer_addvalue_func()
# Run the calc for 21 etc
gameon_dealer_func()

# PLAYER GAME PLAY & CALCULATIONS
# add the dealt card(s) value to a list for value calculation
player_addvalue_func()
# Run the calc for 21 etc
gameon_player_func()

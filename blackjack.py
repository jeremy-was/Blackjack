import random
import datetime
import os
import smtplib
from email.mime.text import MIMEText
# from datetime import datetime
# from datetime import date
suits = ('Hearts','Diamonds','Clubs','Spades')
ranks = ('Two','Three','Four','Five','Six','Seven','Eight','Nine','Ten','Jack','Queen','King','Ace')
values = {'Two':2,'Three':3,'Four':4,'Five':5,'Six':6,'Seven':7,'Eight':8,'Nine':9,'Ten':10,'Jack':10,'Queen':10,'King':10,'Ace':11}
player_funds = 1000
game_count = 1
player_total = 0
dealer_total = 0
draw = 0

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

    hand = []
    hand_value = []
    card_names = []

    def __init__(self):

        self.hand = []
        self.hand_value = []
        self.card_names = []

    def __str__(self):
        return "Dealer currently has " + self.hand + ", with a value of " + self.hand_value

class Player:

    hand = []
    hand_value = []
    card_names = []

    def __init__(self):

        self.name = input('Please enter your name:  ')
        self.hand = []
        self.hand_value = []
        self.card_names = []
        self.bet = 0

    def __str__(self):
        return self.name #+ " has " + "$" + self.player_funds + " remaining."

def bet_func():
    global player_funds

    while True:
        try:
            if player_funds <=0:
                print('No money left, playing just for fun now')
                Player.bet = 0
                break
            if player_funds > 0:
                Player.bet = int(input(f"You have ${player_funds:,}, how much you betting?:   "))

            if Player.bet > player_funds:
                Player.bet = int(input(f"Not enough money, you have ${player_funds:,} remining, how much you betting?:   "))
        except:
            print('Please enter a number')
            continue
        else:
            print(f'${Player.bet} bet placed successfully')
            break

def ace_check():
    if Player.hand[-1].value == 11:
        Player.hand[-1].value = int(input("Please choose 11 or 1 for your Ace:  "))
        Player.hand_value.append(Player.hand[-1].value)
        Player.card_names.append(Player.hand[-1])
    else:
        Player.hand_value.append(Player.hand[-1].value)
        Player.card_names.append(Player.hand[-1])

def two_ace_check():
    if Player.hand[0].value == 11 and Player.hand[1].value == 11:
        Player.hand[0].value = 1
        Player.hand_value.append(Player.hand[0].value)
        Player.hand_value.append(Player.hand[1].value)
        Player.card_names.append(Player.hand[0])
        Player.card_names.append(Player.hand[1])
    else:
        Player.hand_value.append(Player.hand[0].value)
        Player.hand_value.append(Player.hand[1].value)
        Player.card_names.append(Player.hand[0])
        Player.card_names.append(Player.hand[1])

def player_addvalue_func():
    if len(Player.hand) == 2:
        two_ace_check()
    else:
        ace_check()
        

def dealer_addvalue_func():
    if len(Dealer.hand) == 2:
        Dealer.hand_value.append(Dealer.hand[0].value)
        Dealer.hand_value.append(Dealer.hand[1].value)
        Dealer.card_names.append(Dealer.hand[0])
        Dealer.card_names.append(Dealer.hand[1])
    else:
        Dealer.hand_value.append(Dealer.hand[-1].value)
        Dealer.card_names.append(Dealer.hand[-1])

def gameon_player_func():

    gameon = True
    while gameon:

        print(f"\n{currentplayer}'s cards:")
        for c in Player.card_names: print(c)
        print(f"\n{currentplayer}'s card values:")
        print(Player.hand_value)
        print(f"\n{currentplayer}'s hand value:")
        print(sum(Player.hand_value))
        print("* * * * * * *")

        if sum(Player.hand_value) >21:
            print("\n* * * * * * * * * * * * * * * * * * * * *")
            print(f"{currentplayer} is Bust!")
            print("* * * * * * * * * * * * * * * * * * * * *\n")
            gameon = False
            gameon_dealer_finish_func()

        elif sum(Player.hand_value) <= 19:
            while True:
                player_choice = (input("\nHit or stay? h/s "))          
                if player_choice == ("hit") or player_choice == ("Hit") or player_choice == ("H") or player_choice == ("h"):
                    player_one_card_deal()
                    player_addvalue_func()
                    break
                elif player_choice == ("stay") or player_choice == ("Stay") or player_choice == ("S") or player_choice == ("s"):
                    gameon = False
                    print(f'\nGood luck {currentplayer}. Staying! Total value:')
                    print(sum(Player.hand_value))
                    print("* * * * * * * * * * * * * * * * * * * * *\n")
                    gameon_dealer_finish_func()
                    break
                else:
                    print("Bad input, please try again")
                        
        elif sum(Player.hand_value) == 20:
            print("\n* * * * * * * * * * * * * * * * * * * * * * * * * *")
            print(f"{currentplayer} is on 20. Staying")
            print("* * * * * * * * * * * * * * * * * * * * * * * * * * *\n")
            gameon = False
            gameon_dealer_finish_func()
        elif Player.hand_value[0] == 11 and Player.hand_value[1] == 10 or Player.hand_value[1] == 11 and Player.hand_value[0] == 10:
            print("\n* * * * * * * * * * * * * * * * * * * * * * * * * *")
            print(f"{currentplayer} has Black Jack!")
            print("* * * * * * * * * * * * * * * * * * * * * * * * * * *\n")
            gameon = False
            gameon_dealer_finish_func()
        else:
            print("\n* * * * * * * * * * * * * * * * * * * * *")
            print(f"{currentplayer} has 21")
            print("* * * * * * * * * * * * * * * * * * * * *\n")
            gameon = False
            gameon_dealer_finish_func()

def gameon_dealer_func():

    print("\nDealer's cards:")
    for c in Dealer.card_names: print(c)
    print("\nDealer's card values:")
    print(Dealer.hand_value)
    print("\nDealer's total value:")
    print(sum(Dealer.hand_value))
    print("* * * * * * *")

def gameon_dealer_finish_func():

    gameon = True
    while gameon:

        print("\nDealer's cards:")
        for c in Dealer.card_names: print(c)
        print("\nDealer's card values:")
        print(Dealer.hand_value)
        print("\nDealer's hand value:")
        print(sum(Dealer.hand_value))
        print("* * * * * * *\n")

        if sum(Dealer.hand_value) >21:
            print("\n* * * * * * * * * * * * * * * * * * * * *")
            print("Dealer is Bust!")
            print("* * * * * * * * * * * * * * * * * * * * *\n")
            gameon = False
            end_of_game()
            break

        elif sum(Dealer.hand_value) <= 18:
            dealer_one_card_deal()
            dealer_addvalue_func()
                        
        elif sum(Dealer.hand_value) == 19 or sum(Dealer.hand_value) ==20:
            print("\n* * * * * * * * * * * * * * * * * * * * *")
            print("Dealer on 19+. Staying!")
            print("* * * * * * * * * * * * * * * * * * * * *\n")
            gameon = False
            end_of_game()
            break
        elif Dealer.hand_value[0] == 11 and Dealer.hand_value[1] == 10 or Dealer.hand_value[1] == 11 and Dealer.hand_value[0] == 10:
            print("\n* * * * * * * * * * * * * * * * * * * * * * * * * *")
            print(f"Dealer has Black Jack!")
            print("* * * * * * * * * * * * * * * * * * * * * * * * * * *\n")
            gameon = False
            end_of_game()
        else:
            print("\n* * * * * * * * * * * * * * * * * * * * *")
            print("Dealer has 21")
            print("* * * * * * * * * * * * * * * * * * * * *\n")
            gameon = False
            end_of_game()
            break

# def list_to_string():
#     temp_cards = Dealer.card_names
#     dealer_cards = " "
#     return (dealer_cards.join(temp_cards))

def end_of_game():
    global player_funds
    global dealer_total
    global player_total
    global draw
    dealer_score = sum(Dealer.hand_value)
    player_score = sum(Player.hand_value)
    if sum(Dealer.hand_value) == sum(Player.hand_value) and sum(Dealer.hand_value) <= 20 and sum(Player.hand_value) <= 20:
        print(f"The scores are: \n{currentplayer}: {sum(Player.hand_value)} \nDealer: {sum(Dealer.hand_value)}")
        print(f"\nIt's a draw! {currentplayer} still has ${player_funds:,} remaining\n")
        draw += 1
        stats_file = open("stats.txt", "a+")
        stats_file.write(f"\nGame number {game_count} (Draw)\n")
        stats_file.write(f"\nDealer score: {dealer_score}\n")
        for x in range(len(Dealer.card_names)):
            stats_file.write(f"{Dealer.card_names[x]}\n")
        stats_file.write(f"\n{currentplayer} score: {player_score}\n")
        for x in range(len(Player.card_names)):
            stats_file.write(f"{Player.card_names[x]}\n")
        stats_file.write(f"\n{currentplayer} keeps: ${Player.bet:,}")
        stats_file.write(f"\n${player_funds:,} remaining\n")
        stats_file.write("\n******************************")
        stats_file.close()
        play_again_check()
    elif sum(Dealer.hand_value) and sum(Player.hand_value) > 21:
        print(f"The scores are: \n{currentplayer}: {sum(Player.hand_value)} \nDealer: {sum(Dealer.hand_value)}")
        player_funds -= Player.bet
        print(f"\nYou both went bust!")
        print(f"{currentplayer} lost ${Player.bet} and now has ${player_funds:,} remaining\n")
        stats_file = open("stats.txt", "a+")
        stats_file.write(f"\nGame number {game_count} (Both went bust)\n")
        stats_file.write(f"\nDealer score: {dealer_score}\n")
        for x in range(len(Dealer.card_names)):
            stats_file.write(f"{Dealer.card_names[x]}\n")
        stats_file.write(f"\n{currentplayer} score: {player_score}\n")
        for x in range(len(Player.card_names)):
            stats_file.write(f"{Player.card_names[x]}\n")
        stats_file.write(f"\n{currentplayer} lost: ${Player.bet:,}")
        stats_file.write(f"\n${player_funds:,} remaining\n")
        stats_file.write("\n******************************")
        stats_file.close()
        play_again_check()
    elif sum(Dealer.hand_value) > sum(Player.hand_value) and sum(Dealer.hand_value) <= 21:
        print(f"The scores are: \n{currentplayer}: {sum(Player.hand_value)} \nDealer: {sum(Dealer.hand_value)}")
        player_funds -= Player.bet
        print(f"Dealer won! {currentplayer} lost ${Player.bet:,} and now has ${player_funds:,} remaining\n")
        dealer_total += 1
        stats_file = open("stats.txt", "a+")
        stats_file.write(f"\nGame number {game_count} (Dealer won)\n")
        stats_file.write(f"\nDealer score: {dealer_score}\n")
        for x in range(len(Dealer.card_names)):
            stats_file.write(f"{Dealer.card_names[x]}\n")
        stats_file.write(f"\n{currentplayer} score: {player_score}\n")
        for x in range(len(Player.card_names)):
            stats_file.write(f"{Player.card_names[x]}\n")
        stats_file.write(f"\n{currentplayer} lost: ${Player.bet:,}")
        stats_file.write(f"\n${player_funds:,} remaining\n")
        stats_file.write("\n******************************")
        stats_file.close()
        play_again_check()
    elif sum(Dealer.hand_value) < sum(Player.hand_value) and sum(Player.hand_value) <= 20:
        print(f"The scores are: \n{currentplayer}: {sum(Player.hand_value)} \nDealer: {sum(Dealer.hand_value)}")
        player_funds += Player.bet
        print(f"{currentplayer} is the winner! {currentplayer} won ${Player.bet:,} and now has ${player_funds:,} remaining\n")
        player_total += 1
        stats_file = open("stats.txt", "a+")
        stats_file.write(f"\nGame number {game_count} ({currentplayer} won)\n")
        stats_file.write(f"\nDealer score: {dealer_score}\n")
        for x in range(len(Dealer.card_names)):
            stats_file.write(f"{Dealer.card_names[x]}\n")
        stats_file.write(f"\n{currentplayer} score: {player_score}\n")
        for x in range(len(Player.card_names)):
            stats_file.write(f"{Player.card_names[x]}\n")
        stats_file.write(f"\n{currentplayer} won: ${Player.bet:,}")
        stats_file.write(f"\n${player_funds:,} remaining\n")
        stats_file.write("\n******************************")
        stats_file.close()
        play_again_check()
    elif sum(Dealer.hand_value) <=21 and sum(Player.hand_value) >21: 
        print(f"The scores are: \n{currentplayer}: {sum(Player.hand_value)} \nDealer: {sum(Dealer.hand_value)}")
        player_funds -= Player.bet
        print(f"\nDealer won and {currentplayer} went bust")
        print(f"{currentplayer} lost ${Player.bet:,} and now has ${player_funds:,} remaining\n")
        dealer_total += 1
        stats_file = open("stats.txt", "a+")
        stats_file.write(f"\nGame number {game_count} (Dealer won, and {currentplayer} went bust)\n")
        stats_file.write(f"\nDealer score: {dealer_score}\n")
        for x in range(len(Dealer.card_names)):
            stats_file.write(f"{Dealer.card_names[x]}\n")
        stats_file.write(f"\n{currentplayer} score: {player_score}\n")
        for x in range(len(Player.card_names)):
            stats_file.write(f"{Player.card_names[x]}\n")
        stats_file.write(f"\n{currentplayer} lost: ${Player.bet:,}")
        stats_file.write(f"\n${player_funds:,} remaining\n")
        stats_file.write("\n******************************")
        stats_file.close()
        play_again_check()
    elif sum(Player.hand_value) <=20 and sum(Dealer.hand_value) >21: 
        print(f"The scores are: \n{currentplayer}: {sum(Player.hand_value)} \nDealer: {sum(Dealer.hand_value)}")
        player_funds += Player.bet
        print(f"\n{currentplayer} is the winner and dealer went bust")
        print(f"\n{currentplayer} won ${Player.bet:,} and now has ${player_funds:,} remaining\n")
        player_total += 1
        stats_file = open("stats.txt", "a+")
        stats_file.write(f"\nGame number {game_count} ({currentplayer} won, and Dealer went bust)\n")
        stats_file.write(f"\nDealer score: {dealer_score}\n")
        for x in range(len(Dealer.card_names)):
            stats_file.write(f"{Dealer.card_names[x]}\n")
        stats_file.write(f"\n{currentplayer} score: {player_score}\n")
        for x in range(len(Player.card_names)):
            stats_file.write(f"{Player.card_names[x]}\n")
        stats_file.write(f"\n{currentplayer} won: ${Player.bet:,}")
        stats_file.write(f"\n${player_funds:,} remaining\n")
        stats_file.write("\n******************************")
        stats_file.close()
        play_again_check()
    elif sum(Dealer.hand_value) < sum(Player.hand_value) and sum(Player.hand_value) == 21:
        print(f"The scores are: \n{currentplayer}: {sum(Player.hand_value)} \nDealer: {sum(Dealer.hand_value)}")
        player_funds += Player.bet*50
        print(f"{currentplayer} is the winner with 21 (Payout 50/1)")
        print(f"{currentplayer} won ${Player.bet*50:,} and now has ${player_funds:,} remaining\n")
        player_total += 1
        stats_file = open("stats.txt", "a+")
        stats_file.write(f"\nGame number {game_count} ({currentplayer} won with 21)\n")
        stats_file.write(f"\nDealer score: {dealer_score}\n")
        for x in range(len(Dealer.card_names)):
            stats_file.write(f"{Dealer.card_names[x]}\n")
        stats_file.write(f"\n{currentplayer} score: {player_score}\n")
        for x in range(len(Player.card_names)):
            stats_file.write(f"{Player.card_names[x]}\n")
        stats_file.write(f"\n{currentplayer} won: ${Player.bet*50:,}")
        stats_file.write(f"\n${player_funds:,} remaining\n")
        stats_file.write("\n******************************")
        stats_file.close()
        play_again_check()
    elif sum(Player.hand_value) ==21 and sum(Dealer.hand_value) ==21: 
        print(f"The scores are: \n{currentplayer}: {sum(Player.hand_value)} \nDealer: {sum(Dealer.hand_value)}")
        player_funds += Player.bet*50
        print(f"\n{currentplayer} and dealer draw with 21.. Payout is still 50/1 :-)")
        print(f"\n{currentplayer} won ${Player.bet*50:,} and now has ${player_funds:,} remaining\n")
        draw += 1
        stats_file = open("stats.txt", "a+")
        stats_file.write(f"\nGame number {game_count} ({currentplayer} and dealer draw with 21)\n")
        stats_file.write(f"\nDealer score: {dealer_score}\n")
        for x in range(len(Dealer.card_names)):
            stats_file.write(f"{Dealer.card_names[x]}\n")
        stats_file.write(f"\n{currentplayer} score: {player_score}\n")
        for x in range(len(Player.card_names)):
            stats_file.write(f"{Player.card_names[x]}\n")
        stats_file.write(f"\n{currentplayer} won: ${Player.bet*50:,}")
        stats_file.write(f"\n${player_funds:,} remaining\n")
        stats_file.write("\n******************************")
        stats_file.close()
        play_again_check()
    elif sum(Player.hand_value) ==21 and sum(Dealer.hand_value) >21: 
        print(f"The scores are: \n{currentplayer}: {sum(Player.hand_value)} \nDealer: {sum(Dealer.hand_value)}")
        player_funds += Player.bet*50
        print(f"\n{currentplayer} has 21 and dealer is bust")
        print(f"\n{currentplayer} won ${Player.bet*50:,} and now has ${player_funds:,} remaining\n")
        player_total += 1
        stats_file = open("stats.txt", "a+")
        stats_file.write(f"\nGame number {game_count} ({currentplayer} 21 and dealer went bust)\n")
        stats_file.write(f"\nDealer score: {dealer_score}\n")
        for x in range(len(Dealer.card_names)):
            stats_file.write(f"{Dealer.card_names[x]}\n")
        stats_file.write(f"\n{currentplayer} score: {player_score}\n")
        for x in range(len(Player.card_names)):
            stats_file.write(f"{Player.card_names[x]}\n")
        stats_file.write(f"\n{currentplayer} won: ${Player.bet*50:,}")
        stats_file.write(f"\n${player_funds:,} remaining\n")
        stats_file.write("\n******************************")
        stats_file.close()
        play_again_check()

def dealer_one_card_deal():
    global whole_deck
    if len(whole_deck.all_cards) <10:
        print("\n"*20)
        print("\n***************************")
        print("    Deck was low on cards")
        print("***************************")
        print("    Added new deck")
        print("***************************")
        print("    Shuffled new deck")
        print("***************************\n")
        whole_deck = Deck()
        random.shuffle(whole_deck.all_cards)
        Dealer.hand.append(whole_deck.deal_one())
    else:
        Dealer.hand.append(whole_deck.deal_one())

def player_one_card_deal():
    global whole_deck
    if len(whole_deck.all_cards) <10:
        print("\n"*20)
        print("\n***************************")
        print("    Deck was low on cards")
        print("***************************")
        print("    Added new deck")
        print("***************************")
        print("    Shuffled new deck")
        print("***************************\n")
        whole_deck = Deck()
        random.shuffle(whole_deck.all_cards)
        Player.hand.append(whole_deck.deal_one())
    else:
        Player.hand.append(whole_deck.deal_one())

def dealer_two_card_deal():
    global whole_deck
    if len(whole_deck.all_cards) <10:
        print("\n"*20)
        print("\n***************************")
        print("    Deck was low on cards")
        print("***************************")
        print("    Added new deck")
        print("***************************")
        print("    Shuffled new deck")
        print("***************************\n")
        whole_deck = Deck()
        random.shuffle(whole_deck.all_cards)
        Dealer.hand.append(whole_deck.deal_one())
        Dealer.hand.append(whole_deck.deal_another())
    else:
        Dealer.hand.append(whole_deck.deal_one())
        Dealer.hand.append(whole_deck.deal_another())

def player_two_card_deal():
    global whole_deck
    if len(whole_deck.all_cards) <10:
        print("\n"*20)
        print("\n***************************")
        print("    Deck was low on cards")
        print("***************************")
        print("    Added new deck")
        print("***************************")
        print("    Shuffled new deck")
        print("***************************\n")
        whole_deck = Deck()
        random.shuffle(whole_deck.all_cards)
        Player.hand.append(whole_deck.deal_one())
        Player.hand.append(whole_deck.deal_another())
    else:
        Player.hand.append(whole_deck.deal_one())
        Player.hand.append(whole_deck.deal_another())

def play_again_check():
    global game_count
    while True:
        playagain = input("\nPlay again? y/n   ")
        if playagain == ("y") or playagain == ("Y"):
            game_count += 1
            repeat_game()
            break
        elif playagain == ("n") or playagain == ("N"):
            print("\nThanks for playing!\n")
            print("\nThe game stats will be emailed to you\n")
            stats_file = open("stats.txt", "a+")
            stats_file.write("\n"*5)
            stats_file.write("\n******************************")
            stats_file.write("\nGame stats")
            stats_file.write("\n******************************\n")
            stats_file.write(f"\nNumber of games {game_count}\n")
            stats_file.write(f"\nDealer won: {dealer_total}\n")
            stats_file.write(f"\n{currentplayer} won: {player_total}\n")
            stats_file.write(f"\nDraws: {draw}\n")
            stats_file.write("\n******************************")
            stats_file.write("\n*******")
            stats_file.write("\n******")
            stats_file.write("\n*****")
            stats_file.write("\n****")
            stats_file.write("\n***")
            stats_file.write("\n**")
            stats_file.write("\n*")
            stats_file.write("\nMukas Code Corporation")
            stats_file.close()
            # read_the_stats()
            email_the_stats()
            break
        else:
            print("\nBad input, please try again\n")

def email_the_stats():
    with open('stats.txt', 'r') as gamefile:
        gameinfo = gamefile.read().rstrip('\n')

    fromx = 'Mukas Code Corporation'
    sender_email  = input("Type sender email address and press enter:  ")
    to  = input("Type recipient email address and press enter:  ")
    msg = MIMEText(gameinfo)
    msg['Subject'] = 'Game stats, Mukas Black Jack'
    msg['From'] = fromx
    msg['To'] = to

    server = smtplib.SMTP('smtp.gmail.com:587')
    password = input("Type sender password and press enter:  ")
    server.starttls()
    server.ehlo()
    server.login(sender_email, password)
    server.sendmail(fromx, to, msg.as_string())
    server.quit()
    print("\n"*2)
    print("Your game stats have been emailed")
    print("\n"*2)

def reveal_before_bet():

    print("\nDealer's cards:")
    for c in Dealer.card_names: print(c)
    print("\nDealer's card values:")
    print(Dealer.hand_value)
    print("\nDealer's hand value:")
    print(sum(Dealer.hand_value))
    print("* * * * * * *\n")

    print(f"\n{currentplayer}'s cards:")
    for c in Player.card_names: print(c)
    print(f"\n{currentplayer}'s card values:")
    print(Player.hand_value)
    print(f"\n{currentplayer}'s hand value:")
    print(sum(Player.hand_value))
    print("* * * * * * * * * * * * * * * * * * * * *\n")

def repeat_game():
    Player.hand.clear()
    Player.card_names.clear()
    Player.hand_value.clear()
    Dealer.hand.clear()
    Dealer.card_names.clear()
    Dealer.hand_value.clear()
    
    print(f"\n**************** NEW GAME **************** GAME no. {game_count} ****************")
    print(f"\n*********************** Cards left in deck: {len(whole_deck.all_cards)} ***********************\n")
    print(f"\nHello again {currentplayer}\n")

    # First deal (two cards each)
    dealer_two_card_deal()
    player_two_card_deal()

    # add dealt card(s) value to a list for value calculation
    dealer_addvalue_func()
    # add dealt card(s) value to a list for value calculation
    player_addvalue_func()

    reveal_before_bet() # Player has the upper hand. Can see the dealers cards before betting :-)

    bet_func()

    # Run the calc for 21 etc
    gameon_dealer_func()
    # Run the calc for 21 etc
    gameon_player_func()

#@@@@@@@@@@@@@@@@@@@@@@@ Game play script @@@@@@@@@@@@@@@@@@@@@@@@@@

whole_deck = Deck()
random.shuffle(whole_deck.all_cards)

currentplayer = Player()
gameinfo = datetime.datetime.now()
gamedate = (gameinfo.strftime("%B %d, %Y"))
gametime = (gameinfo.strftime("%H:%M:%S"))
if os.path.exists("stats.txt"):
    os.remove("stats.txt")
else:
    print("...")
print(f"\nWelcome {currentplayer}")
# stats_file = open(f"{currentplayer}_stats.txt", "x")
# stats_file = open(f"{currentplayer}_stats.txt", "a+")
stats_file = open("stats.txt", "x")
stats_file = open("stats.txt", "a+")
stats_file.write(f"Mukas Black Jack, stats for {currentplayer}\n")
stats_file.write(f"\n{gamedate}\n")
stats_file.write(f"{gametime}\n")
stats_file.close()

# First deal (two cards each)
dealer_two_card_deal()
player_two_card_deal()

# add dealt card(s) value to a list for value calculation
dealer_addvalue_func()
# add dealt card(s) value to a list for value calculation
player_addvalue_func()

reveal_before_bet() # Player has the upper hand. Can see the dealers cards before betting :-)

bet_func()

# Run the calc for 21 etc
gameon_dealer_func()
# Run the calc for 21 etc
gameon_player_func()

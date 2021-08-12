from art import logo
import random

user_cards = []
computer_cards = []
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
still_play = True

def deal_card(cards):
    return random.sample(cards,2)
   
user_cards = deal_card(cards)
computer_cards = deal_card(cards)

def  calculate_score(arry_cards):
    if 11 in arry_cards and 10 in arry_cards:
       return 0
    elif sum(arry_cards) > 21 and 11 in arry_cards:
        return   (sum(arry_cards) - 11) + 1
    else:
       return sum(arry_cards)

def compare(last_user_score, last_computer_score):
    print(f"Your cards : {user_cards}, current score: {user_score} \nComputer's card : {computer_cards}, computer score {computer_score}")
    if last_user_score == last_computer_score:
        print("draw")
    elif last_computer_score == 0:
        print("You lost")
    elif last_user_score == 0:
        print("You win the blackjack")
    elif last_user_score  > 21:
        print("You lost")
    elif last_computer_score > 21:
            print("You wine")
    elif last_computer_score > last_user_score:
        print("You lost")
    elif last_user_score > last_computer_score:
        print("You wine the blackjack")
    else:
        print("In possible game")
        
are_you_play = input("Do you want to play a game of Blackjack ? 'y' or 'n' ")

if are_you_play.lower() == 'y':
    user_score = calculate_score(user_cards);
    computer_score = calculate_score(computer_cards)
    
    while still_play:
     print(logo)

     print(f"Your cards : {user_cards}, current score: {user_score} \nComputer's first card : {computer_cards[0]}")
     choose_to_play = input("Type 'y' to get another card, type 'n' to pass: ")

     if choose_to_play.lower() == 'y':
        user_cards.append(random.choice(cards))
        computer_cards.append(random.choice(cards))
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        if user_score == 0 or computer_score == 0 or user_score > 21:
            still_play = False
            print("Game is over")

     else:
         still_play = False
         while computer_score < 17:
             print(computer_score)
             computer_cards.append(random.choice(cards))
             computer_score = calculate_score(computer_cards)
             
    compare(user_score, computer_score)

else:
    print("Thank you for visiting")
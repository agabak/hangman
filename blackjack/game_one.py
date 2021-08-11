from art import logo
import random

user_cards = []
computer_cards = []



print(logo)

def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.sample(cards,2)
   
user_cards = deal_card()
computer_cards = deal_card()

def  calculate_score(arry_cards):
    print(arry_cards)
    if 11 in arry_cards and 10 in arry_cards:
       return 0
    elif sum(arry_cards) > 21 and 11 in arry_cards:
        return   (sum(arry_cards) - 11) + 1
    else:
       return sum(arry_cards);
    
user_score = calculate_score(user_cards);
computer_score = calculate_score(computer_cards)

if user_score > 21:
    print("You loss")

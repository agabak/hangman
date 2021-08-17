from art import logo, vs
from game_data import  data
import random

print(logo)
def  who_have_more_follower():
    questions = random.sample(data,2)
    print(f"Compare A: {questions[0]['name']}, a {questions[0]['description']}, from {questions[0]['country']} .")
    print(vs)
    print(f"Compare B: {questions[1]['name']}, a {questions[1]['description']}, from {questions[1]['country']} .")
    return  {'A': questions[0], 'B': questions[1]}



def play_game():
    score = 0;
    game_over = False
    while not game_over:
        result =  who_have_more_follower()
        who_foller = input("Who has more followers ? Type 'A' or 'B'. ").lower()
        if who_foller == 'a' and  result['A']['follower_count'] > result['B']['follower_count']:
            score +=1
            print(result['A']['follower_count'])
        elif who_foller == '' and result['B']['follower_count'] > result['A']['follower_count']:
            score +=1
            print(result['B']['follower_count'])
        else:
            game_over = True
            print(f"Sorry , that's wrong. Final score  {score}")
        
        
play_game()
        




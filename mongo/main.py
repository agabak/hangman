
#Hangman
from os import O_LARGEFILE
import  random
import  hangman_word
import hangman_art 
word_list = hangman_word.word_list
stegas = hangman_art.stages
display = []
lives = 6

print(hangman_art.logo)
chosen_word = random.choice(word_list)
print(f"Psst, the solution is {chosen_word}")

for _ in chosen_word:
    display.append("_")

# *** check if there more "_" in the display array *** 
end_of_game = False

while  not end_of_game:
    guess = input("Guess a letter ").lower()

    if guess in chosen_word:
        print(f"You have already guessed this {guess} letter")

    for indx, letter in enumerate(chosen_word):
        if letter == guess:

 # print(f"Current position: {indx} Current letter: {letter} Guess letter: {guess}")
            display[indx] = guess;

    if guess not in chosen_word:
        print(stegas[lives])
        lives -= 1
        print(f" {guess} it's not in the word")
        if lives == 0:
            end_of_game = True
            print("You lose")
        
    if "_"  not in display:
        end_of_game = True
        print("You wine")

    print(display)

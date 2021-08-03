#print('What is the name of your band')
#name_of_city = input('Whay is the name of your city')
#print(name_of_city)
#name_of_pety = input('What is the name of your pet ? ')
#print(name_of_pety)
#print('Your band name is ' + name_of_city + ' ' + name_of_pety)
#is_working = False
#print(is_working)
#print(len("Hello there"))

#num_char =len(input('what is your name ?'))
#print(num_char)

#print(type(num_char))

#char_num = str(num_char)

#print(type(char_num))

#def add_number(a,b):
#    if(type(a) == int and type(b)):
#        return a + b
#    elif(type(a) == str and type(b)):
#        return int(a) + int(b)
#    else:
#      return  'Make sure is number or string or  int'

#print(add_number(8,7))
#print(add_number('8','7'))
#print(add_number(8.0,7))

#def digit_number(num):
#    if(type(num) == str):
#        first_num = num[0];
 #       second_num = num[1]
#        return int(first_num) + int(second_num)
#    else:
#        return 'Make sure is string'

#print(digit_number('35'))
#print(digit_number(45))
#print(3-3/3 + 3*3)


#print("BMI")
##weight = input("What is you're weith ? ") 
#print(weight)
#height = input("What is you're height ? ")
#print(height)

#bmi = int(weight) / (float(height)**2)

#print(int(bmi))

#print(int(6/8))
#print(round(6/8, 3))

#print(9//8)

#if-string  is the sane as using $ or @ in c#
#print(f"youre score is {bmi}")

#age_lived = input("What is your current age ? ")
#year_lived = int(age_lived)
#limit_age = 90;
#total_dayes = 365
#total_week = 52
#total_month = 12

#years_left = limit_age - year_lived
#month_left = years_left * total_month
#week_left = years_left * total_week
#days_left = years_left * total_dayes

#print(f"You have {days_left} days, {week_left} weeks, and {month_left} months left")

#print(6 +4/2-(1*2))
#print("Welcome to the tip calculator.")
#final_bill = input("What was the total bill? $")
#tip_percent = input("What percentage tip would you like to give ? 10, 12, 15 ")
#num_guest = input("How many people to split the bill ?")
#tip_as_percent = int(tip_percent)/100


#total_tip_amont = float(final_bill) *  float(tip_as_percent)
#print(total_tip_amont)

#total_amont = float(final_bill) + total_tip_amont
#print(total_amont)


#each_guest =  float(total_amont)/int(num_guest)

#print(each_guest)

#total = "{:.2f}".format(each_guest)
#print(f"Each  person should pay: ${total}")


# we don't need random librariry for range method

#def three_num(arrays):
#    count = 0
#    for num in arrays:
#        for num1 in arrays:
#            print(num1)
#            for num2 in arrays:
#                if(num + num1 + num2 == 0):
#                    print(num, num1, num2, count)
#                    count +=1
#  print(f"{count} - count")
#
# three_num([3,4,5,6,9,-3])

#Hangman
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

#check if there more "_" in the display array
end_of_game = False

while  not end_of_game:
    guess = input("Guess a letter ").lower()

    if guess in chosen_word:
        print(f"You have already guessed thid {guess} letter")

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

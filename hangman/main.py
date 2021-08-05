# Work with leap year
# def find_leap_year(year):
#    if (year % 4 == 0 and year % 100 != 0) or year % 100 == 0 and year  % 400 == 0:
#        return "leap year"
#    else:
#        return "not leap year"
#
# year = int(input("please enter the year"))
#
# print(find_leap_year(year))
#
# ticket system
# check if you can ride or not
# def is_ride_rollercoaster(height):
#    if type(height) == float or type(height) == int:
#        return height  >= 120
#    else:
#        return False;
# this function will return the price of the ride accoutding to their age
# def price_for_rollercoaster(age):
#   if age < 12:
#       return 5.00
#    elif age <= 18: 
#        return 7.00
#    elif age >= 45 and age <=55:
#        return 0
#   else:
#        return 12.00
#
# this function will return true or false      123
# def pay_picture(yorn): 
#   if type(yorn) == str:
#      return  True if yorn.upper() == "Y" else False
# height = float(input("What is your height ? "))
# age  = int(input("What is your age ? "))   
# can_rollercoaster = is_ride_rollercoaster(height)
# message = "Older" if age  > 18  else "Your young buck"  
# if can_rollercoaster:
#    price = price_for_rollercoaster(age)
#    picture = input("Please enter Y for yes or N or no ")
#   want_picture = pay_picture(picture)
#   if want_picture:
#        price +=3
#    print(f"{message} Your price is {price}")
# else:
#    print("Sorry, You have to frow taller before you can ride ")
# to Lower in python .lower()
# print("Agaba".lower())
# print("Agaba".upper())


#print("Welcome to the treasure island.\nYour mission is to find the treasure. " )
#
#left_or_right = input("Enter left or right ? " )
#if left_or_right.lower() == 'left':
#    swim_or_wait  = input("Enter swim or wiat ? " )
#    if swim_or_wait.lower() =="wait":
#       door_color = input("What color of the door, red, blue or yellow ? " )
#       if door_color.lower() == "yellow":
#           print("You win the game")
#       else:
#           print("LOSSER !!")
#    else:
#        print("Game over")
#else:
# print("Game over")
# import my_module
#print(my_module.pi)
#import random
 
#rand = random.randint(100,200)
# 0.00000 - 0.99999 ...
#print(random.random() * 5)
#random_side = random.randint(0,1)
#print(random_side)
#if random_side == 1:
#    print('Heads')
#else:
#    print('Tails')

#python list - data structure
#states_of_america = ["Delaware","Pennsylvania",
#"New Jersey","Georgia","Connecticut","Massachusetts","Maryland","South Carolina","New Hampshire","Virginia","New York","North Carolina",
#"Rhode Island","Vermont","Kentucky","Tennessee","Ohio","Louisiana","Indiana","Mississippi","Illinois","Alabama","Maine","Missouri",
#"Arkansas","Michigan","Florida","Texas","Iowa","Wisconsin","California","Minnesota","Oregon","Kansas","West Virginia","Nevada","Nebraska",
#"Colorado","North Dakota","South Dakota","Montana","Washington","Idaho","Wyoming","Utah","Oklahoma","New Mexico","Arizona","Alaska","Hawaii"]

#import random
# take input of names
#name_string = input("Give avery boday name follow by ,")   #"Angela, Ben, Jenny, Michael, Chloe"
#name = name_string.split(",")
#random_choice = random.randint(0,len(name) - 1)
#print(f"{name[random_choice]} will pay a bill")
# len(list) total count of the item in the list, split(",") create a list from a string

#using random choice function

#person_pay_for_meal = random.choice(name)
#print(f"{person_pay_for_meal} will pay for meal today")
#is_true = True person_pay_for_meal == name[4] else False
#fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
#print(fruits[-6])
#fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
#fruits[-1] = "Melons"
#fruits.append("Lemons")
#print(fruits)
#fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
#vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]
#dirty_dozen = [fruits, vegetables]
#print(dirty_dozen[1][1])
#is_true = True if type("agaba") == str else False

#for item in dirty_dozen[1]:
# for item2 in dirty_dozen[0]:
#    print(item2)
    

# using for loop
#student_heights = [180, 124,165,173,189,169,146]
#total_student_heights = 0
#average_heights = 0
#count = 0
#for student in student_heights:
#       total_student_heights += student
#       count +=1
#average_heights = round(total_student_heights/count)
#print(average_heights)


# using sum() and len() functions
#sum_height = sum(student_heights)/ len(student_heights)
#student_scores = [78,65,89,86,55,91,64,89]
#heigher_score = 0
#for score in student_scores:
#    if score > heigher_score:
#        heigher_score = score       
#print(heigher_score)
# total = 0
#for num in range(1,101):
#    total += num
#print(total)
#total_even_number = 0
#for even in range(1,101):
#    if even % 2 == 0:
#        total_even_number += even
        
        
#print(total_even_number)


#Fizz Buzz
#for number in range(1,101):
#    if number % 3 == 0 and number % 5 == 0:
#            print("FizzBuzz")
#    elif number % 3 == 0:
#        print("Fizz")
#    elif number % 5 == 0:
#        print("Buzz")
#    else:
#        print(number)


#working with while loop
#import random
#letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
#numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
#symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
#
#print("Welcome to the PyPassword Generator!")
#nr_letters= int(input("How many letters would you like in your password?\n")) 
#nr_symbols = int(input(f"How many symbols would you like?\n"))
#nr_numbers = int(input(f"How many numbers would you like?\n"))


# create empy array to hold you're letters symbols and numbers
#password_list = []

# choice one form the collection of letters in each iteration
#for letter in range(1, nr_letters + 1):
#    password_list.append(random.choice(letters))
 
 # choice one symbol in every iteration   
#for symbol in range(1,nr_symbols + 1):
#    password_list.append(random.choice(symbols))
    
# choice one number for each iteration
#for number in range(1, nr_numbers + 1):
#    password_list.append(random.choice(numbers))

# shuffle to the array to make it random in every generation    
#random.shuffle(password_list)

# convert a array to str
#password = "".join(password_list)

    
#print(password)


#hangman Game
import random
import hangman_art 
import hangman_words
end_of_game = False
lives = 6
word_list = hangman_words.word_list
display = []
stages = hangman_art.stages

#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.
chosen_word = random.choice(word_list)

#Testing code
print(hangman_art.logo)

for  _  in chosen_word:
    display.append("_")

print(display)

while not end_of_game:
    #TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
    guess = input("Guess a letter:  ").lower()

    #TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
    for indx, letter  in  enumerate(chosen_word):
        if  letter == guess:
            display[indx] = letter 
            
    if guess not in chosen_word:
        print(stages[lives - 1])
        lives -= 1
        
    if lives == 0:
        end_of_game = True
        print("You Lose")
                   
    print(display)

        
    if "_" not in display:
        end_of_game = True
        print("You win.")
        
    

      

    

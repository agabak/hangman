from os import name
import math

def greet(name,message):
    print(name , message)


def greet_with(name,location):
    if type(name) == str and name and type(location) and location:
       print(f'Hello {name} \nWhat is it like in {location}')



def pint_wall(height,width):
    number_of_cans = round((height * width)/5)
    print(f"Yo'll need {number_of_cans} number of cans")
    a_arae = math.ceil((height*width)/5)
    print(a_arae)

def prime_checker(number):
    is_prime = True;
    for i in range(2,number):
        if number % i == 0:
            is_prime = False;

    if is_prime == True:
        print("Is the prime number")
    else:
        print("Is not prime number")

prime_checker(21)
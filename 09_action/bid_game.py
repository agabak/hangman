from replit import clear
from art import logo

print(logo)
end_of_bid = False
bid = {}

while not  end_of_bid:
  name = input("What is you're name ? ")
  price = int(input("How much you bid for $ ?"))
  bid["name"] = name
  bid["price"] = price

  some_else = input("Some else in the room to bid Yes or No").lower()
  if  some_else == "no":
    end_of_bid = True
  else:
    clear()



price(bid)
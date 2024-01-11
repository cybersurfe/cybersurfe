from replit import clear

import art

print(art.logo)

print("Welcome to the secret auction program!")

recycle = True

auctioneers = {}

def add_new_bidder(x,y):
   auctioneers.update({x:y})
  
while recycle == True:
  name = input("What is your name?:\n")
  bid_price = int(input("What is your bid?:\n $"))
  add_new_bidder(name, bid_price)
  
  redo = input("Are there any other bidders. Type 'yes' or 'no'.")
  
  if redo == 'yes':
    clear()
    recycle = True
  else:
    max = 0
    for x,y in auctioneers.items():
      if y > max:
        max = y
        winner = x
    print(f"The winner is {winner} with a bid of ${max}.")
    recycle = False
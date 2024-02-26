from replit import clear
from art import logo

print(logo)
print("Welcome to the secret auction program.")

more_names = True
bid_dictionary = {}

while more_names:
  name = input("What is your name?: ")
  bid_value = input("What is your bid?: $")
  
  bid_dictionary[name] = bid_value

  other_bidders = input("Are there any other bidders? Type 'yes' or 'no': ").lower()
  if other_bidders == "yes":
    clear()
  else:
    more_names = False
    clear()
    highest_value = 0
    winner = ''
    for player in bid_dictionary:
      if int(bid_dictionary[player]) > highest_value:
        highest_value = int(bid_dictionary[player])
        winner = player
    print(f"{winner} is the winner with a bid of ${highest_value}.")



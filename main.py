############### Blackjack Project #####################
from art import logo
from replit import clear
import random
#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size.
## There are no jokers.
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

##################### Hints ####################
def print_computer_cards(computer_cards):
  for card in range(0,len(computer_card)-1):
    print(f"[{card}]")
first_game = input(
    "Do you want to play a game of Blackjack? Type 'y' or 'n': ")
play = 1
if first_game == "y":
  while play == 1:
    print(logo)

    your_card = []
    card1 = random.choice(cards)
    card2 = random.choice(cards)
    your_card.append(card1)
    your_card.append(card2)
    print(f"Your cards: {your_card}")

    computer_card = []
    card3 = random.choice(cards)
    computer_card.append(card3)
    print(f"Computers first card: {computer_card}")
    card5 = random.choice(cards)
    computer_card.append(card5)
    keep_drawing = 0
    stop = 0
    another_card = input("Type 'y' to get another card, type 'n' to pass: ")
    if another_card == "y":
      keep_drawing = 1
      
    else:
      print(f"Your hand: {your_card}")
      print(f"Computers hand: {print_computer_cards}")
      if sum(your_card) > 21 and sum(computer_card)<=21:
        print("You lose")
        stop=1
     
      elif sum(computer_card) > 21:
        print("You win")
        stop=1

      elif sum(your_card) == sum(computer_card):
        print("Draw")
        stop=1
      elif sum(your_card) > sum(computer_card) and sum(your_card)<=21 and sum(computer_card)<=21:
        print("You win")
        stop=1
      elif sum(your_card) < sum(computer_card) and sum(your_card)<=21 and sum(computer_card)<=21:
        print("You lose")
        stop=1

    
      
    

    while keep_drawing == 1 and stop == 0:
      card4 = random.choice(cards)
      your_card.append(card4)
      if sum(computer_card) < 17:
        card6 = random.choice(cards)
        computer_card.append(card6)
      print(f"Your hand: {your_card}")
      print(f"Computers hand: {computer_card}")
      if sum(your_card) > 21:
        print("You lose")
        stop = 1
      elif sum(computer_card) > 21:
        print("You win")
        stop = 1
    
      keep_drawing = 0
      another_card = input("Type 'y' to get another card, type 'n' to pass: ")
     
      if another_card == "y":
        keep_drawing = 1
      elif another_card =="n":
          
          print(f"Your hand: {your_card}")
          print(f"Computers hand: {computer_card}")
          if sum(your_card) > 21 and sum(computer_card)<=21:
            print("You lose")
            stop = 1
            keep_drawing = 0
          elif sum(computer_card) > 21:
            print("You win")
            stop = 1
            keep_drawing = 0

          elif sum(your_card) == sum(computer_card):
            print("Draw")
            stop = 1
            keep_drawing = 0
          elif sum(your_card) > sum(computer_card) and sum(your_card)<=21 and sum(computer_card)<=21:
            print("You win")
            stop = 1
            keep_drawing = 0
          elif sum(your_card) < sum(computer_card) and sum(your_card)<=21 and sum(computer_card)<=21:
            print("You lose")
            stop = 1
            keep_drawing = 0
          

    
    keep_playing = input(
        "Do you want to play a game of Blackjack? Type 'y' or 'n': ")

    if keep_playing == "y":
      play = 1
    else:
      play = 0

print("Thank you for playing")

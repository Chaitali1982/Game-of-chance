import random

money = 100

#Write your game of chance functions here
#What should happen if a player tries to bet more money than they have?
print("-----Games of Chance------")
def more(bet):
 if bet >= money:
  print("You can bet")
 else:
  print("you want to borrow money")




#STEP 3
#HEAD and TAILS GAME
def coin_flip(guess, bet):

 if(bet > 0):
   print("You can play COIN-FLIP")
 else:
   print("you can not play COIL-FLIP")
   
 number= random.randint(1, 2)
 if number == 1:
  print("num is Heads!")
 if number == 2:
  print("num is Tails")
  #Ignore case of head and tail
 
 if guess == "Heads" and number == 1:
  print("You win by" +str(bet))
  return bet
 if guess == "Tails" and number == 2:
  print("You win by" +str(bet))
  return bet
 if guess == "Tails" and number == 1:
  print("You lose by" +str(bet))
  return -bet
 if guess == "Heads" and number == 2:
  print("You lose by" +str(bet))
  return -bet
#step 4 Cho-Han DICE Game
def dice(guess, bet):

 if(bet > 0):
   print("--------------------------------")
   print("You can play Cho-Han Dice game")
 else:
   print("--------------------------------")
   print("you can not play Cho-Han Dice game")

 dice1= random.randint(1, 6)
 dice2= random.randint(1, 6)
 add = dice1 + dice2

 if guess == "even" and add % 2 == 0:
   print("You win by" +str(bet))
   return bet
 if guess == "odd" and add % 2 == 1:
   print("You lose by" +str(bet))
   return -bet
 else:
   print("You lose by" +str(bet))
   return -bet

#step 5 CARD GAME
def card_game(bet):

 if(bet > 0):
   print("--------------------------------")
   print("You can play Card game")
  
 else:
   print("--------------------------------")
   print("you can not play Card game")

 my= random.randint(1, 10)
 your= random.randint(1, 6)
 print("my number is " + str(my))
 print("your number is " + str(your))

 if my > your:
   print("You win by " +str(bet))
   return bet
 if your > my:
   print("You lost by " +str(bet))
   return -bet
 if your == my:
   print("It is TIE ")
   return -bet

#step 6  roulette game
def multigame(guess,bet):
  if(bet > 0):
    print("--------------------------------")
    print("You can play roulette game")
  else:
    print("--------------------------------")
    print("you can not play game")
  value= random.randint(1, 36)
  if(value == 36):
     print("wheel is loading on 00")
   
  else:
     print("wheel is loading on "  +str(value))
     
     
  if guess == "Even" and value % 2 == 0 and value != 0:
     print(str(value) + " is an even number.")
     print("You won Even " + str(bet)+" dollars!")
     return bet
     print("--------------------------------")
  elif guess == "Odd" and value % 2 == 1 and value != 37:
      print(str(value) + " is an odd number.")
      print("You won Odd " + str(bet)+" dollars!")
      return bet
      print("--------------------------------")
  elif guess == value:
      print("You guessed " + str(guess) + " and the result was " + str(value)) 
      print("You won " + str(bet * 35)+" dollars!")
      return bet * 35
      print("--------------------------------")
  else:
      print("You lost " + str(bet)+" dollars!")
      return -bet
      print("--------------------------------")

#step 7 call function
money += coin_flip("Heads", 10)
money += card_game(5)
money += dice("even", 2)
money += multigame("even", 10)
money += multigame(3, 1)
money += multigame("Odd", 100)
("--------------------------------")
print("Your total amount of money is " + str(money))

    


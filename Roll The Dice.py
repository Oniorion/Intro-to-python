# Dice rolling final project
# First we will need to import some libarays
import random
import time
# Player will enter in their name
player_one = input ("Player one please enter your name: ")
# Min and Max like range for the program
min = 1
max = 6

# Sets the min/max for the dice
a = 0

# This is the part of the code that will take the input from reroll and either rolls again or quits
for name in player_one:
    reroll = "yes"
while reroll == "yes": 
   if reroll == "no":
      exit(0)
# After 1 sec. the program will then move to the next line
   time.sleep(1)

   print ("\nDie is rolling",player_one,"please wait...")
      
   time.sleep (2)
# Selects a random dice face
   a = random.randint(min, max)

# Decided to display the dice face instead of just displaying the number
# Now it displays the number along with the face
   def dice (Face):
     if Face == 1:
      print (""" 
       You Rolled a 1,
          _________
         |         |
         |         |  
         |    *    | 
         |         | 
         |_________|  
         
         """)
         
     elif Face == 2:
      print  ("""
       You Rolled a 2,
          _________
         |         |
         |     *   |
         |         | 
         |   *     | 
         |_________|  
         
         """)
      
     elif Face == 3:
      print ("""
       You Rolled a 3,
          _________
         |         |
         |      *  |  
         |    *    | 
         |  *      | 
         |_________|  
         
         """) 
    
     elif Face == 4:
      print ("""
       You Rolled a 4,
          _________
         |         |
         |  *   *  |  
         |         | 
         |  *   *  | 
         |_________|  
         
         """) 
    
     elif Face == 5:
      print (""" 
       You Rolled a 5,
          _________
         |         |
         |  *   *  |  
         |    *    | 
         |  *   *  | 
         |_________|  
         
         """)
    
     elif Face == 6:
      print (""" 
       You Rolled a 6,  
          _________
         |         |
         |  *   *  |  
         |  *   *  | 
         |  *   *  | 
         |_________|  
         
         """)
   
   dice (a)

   print ("To keep playing type yes, type no to exit")
   # Very last a simple user input asking if the user would like to reroll 
   # Which then depening on the input will either roll again or exit
   reroll = input("\nWould you like to roll the die again? ")
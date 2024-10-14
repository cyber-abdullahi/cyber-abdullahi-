# This app think of a random colour and prompt the user to get what the colour is.check to see if The user guess matches the color it thinks about as well as counts the number of guess


import random as r

colour_list = ['red','green','blue','yellow','orange','white','blackj'] #a list of color the app choses 

# App chooses a random colour
app_choice = r.choice(colour_list)

#Define the player guess counter
guesses = 0

# prompt user to guess the color
while True:
    print("I am thinking of a color , guess what it is!")
    user_guesss = input() # This store the user guess

    if 'user_guess' != app_choice:
       print("you guessed wrong.Try again!") 
       guesses = + 1
    else:
        break

print (f"you geussed right.it took you {guesses} guesss")





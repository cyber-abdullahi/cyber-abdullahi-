#This app plays "Rock,paper,scissors,game with the user"

#Initiate computer's choice
import random
choice_list = ["Rock","Paper","Scissor"]
app_choice = random.choice(choice_list) #app choose from the list...

#Initiate user's choice
user_chioce = input("Welcome to the game. Rock Paper or Scissors?:").capitalize()



# Enter validation
while user_chioce not in ["Rock","Paper","Scissor"]:
    user_chioce = input("Invalid entry.Enter Rock, Paper or Scissor:").capitalize()

    # compare user entry and app choice and determine winner

    if user_chioce == app_choice: 
        print(f"It's a draw! we both chose {app_choice}!")
    elif(
        user_chioce == "Rock" and app_choice =="Scissors"or
        user_chioce == "Scissor" and app_choice == "Paper"or
        user_chioce == "Paper" and app_choice == "Rock"
    ):
        print(f"You won! you chose {user_chioce}and i chose {app_choice}.")   
    else:
        print(f"I won! you chose {user_chioce} and i chose {app_choice}.")
        


        
        





      

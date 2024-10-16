#This app plays "Rock,paper,scissors,game with the user"

#Initiate computer's choice
import random
# choice_list = ["Rock","Paper","Scissor"]
# app_choice = random.choice(choice_list) #app choose from the list...

#Initiate user's choice
while True:
    rounds = int(input("How many time would you like to play? Enter a number:"))
    if (rounds <2
       or rounds> 10):
      print("Enter a number between 2-10.Try again")
      continue
    else:
       print( "Welcome to the game. lets play!")
    
    for round in range(rounds):
        choice_list = ["Rock","Paper or Scissor"]
        app_choice = random.choice(choice_list) #app choose from the list...
        user_choice = input( "Rock Paper or Scissor:").capitalize()

    #Enter validation
        while user_choice not in ["Rock","Paper","Scissor: "]:
            user_choice=input("invalid Entry.Type Rock,Paper or Scissor: ").capitalize()
        #Match the entries and determine a winner
        if user_choice == app_choice:
            print(f"It is a draw! We both chose {app_choice}") 
        elif(
            user_choice == "Rock" and app_choice == "Scissors" or
            user_choice == "paper" and app_choice == "Rock" or
            user_choice == "Scissors" and app_choice == "Paper"
            ):
            print(f"You won. You chose {user_choice} and I chose{app_choice}")
    else:
        print(f"I won.I choice {app_choice} and you chose {user_choice}. ")
    play_again = input(f"You have played {rounds} games.Would you like to play again? (yes or no): ")
    if play_again == 'yes'.lower():
        continue
    else:
        print("Thanks for playing. Bye.")
        break






    















# user_chioce= input("Welcome to the game. Rock Paper or Scissors?:").capitalize()
# # Enter validation
# while user_chioce not in ["Rock","Paper","Scissor"]:
#     user_chioce = input("Invalid entry.Enter Rock, Paper or Scissor:").capitalize()

#     # compare user entry and app choice and determine winner

#     if user_chioce == app_choice: 
#         print(f"It's a draw! we both chose {app_choice}!")
#     elif(
#         user_chioce == "Rock" and app_choice =="Scissors"or
#         user_chioce == "Scissor" and app_choice == "Paper"or
#         user_chioce == "Paper" and app_choice == "Rock"
#     ):
#         print(f"You won! you chose {user_chioce}and i chose {app_choice}.")   
#     else:
#         print(f"I won! you chose {user_chioce} and i chose {app_choice}.")

        


        
        





      

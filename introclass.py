#This app askers you your name, age and tells you your age in 1year's time

#step one - Greet the user and ask thier name
print("welcome'please what is your name?")
username = input()
# step two, greet the user by name and ask for their age
print("Hello",username,"How old are you")
userage =int( input())


#step Three,tell the user thier age next year
if userage < 18:
    print(f"dear {username}you are a minor. you will be",userage+1,"years old next year")

elif userage <=30:
    print(f"Dear {username}you are a young adult.you will be",userage+1,"years old next year")

elif userage < 45:
    print(f"Dear{username}you are a middie-age.you will be",userage+1,"years old next year.")
elif userage <=75:
    print(f"Dear{username}you are agrtting old.you will be",userage+1,"years old next year")
else:
    print(f"Dear{username}you are a quite old. you will be",userage+1,"years old next year")
    
          



      



# This app displays which student is most and least social and state thier number of friends 
myclass ={}
myclass['Jhon']={'age': 19,'email':'JOhny234@gmail.com','gender':'M','Frinde':['Solomon','omolola','james']}
myclass['Rache']={'age': 29,'email':'rachagrace@gmail.com','gender':'M','Frinde':[]}
myclass['Abdullahi']={'age': 16,'email':'Babakaka4@gmail.com','gender':'M','Frinde':['Solomon','omolola','james']}
myclass['Tobi']={'age': 18,'email':'Tobi234@gmail.com','gender':'M','Frinde':['Solo','lola','james','ayo']}


# set variable for collating most or least friends
max = 100
min = 0

# looop through the dictionary

for key in myclass:
    user = myclass[key] #get each user's attributes
    friendslislist = user['friends'] # get the user's friend list
    if len(friendslislist) <max: # compare the length of the list with the integer provided
        least_social = key
        max = len(friendslislist)
    if len(friendslislist) > 0:
       most_social = key
       min = len(friendslislist)
print(f"{least_social} is the least sociable person in the class.Number of friends: {max}\n{most_social}is the most sociable person with {max} friends")



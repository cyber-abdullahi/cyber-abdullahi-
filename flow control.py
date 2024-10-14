# This app allow you to create a username, password and askes you to login with it 

# create username and password 
print("Hello user, create username:")
username = input()  
print("Awesome! now create a password")
password = input()

#login with the username and password created
print(".................................")
print("you have successfully signed up.please log in with your credentials")
print(".................................")
userlogin = input("Enter your username")
#if userlogin == username:
#   print("Nice one!")
#   userpassword = input("Enter password:")
#   if userpassword == password:
#       print("Access granted!")
#   else:
#       print("wrong password. try again")
#   else:
#       print("wrong username..try again ")

while userlogin !=username:
        print("wrong username,please try again")
        userlogin=input()
userpassword = input ("please enter your password:")
while userpassword != password:
     print("wrong password, please try again: ")   
     usrepassword = input()
print(f"Nice work,{username}.Access granted!")





 

          

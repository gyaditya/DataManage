# # Create an empty list to store the user accounts
# from data import ProgramLoop


# user_accounts = []

# while userLogin:
#     #Print the Options
#     print("Enter 'L' to log in:")
#     print("Enter 'S' to sign up:")
#     print("Enter 'E' to exit:")

#     # Get the user's choice
#     choice = input("Please Enter Your choice:\n").lower()


#     # Login
#     if choice == "l":
#         username = input("Enter your username: ")
#         password = input("Enter your password: ")

#         # Check if the username and password match any existing accounts
#         found_account = False
#         for i in range(len(user_accounts)):
#             if user_accounts[i]["username"] == username and username["password"] == password:
#                 ProgramLoop = True
#                 break
#         # If the account was found, allow the user to log in
#         if found_account:
#             print("Logged in successfully!")
#         else:
#             print("Username or password is wrong")

#     # If the user wants to create an account, add their information to the list of user accounts
#     elif choice == "c":
#         username = input("Enter a username: ")
#         password = input("Enter a password: ")

#          # Add the new account

#         found_account = False
#         for i in range(len(user_accounts)):
#             if user_accounts[i]["username"] == username:
#                 found_account = True
#             else:
#                 user_accounts.append({"username": username, "password": password, "favs": []})
        
#         if found_account:
#             print("Account Already Exists")
#             break
#         else:
#             print("Account Created")
#             ProgramLoop = True
#             break       

#     #Exit
#     elif choice == "E":
#         break


#     # If the user enters Invalid Key
#     else:
#         print("Invalid input Try Again")

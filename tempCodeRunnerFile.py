from structure import *



# def login_user():
#     email = input("Enter Email ID: ").lower()
#     password = input("Enter Password: ")
#     count = 1
#     # Check if the user exists in the logs
#     while True :
#         if email in UserLog.user_logs and  UserLog.user_logs[email] == password:
#             print("Login Successfull")
#             return False
#         else:
#             print("Invalid Email or Password")
#             count += 1



# def register_user():
#     first_name = input("Enter your First Name: ")
#     last_name = input("Enter your Last Name: ")
#     email = input("Enter your Email: ").lower()
#     location = input("Enter Your Location: ")

#     while True:
#         password = input("Enter your Password: ")
#         confirm_password = input("Confirm your Password: ")
#         if password == confirm_password:
#             break
#         else:
#             print("Passwords do not match. Please try again.")

#     # Register the user and store credentials
#     user = UserProfile(first_name=first_name, last_name=last_name, email=email, location=location)
#     UserLog(email, password)

#     print(f"User {first_name} {last_name} registered successfully!")
#     login_user()



# while True:
#     print("""
# MAIN MENU: \n
# 1 To register as new user account \n
# 2 To login to an existing user account \n
# 3 To Regieter as company 
# 4. To login as company
# 5. Update company Details

# """)
#     choice = input("Enter your choice: ")
#     if choice ==  "1":
#         register_user()
#     elif choice == "2":
#         login_user()
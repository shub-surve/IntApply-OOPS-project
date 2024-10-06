from structure import *  
from user import *
from company import *

def main():
    print("Welcome to the User Profile System!")
    
   
    UserProfile.load_profiles_from_file()
    UserLog.load_log_from_file()
    Company.load_company_data()
    
    while True:
        choice = input("Do you want to \n(1) Register as user  \n(2) Login as user? \n(3)Register as Company \n(4)Login as company \n(0)Enter 0 to exit: \nOption:- ")
        
        if choice == '1':
            registerUser()
        elif choice == '2':
            if login():
                
                email = input("Enter your email to proceed: ")
                user = find_user_by_email(email)
                if user:
                    manage_user_profile(user)
                else:
                    print("User not found.")
        elif choice == '3':
            registerCompany()
        
        elif choice == '4':
               loginCompany()
               if loginCompany():
                    email = input("Enter your email to proceed: ")
                    company = find_company_by_email(email)
                    if company:
                       manageCompanyProfile()
                    else:
                        print("Company not Found")    
        
        elif choice == '0':
            print("Exiting the system. Goodbye!"
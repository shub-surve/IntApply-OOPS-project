from structure import *  
from user import *
from company import *

def main():
    print("Welcome to the INTAPPLY!!")
   
   
    UserProfile.load_profiles_from_file()
    UserLog.load_log_from_file()
    Company.load_company_data()
    CompanyLog.load_log_from_file()
    for user in UserProfile.user_profiles:
        print(user.email)
                     
  
   

    # print(Company.company_details)
    
    while True:
        choice = input("Do you want to \n(1) Register as user  \n(2) Login as user? \n(3)Register as Company \n(4)Login as company \n(0)Enter 0 to exit: \nOption:- ")
        
        if choice == '1':
            registerUser()
        elif choice == '2':
            if login():
                email = input("Enter your email to proceed: ").lower()

                for user in UserProfile.user_profiles:
                    if user.email == email:
                        manage_user_profile(user)
                        print("Welcome back!!")
                    else:
                        print("Invalid email")

        elif choice == '3':
            registerCompany()
        
        elif choice == '4':
               if loginCompany():
                    email = input("Enter your email to proceed: ")
                    for company in Company.company_details:
                        if company.email == email:
                            manageCompanyProfile(company)
                        else:
                            print("Company not found.")
                     
        
        elif choice == '0':
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid choice. Please select again.")


if __name__ == "__main__":
    main()

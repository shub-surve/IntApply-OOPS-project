from structure import *
from verify_email import verify_email

def registerCompany():
    name = input("Enter name of the company: ")
    industry = input("Type of inductry: ")
    website = input("Company website: ")
    location = input("Location of the company: ")
    email = input("Enter Company email: ")
    desc = input("Describe  the company: ")
    passw = input("Enter Password: ")
    confirm = input("Confirm Password: ")
    if passw == confirm:
        company = Company(name, industry, website, location, email, desc)
        CompanyLog(email , passw)
        Company.save_company_to_file()
        CompanyLog.save_company_log()  
        print("Company registered successfully")
    else: 
        print("Please enter valid Email id!")

def loginCompany():
    email = input("Enter Company email: ")
    passw = input("Enter password: ")
    if CompanyLog.componyAuth(email , passw):
        print("Login successful")
      
    else:
        print("Invalid email or password")
    


def manageCompanyProfile():
    pass

def find_company_by_email(email):
    for company in Company.company_details:
        if company.email == email:
            return company
        
        return None
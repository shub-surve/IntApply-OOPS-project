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
   
    print("Login successful")
    return True
   
      


def manageCompanyProfile(company):
    print("(1)  Update Company details: ")
    print("(2) Create internships: ")
    print("(3) View company profile: ")
    print("(4) View Applications: ")
    choice = input("Enter your choice: ")
    
    if choice == '1':
        Company.updateCompanydetails(company)
        print("Company Updated Successfully")
        Company.save_company_to_file()
    elif choice == '2':
        title = input("Enter  internship title: ")
        name = input('Enter name of company')
        desc = input("Enter internship description: ")
        location = input("Enter internship location: ")
        salary = input("Enter internship salary: ") or 0
        duration = input("Enter internship duration: ")
        req = input(" Enter required skills: ").split(',')

        company.createInternship(title=title , description= desc , location=location , salary=salary , duration=duration , requirements=req , company_name=name)
        print("Internship created successfully")
        Company.save_company_to_file()



def find_company_by_email(email):
    for company in Company.company_details:
        if company.email == email:
            return company
        
        return None
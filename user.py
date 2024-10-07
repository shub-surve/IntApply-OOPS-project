from structure import *


def registerUser():
    firstname = input("Enter first name: ")
    lastname = input("Enter last name: ")
    email = input("Enter email: ").lower()
    location = input("Enter location: ")
    password = input("Enter password: ")
    confirm_password = input("Confirm password: ")

    if password == confirm_password:

        user = UserProfile(firstname, lastname, email, location)
        UserLog(email, password)
        UserProfile.save_profiles_to_file()  
        UserLog.save_log_to_file() 
        print("User registered successfully! You can now log in.")
    else:
        print("Passwords do not match. Try again.")
        return  

def login():
    count = 0
    while count < 3:
        email = input("Enter email: ").lower()
        password = input("Enter password: ")
        
        if UserLog.authenticate(email, password): 
            print("Login successful!")
            return True  
        else:
            print("Invalid email or password")
            count += 1
            if count == 3:
                print("Too many attempts. Please try later.")
                return False  

def find_user_by_email(email):
    
    for user in UserProfile.user_profiles:
        if user.email == email:
            return user
    return None

def manage_user_profile(user):
    while True:
        action = input("What would you like to do? (1) Add Education (2) Add Resume (3) Update Profile (4) View Internships: ")
        
        if action == '1':
            addEducation(user)
        elif action == '2':
            addResume(user)
        elif action == '3':
            UserProfile.updateProfile(user)
            UserProfile.save_profiles_to_file()
            UserLog.save_log_to_file()
        elif action == '4':
            fetch_internships()
        elif action == '4' :
            UserProfile.save_profiles_to_file()
            break
        else:
            print("Invalid choice. Please select again.")

def addEducation(user):
    degree = input("Enter degree: ")
    institution = input("Enter institution: ")
    start_year = input("Enter start year: ")
    end_year = input("Enter end year: ")

    user.add_education(degree, institution, start_year, end_year)
    print("Education added successfully!")

def addResume(user):
    name = input("Enter Your name: ")
    job_title = input("Enter Job Title: ")
    description = input("Enter Description: ")
    skills = input("Enter Skills (comma-separated): ").split(",")

    user.add_resume(name=name, job_title=job_title, description=description, skills=skills)
    print("Resume added successfully!")

def fetch_internships():
    try:
    
        with open("company_details.json", 'r') as file:
            companies = json.load(file)
        
        internships = []
        
       
        for company in companies:
            company_name = company.get('name')
            company_internships = company.get('internship', [])
            
            # Add internships to the list with company name and internship details
            for internship in company_internships:
                internship['name'] = company_name 
                internships.append(internship)


            for internship in internships:
                print(f"Company id :  {internship['internship_id']}")
                print(f"Company: {internship['name']}")
                print(f"Internship Title: {internship['title']}")
                print(f"Description: {internship['description']}")
                print(f"Location: {internship['location']}")
                print(f"Duration: {internship['duration']}")
                print(f"Stipend: {internship['stipend']}\n")

    except FileNotFoundError:
        print(f"File not found!")
        return []
    except json.JSONDecodeError:
        print("Error decoding JSON!")
        return []
    
   

            
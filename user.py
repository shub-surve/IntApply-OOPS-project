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
        UserProfile.save_profiles_to_file()  # Save user profiles
        UserLog.save_log_to_file()  # Save user login credentials
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
        action = input("What would you like to do? \n(1) Add Education \n(2) Add Resume \n(3) Update Profile \n(4) View available Internships \n(5) Apply for internship \n(6) View Notifications \n(7) Exit: ")
        
        if action == '1':
            addEducation(user)
        elif action == '2':
            addResume(user)
        elif action == '3':
            UserProfile.updateProfile(user)
            UserProfile.save_profiles_to_file()  # Save profile after update
            UserLog.save_log_to_file()  # Save logs after update
        elif action == '4':
            fetch_internships()
        elif action == '5':
            internship_id = int(input("Enter the ID of the internship you want to apply for: "))
            apply_for_internships(user, internship_id)
        elif action == '6':
            user.view_notifications()
        elif action == '7':
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

def fetch_internships(filename="company_details.json"):
    try:
        with open(filename, 'r') as file:
            companies = json.load(file)
        
        internships = []
        
        for company in companies:
            company_name = company.get('name')
            company_internships = company.get('internship', [])
            
            for internship in company_internships:
                internship['company_name'] = company_name 
                internships.append(internship)

        for internship in internships:
            print(f"Internship ID: {internship['internship_id']}")
            print(f"Company: {internship['company_name']}")
            print(f"Title: {internship['title']}")
            print(f"Description: {internship['description']}")
            print(f"Location: {internship['location']}")
            print(f"Duration: {internship['duration']}")
            print(f"Stipend: {internship['stipend']}\n")
        
        return internships

    except FileNotFoundError:
        print("File not found!")
        return []
    except json.JSONDecodeError:
        print("Error decoding JSON!")
        return []

def apply_for_internships(user, internship_id, filename="company_details.json"):
    """
    Apply for internships for the user!
    """
    internships = fetch_internships(filename)

    # Find the selected internship based on internship_id
    selected_internship = next(
        (internship for internship in internships if internship['internship_id'] == internship_id), 
        None
    )

    if selected_internship:
        # Check if the user has already applied for the internship
        for application in user.applications:
            if application["internship_id"] == internship_id:
                print("You have already applied for this internship!")
                return

        # Create an application
        application = {
            "internship_id": selected_internship['internship_id'],
            "title": selected_internship['title'],
            "company_name": selected_internship['company_name'],
            "status": "Pending"
        }

        # Append the application to the user's applications
        user.applications.append(application)

        # Notify the user about the application
        user.add_notification(f"Successfully applied for {selected_internship['title']} at {selected_internship['company_name']}")
        UserProfile.save_profiles_to_file()

        print(f"Applied for {selected_internship['title']} at {selected_internship['company_name']} successfully!")
    else:
        print(f"No internship found with ID: {internship_id}")

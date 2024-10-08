import json

class UserProfile:
    userid_count = 1  
    user_profiles = []  

    def __init__(self, first_name, last_name, email, location):
        self.user_id = UserProfile.userid_count
        UserProfile.userid_count += 1
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.location = location
        self.education = [] 
        self.resumes = [] 
        self.applications = []  
        self.notifications = [] 
        UserProfile.user_profiles.append(self)  

    def add_education(self, degree, institution, start_year, end_year):
        education_entry = {
            'degree': degree,
            'institution': institution,
            'start_year': start_year,
            'end_year': end_year
        }
        self.education.append(education_entry)

    def add_resume(self, name, job_title, description, skills):
        resume = {
            'Name': name,
            'job_title': job_title,
            'description': description,
            'skills': skills
        }
        self.resumes.append(resume)
        print("Resume added successfully!")

    def add_notification(self, message):
        self.notifications.append(message)

    def view_notifications(self):
        return self.notifications
    
    def updateProfile(self):
        print("Update Profile Info:-")
        newFirstName =  input(f"Enter New First Name {self.first_name}:- ").lower() or self.first_name
        newlastname = input(f"Enter  New Last Name {self.last_name}:- ").lower() or self.last_name
        newEmail = input(f"Enter New Email {self.email}:- ").lower() or self.email
        newLocation = input(f"Enter New Location {self.location}:- ").lower() or self.location

        self.first_name = newFirstName
        self.last_name = newlastname
        self.email = newEmail
        self.location = newLocation

        if newEmail !=  self.email:
            self.add_notification(f"Email updated to {newEmail}")
            UserLog.save_log_to_file()


        print("Profile Updated Successfully!!")

   

        
    

    @staticmethod
    def save_profiles_to_file(filename="user_profiles.json"):
        profiles_data = []
        for profile in UserProfile.user_profiles:
            profiles_data.append({
                'user_id': profile.user_id,
                'first_name': profile.first_name,
                'last_name': profile.last_name,
                'email': profile.email,
                'location': profile.location,
                'education': profile.education,
                'resumes': profile.resumes,
                'applications': profile.applications,
                'notifications': profile.notifications
            })
        with open(filename, 'w') as file:
            json.dump(profiles_data, file, indent=4)
        print(f"User profiles saved to {filename}")

    @staticmethod
    def load_profiles_from_file(filename="user_profiles.json"):
        try:
            with open(filename, 'r') as file:
                profiles_data = json.load(file)
                for profile_data in profiles_data:
                    
                    profile = UserProfile(
                        profile_data['first_name'],
                        profile_data['last_name'],
                        profile_data['email'],
                        profile_data['location']
                    )
                    profile.user_id = profile_data['user_id'] 
                    profile.education = profile_data['education']
                    profile.resumes = profile_data['resumes']
                    profile.applications = profile_data['applications']
                    profile.notifications = profile_data['notifications']
                print("User profiles loaded successfully!")
        except FileNotFoundError:
            print("No existing user profiles found.")


class UserLog:
    user_log = {}  

    def __init__(self, email, password):
        self.email = email
        self.__password = password
        UserLog.user_log[email] = self.__password  

    @staticmethod
    def authenticate(email, password):
        return UserLog.user_log.get(email) == password

    def changepassword (self , password):
        self.__password = password
        UserLog.user_log[self.email] = self.__password


    @staticmethod
    def save_log_to_file(filename="user_log.json"):
        with open(filename, 'w') as file:
            json.dump(UserLog.user_log, file, indent=4)
        print(f"User log saved to {filename}")

    @staticmethod
    def load_log_from_file(filename="user_log.json"):
        try:
            with open(filename, 'r') as file:
                UserLog.user_log = json.load(file)
                print("User log loaded successfully!")
        except FileNotFoundError:
            print("No existing user log found.")




class Company:
    company_details = []  
    companyId = 1  

    def __init__(self, name, industry, website, location, email, description):
        self.companyId = Company.companyId
        Company.companyId += 1
        self.name = name
        self.industry = industry
        self.website = website
        self.location = location
        self.email = email
        self.description = description
        self.internship = []
        Company.company_details.append(self)

    @staticmethod
    def save_company_to_file(filename='company_details.json'):
        company_data = []
        for company in Company.company_details:
            company_data.append({
                'companyId': company.companyId,  
                'name': company.name,
                'industry': company.industry,
                'website': company.website,
                'location': company.location,
                'email': company.email,
                'description': company.description,
                'internship': company.internship
            })
        
     
        with open(filename, 'w') as file:
            json.dump(company_data, file, indent=4)
        print(f'Company data saved to {filename}')

    @staticmethod
    def load_company_data(filename='company_details.json'):
        try:
            with open(filename, 'r') as file:
                company_data = json.load(file)
                Company.company_details.clear() 
                for data in company_data:
                    company = Company(
                        name=data["name"],
                        industry=data["industry"],
                        website=data["website"],
                        location=data["location"],
                        email=data["email"],
                        description=data["description"],
                    )
                    company.companyId = data["companyId"]  
                    company.internship = data["internship"]
                    if data["companyId"] >= Company.companyId:
                        Company.companyId = data["companyId"] + 1

                print("Company data loaded successfully!")
        except FileNotFoundError:
            print("No existing company data found.")

    def updateCompanydetails(self):
        newName =  input(f"Enter new company name {self.name}: ") or self.name
        newIndustry = input(f"Enter new industry {self.industry}: ") or self.industry

        newWebsite = input(f"Enter new website: {self.website} ") or self.website

        newLocation = input(f"Enter new location:  {self.location} ") or self.location

        newEmail = input(f"Enter new email: {self.email} ") or self.email

        newDescription = input("Enter new description: ") or self.description

        self.name = newName
        self.industry = newIndustry
        self.website = newWebsite
        self.location = newLocation
        self.email = newEmail
        self.description = newDescription


    def createInternship( self , title , company_name , duration , salary , requirements,  description , location):
        internId = 1
        enter_internship = {
            "internId" : internId ,
            'title' : title , 
            'company_name' :  company_name ,
            'duration' : duration ,
            'salary' : salary ,
            'requirements' : requirements ,
            'description' : description ,
            'location' : location
        }
        internId += 1
        self.internship.append(enter_internship)
    
    def view_all_internships(self):
        for internship in self.internship:
            return internship
        

        
        
class CompanyLog:
   
    company_log = {}

    def __init__(self , email , password):
        self.email = email
        self.__password = password

        CompanyLog.company_log[email] = self.__password

    @staticmethod
    def companyAuth(email , password):
        return CompanyLog.company_log.get(email) == password
    

    @staticmethod
    def save_company_log(filename = 'company_log.json'):
        company_log_data = []
        for email , password in CompanyLog.company_log.items():
            company_log_data.append({
                'email': email ,
                'password': password
            })
        with open(filename ,  'w') as file:
            json.dump(company_log_data , file)

    def load_log_from_file(filename = 'company_log.json'):
        try:
            with open(filename , 'r') as file:
                CompanyLog.company_log = json.load(file)
                print("User Log loaded Successfully!")
        except FileNotFoundError:
            print("No user log file found!")

    
    

        


# IntApply-OOPS-project

### User Profile & Company Management System (Terminal-based)

---

## Project Overview

This is a **terminal-based application** for managing user profiles and company details. The project allows users to **register, log in**, and manage their profiles by adding education, resumes, and applying for internships. Additionally, companies can register and manage their details in a similar manner. All data is **persisted** in JSON files, allowing the application to save and retrieve data across sessions.

---

## Features

### User Management

- **User Registration and Login:** Users can register by providing their details (first name, last name, email, location, and password) and log in using their credentials.
- **Profile Management:** After logging in, users can:
  - Add education details (degree, institution, start and end year).
  - Add multiple resumes (name, job title, description, and skills).
  - View notifications related to applications.
- **Session Persistence:** User profile data is stored in a JSON file and can be loaded during subsequent sessions.

### Company Management

- **Company Registration:** Companies can be registered by providing their name, industry, website, location, email, and description.
- **Company Data Persistence:** Company data is saved in a JSON file for easy retrieval.
- **Auto-increment Company ID:** Each company is assigned a unique, auto-incremented ID.

---

## Project Structure

- `structure.py`: This file contains the core classes and methods used in the project.
- `main.py`: This is the entry point of the application, handling user inputs and interactions with the system.
- `company_details.json`: This file stores the company information persistently.
- `user_profiles.json`: This file stores user data persistently.

---

## Classes

### 1. **UserProfile**

- **Attributes:**
  - `user_id`: Auto-incremented user ID.
  - `first_name`, `last_name`, `email`, `location`: User's personal details.
  - `education`, `resumes`, `applications`, `notifications`: Lists to store respective details.

- **Methods:**
  - `add_education`: Adds an education entry for the user.
  - `add_resume`: Adds a new resume for the user.
  - `apply_for_internship`: Simulates applying to an internship and notifies the user.
  - `add_notification`: Adds notifications for user activities.

### 2. **UserLog**

- **Attributes:**
  - `user_log`: A dictionary storing user email and password pairs for login authentication.
  
- **Methods:**
  - `authenticate`: Validates email and password during login.
  - `save_user_to_file`: Saves user profile data to `user_profiles.json`.
  - `load_user_data`: Loads user profile data from `user_profiles.json`.

### 3. **Company**

- **Attributes:**
  - `companyId`: Auto-incremented company ID.
  - `name`, `industry`, `website`, `location`, `email`, `description`: Company details.
  
- **Methods:**
  - `save_company_to_file`: Saves company details to `company_details.json`.
  - `load_company_data`: Loads company details from `company_details.json`.

---

## How to Run the Project

### Prerequisites

- **Python 3.x** installed on your system.
- Familiarity with terminal or command line interface (CLI).

### Running the Project

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/<your-username>/<repo-name>.git
   cd <repo-name>
   ```

2. **Run the Main Program:**

   ```bash
   python main.py
   ```

3. **Follow the prompts** on the terminal to register a user, log in, manage profiles, or register companies.

---

## Data Persistence

- **User Data:** Stored in `user_profiles.json`. This file contains all the registered user information, including their education, resumes, and applications.
  
- **Company Data:** Stored in `company_details.json`. This file contains details of all registered companies.

---

## Example Usage

### Register a User

```bash
Do you want to (1) Register or (2) Login? Enter 0 to exit: 1
Enter first name: John
Enter last name: Doe
Enter email: john.doe@example.com
Enter location: New York
Enter password: ****
Confirm password: ****
User registered successfully! You can now log in.
```

### Log in as a User

```bash
Do you want to (1) Register or (2) Login? Enter 0 to exit: 2
Enter email: john.doe@example.com
Enter password: ****
Login successful!
```

### Add Education and Resume

```bash
What would you like to do? (1) Add Education (2) Add Resume (3) Logout: 1
Enter degree: B.Sc. Computer Science
Enter institution: MIT
Enter start year: 2018
Enter end year: 2022
Education added successfully!

What would you like to do? (1) Add Education (2) Add Resume (3) Logout: 2
Enter Your name: John Doe
Enter Job Title: Software Developer
Enter Description: Passionate developer with experience in Python.
Enter Skills (comma-separated): Python, JavaScript, SQL
Resume added successfully!
```

### Register a Company

```bash
Enter company name: TechCorp
Enter industry: IT
Enter website: www.techcorp.com
Enter location: New York
Enter email: hr@techcorp.com
Enter description: Leading IT services provider.
Company data saved to company_details.json
```

---

## Future Enhancements

1. **User Interface Improvement:** Build a graphical user interface (GUI) for easier interaction.
2. **Database Integration:** Integrate with a SQL or NoSQL database for better data handling and performance.
3. **Security Enhancements:** Encrypt stored passwords and add more robust user authentication mechanisms.
4. **Application Tracking:** Extend the internship application system to track application status updates.

---

## Contributions

Feel free to submit pull requests, report issues, or contribute to new features. All contributions are welcome!

---

## License

This project is licensed under the MIT License.

---

## Contact

For any questions or inquiries, please reach out to:

- **Shubham Vinod Surve**
- Email: [Shubhamsurve30803@gmail.com](mailto:Shubhamsurve30803@gmail.com)

--- 

This documentation outlines the overall functionality, usage, and structure of the project. It should give any potential collaborators or users a clear understanding of how to get started and contribute.

## UPDATE 1/14/2025
#==================
age = input("What is your age? ")
job_category = input("What category of job are you interested in? (e.g., Healthcare, Technology, Education, Finance, Arts, etc.) ")
expected_income = input("What is your expected income? ")
years_ = input("How many years of experience do you have? ")

# Define job categories with specific jobs
if job_category.lower() == "healthcare":
    jobs = ["Doctor", "Nurse", "Pharmacist", "Physical Therapist", "Surgeon"]
elif job_category.lower() == "technology":
    jobs = ["Software Engineer", "Data Scientist", "Web Developer", "Network Administrator", "IT Support Specialist"]
elif job_category.lower() == "education":
    jobs = ["Teacher", "Professor", "School Counselor", "Librarian", "Special Education Teacher"]
elif job_category.lower() == "finance":
    jobs = ["Accountant", "Financial Analyst", "Investment Banker", "Financial Planner", "Auditor"]
elif job_category.lower() == "arts":
    jobs = ["Graphic Designer", "Musician", "Painter", "Photographer", "Actor"]
else:
    jobs = ["Please specify a valid category (Healthcare, Technology, Education, Finance, Arts)."]

print("You are " + age + " years old.")
print("Your desired job category is: " + job_category)
print("Some jobs in the " + job_category + " category are: " + ", ".join(jobs))
print("Your expected income is: " + expected_income)
print("You have " + years_ + " years of experience.")

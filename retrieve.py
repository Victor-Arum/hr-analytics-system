#!/usr/bin/env python
# coding: utf-8

# In[ ]:
import tui # Import tui module

# In[ ]:
# Define variables for column/list (data list) indices of different attributes
COL_GENDER = 9
COL_AGE = 4
COL_MARITAL_STATUS = 11
COL_DEPARTMENT = 7
COL_EMPLOYEE_NO = 1
COL_HOURLY_RATE = 20
COL_JOB_ROLE = 10
COL_DEPARTMENT = 7
COL_EDUCATION_LEVEL = 17
COL_TOTAL_WORKING_YEARS = 33
COL_STANDARD_HOURS = 30
COL_MONTHLY_INCOME = 24
COL_DAILY_RATE = 19
COL_PERCENT_SALARY_HIKE = 27
COL_YEARS_AT_COMPANY = 35
COL_EDUCATION_LEVEL = 17

# In[ ]:
# Function to retrieve the gender, age, marital status, and department of employees by employee number
def get_employee_details(data):
    
    # Continue prompting user until they enter a valid employee number
    while True:
        # Ask user to enter employee number to retrieve data
        employee_number = input("Please enter the employee number: ")
        tui.started(operation_name="Gathering employee data...")
        
        # Create dictionary to store the needed employee details
        employee_details = {employee_number: {}}
        
        # Flag tracking if any employee is found
        employee_found = False
        
        # Iterate over each row in the data list
        for row in data:
            # Populate employee_details dictionary with employee details if the condition is met – if employee is found
            if row[COL_EMPLOYEE_NO] == employee_number:
                employee_details[employee_number]["Gender"] = row[COL_GENDER]
                employee_details[employee_number]["Age"] = row[COL_AGE]
                employee_details[employee_number]["Marital Status"] = row[COL_MARITAL_STATUS]
                employee_details[employee_number]["Department"] = row[COL_DEPARTMENT]
                
                # Flag indicating at least one employee is found
                employee_found = True
                break
        
        # Display employee details if the employee is found
        if employee_found:
            tui.display_employee_details(employee_details)
            tui.completed()
            break # End program
            
        # Print error message if employee not found    
        else:
            msg = f"No records found for employee with employee number: {employee_number}. Please try again"
            tui.error(msg)
            
# In[ ]:
# Function to create a set and add new items to it so that they're unique
def create_lists(list_of_items, column):
    list_of_items.add(column)
    return list_of_items

# In[ ]:
# Function to retrieve information about a particular job role
def get_job_info(data):
    
    # Continue prompting user to enter a job role until a valid one is entered
    while True:
        job_role = input("Kindly enter the job role: ")
        tui.started(operation_name=f"Gathering data about the job role, {job_role}...")
        
        # Create empty sets to store unique department names, education levels, total working years, and standard hours
        department_list = set()
        education_level_list = set()
        total_working_years_list = set()
        standard_hours_list = set()
        
        # Create job_info dictionary to store information about job role
        job_info = {}
        
        # Flag tracking if a job is found
        job_found = False
        
        # Iterate over each row of data and select rows matching the user-selected job role
        for row in data:
            if row[COL_JOB_ROLE] == job_role:
                # Add department name, education level, working years, and standard hours to their respective sets
                create_lists(department_list, row[COL_DEPARTMENT])
                create_lists(education_level_list, row[COL_EDUCATION_LEVEL])
                create_lists(total_working_years_list, row[COL_TOTAL_WORKING_YEARS])
                create_lists(standard_hours_list, row[COL_STANDARD_HOURS])
                
                # Store the created sets in a dictionary
                job_info[job_role] = {
                    "Department(s)": department_list,
                    "Education Level(s)": education_level_list,
                    "Total Working Year(s)": total_working_years_list,
                    "Standard Hours": standard_hours_list
                }
                
                # Flag indicating at least one job is found
                job_found = True
    
        # Display the job information if job found. If not found, show an error message
        if job_found:
            tui.display_job_info(job_role, job_info)
            tui.completed()
            break # End program
            
        else:
            msg = f"Job role, {job_role}, not found in our HR database."
            tui.error(msg)

# In[ ]:
# Function to retrieve specific data for employees working under 60 hours
def get_under_60_hours_employee_info(data):
    
    # Continue asking for user input until a valid department is entered
    while True:
        # Prompt user to enter a department
        department = input("Kindly enter the department: ")
        tui.started(operation_name=f"Gathering requested data...")
        
        # Create a list of dictionaries to store employee details for individuals working under 60 hours
        under_60_hours_employee_details = [{}]
        # Flag tracking if any employee working under 60 hours is found
        under_60_hours_employee_found = False
        
        # Iterate over each row in the data list
        for row in data:
            
            # Extract the row of standard hours and convert to integer
            standard_hours = int(row[COL_STANDARD_HOURS])
            # Check if the employee works under 60 hours
            under_60_hours_employees = standard_hours < 60
            
            # If employee works under 60 hours and belongs in the user-selected department
            if under_60_hours_employees and department in row[COL_DEPARTMENT]:
                
                # Add employee details to the list of dictionaries named under_60_hours_employee_details
                under_60_hours_employee_details.append({
                    "Employee Number": row[COL_EMPLOYEE_NO],
                    "Job Role": row[COL_JOB_ROLE],
                    "Marital Status": row[COL_MARITAL_STATUS],
                    "Hourly Rate": row[COL_HOURLY_RATE]
                })
                # Flag indicating at least one employee working under 60 hours has been found
                under_60_hours_employee_found = True
            
        # If at least one employee is found, display their details
        if under_60_hours_employee_found:
            tui.display_under_60_hours_employee_info(under_60_hours_employee_details, department)
            tui.completed()
            break # End program
            
        # If employee working under 60 hours is not found, display the error message
        else:
            msg = f"No record of employee working below 60 hours in {department} department"
            tui.error(msg)

# In[ ]:
# Function to gather salary information for employees hired in the past decade
def get_salary_info_last_10_years(data):
    # Loop until user enters a valid education level
    while True:
        # Prompt user to enter an education level
        education_level = input("Please, enter the education level: ")
        tui.started(operation_name=f"Processing the salary information of recent hires...")
        
        # Create a list of dictionaries to store salary details and job roles
        last_10_years_salary_details = [{}]
        # Flag tracking if any employee with the user-selected education level is found
        education_level_found = False
        
        # Iterate over each row in the data list
        for row in data:
            
            # Extract the row comprising the years at company and convert to integer
            years_at_company = int(row[COL_YEARS_AT_COMPANY])
            # Check if the employee joined the company in the last 10 years
            last_10_years_employees = years_at_company <= 10
            
            # If employee joined in the last decade and holds a degree matching the user-selected education level
            if last_10_years_employees and education_level in row[COL_EDUCATION_LEVEL]:
                # Add the employee's salary details to the list named last_10_years_salary_details
                last_10_years_salary_details.append({
                    "Job Role": row[COL_JOB_ROLE],
                    "Monthly Income": row[COL_MONTHLY_INCOME],
                    "Daily Rate": row[COL_DAILY_RATE],
                    "Percentage Salary Hike": row[COL_PERCENT_SALARY_HIKE]
                })
                # Flag indicating that at least one employee has been found
                education_level_found = True
                
        # If any employee(s) is found, print out their salary detail and job role
        if education_level_found:
            tui.display_salary_info_last_10_years(last_10_years_salary_details, education_level)
            tui.completed()
            break # End program
            
        # If employee not found, display an error message
        else:
            msg = f"No record of employee with the education level, {education_level}, joining the company in the last decade"
            tui.error(msg)
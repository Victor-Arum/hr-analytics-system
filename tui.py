#!/usr/bin/env python
# coding: utf-8

# In[ ]:
from tabulate import tabulate

# Define a line width for the purpose of formatting
line_width = 115


# In[ ]:
# Function to print a welcome message with an extra optional message
def welcome():
    # Use ASCII characters to design my welcome message
    print("╔" + "═" * (line_width - 5) + "╗") # Print lines to form a top border
    print("║" + " " * (line_width - 5) + "║") # Empty spaces within the rectange
    print("║" + "WELCOME TO THE HR DESK!".center(line_width - 5) + "║") # Text centered in the rectangle
    print("║" + " " * (line_width - 5) + "║") # Empty spaces again
    print("╚" + "═" * (line_width - 5) + "╝") # Print lines to form a bottom border

# In[ ]:
# Function to display a message saying that an operation has started
def started(operation_name=""):
    print("*" * line_width) # Print line of dashes for formatting
    print(f"Operation started: {operation_name}\n") # Print a message denoting start of an operation with an optional user input


# In[ ]:
# Function to indicate that an operation has been completed
def completed():
    print("\nOperation completed.") # Print completion message
    print("*" * line_width) # Print line of dashes for formatting

# In[ ]:
# Function to print error message
def error(msg = ''):
    print(f"Invalid Selection! {msg}")
    
# In[ ]:
# Function to display the main menu
def main_menu():
    
    # Print out the options in the sub-menu
    print("Want to explore and delve deep into our HR records? Please select an option to proceed:")
    print("""
    [1]          Retrieve data regarding our employees and job roles
    [2]          Analyse our employee data and generate insights
    [3]          Use charts to visualize our employee data
    [exit]       Exit the program
    """)
    
    # Get user input for the main menu
    main_selection = input()
    
    return main_selection # Return user selection

# In[ ]:
# Function to display the retrieve sub-menu
def sub_menu_retrieve():
    
    # Print out the options in the sub-menu
    print("Enter an option of your choice:")
    print("""
    [1]          Get an employee's personal details based on their employee number
    [2]          Retrieve information about specific job roles
    [3]          Fetch information of employees working below 60 hours by department
    [4]          Retrieve the job role and salary info of last-decade hires by education level
    [menu]       Return to the main menu
    [exit]       Exit the program
    """)
    
    # Get user input for the retrieve sub-menu
    retrieve_selection = input()
    
    return retrieve_selection # Return user selection

# In[ ]:
# Function to display the analyse sub-menu
def sub_menu_analyse():
    
    # Print out the options in the sub-menu
    print("Enter an option of your choice:")
    print("""
    [1]          Identify the top 3 job roles with most hires based on education level
    [2]          Analyse employees' average monthly rate based on education level
    [3]          Analyse the average duration of employment for employees in a department
    [4]          Discover the top 10 earners' gender and department for a particular education level
    [menu]       Return to the main menu
    [exit]       Exit the program
    """)
    
    # Get user input for the analyse sub-menu
    analyse_selection = input()
    
    return analyse_selection # Return user selection

# In[ ]:
# Function to display the visualise sub-menu
def sub_menu_visualise():
    
    # Print out the options in the sub-menu
    print("Enter an option of your choice:")
    print("""
    [1]          The proportion of employees in the company based on their education levels
    [2]          The frequency of employee training in each education field
    [3]          How job satisfaction scores change across job levels for each department
    [4]          The average salary of employees in each job role
    [menu]       Return to the main menu
    [exit]       Exit the program
    """)
    
    # Get user input for the visualise sub-menu
    visualise_selection = input()
    
    return visualise_selection # Return user selection

# In[ ]:
# Function to display employee personal details based on their employee number
def display_employee_details(employee_details):
    
    # Run a loop over each employee number and their information
    for employee_number, info in employee_details.items():
        
        # Print a header message with the user-selected employee number
        print(f"Employee Personal Details for Employee Number: {employee_number}")
        print("=" * line_width)  # Print a separator line
        
        # Loop over each attribute and its value for each employee
        for attribute, value in info.items():
            print(f"{attribute}: {value}") # Print each attribute and its value
        print("=" * line_width) # Print another separator line
            
# In[ ]
# Function to display specific information about a particular job role
def display_job_info(job_role, job_info):
    
    # Print a header message with the user-selected job role
    print(f"Displaying information specific to the job role, {job_role}:")
    
    # Retrieve the attributes and values for the job roles
    attributes = job_info[job_role]
    rows = []
    
    # Iterate over each key and values in the attributes variable
    for key, values in attributes.items():
        # Convert each value into a string and joins them if multiple values
        rows.append([key, "\n".join(map(str, values))])
    
    # Print the job info in a nice format using tabulate
    print(tabulate(rows, headers=["Attribute", "Values"], tablefmt="grid"))

# In[ ]
# Function to display data of employees working less than 60 hours based on department
def display_under_60_hours_employee_info(under_60_hours_employee_details, department):
    
    # Print a header message with the user-selected department
    print(f"Displaying employee details for individuals working below 60 standard hours in {department} department:")
    
    # Create columns/headers for use in tabulate() function
    headers = ["Employee Number", "Job Role", "Marital Status", "Hourly Rate"]
    
    # Create an empty list to store rows of employee data
    rows = []
    
    # Iterate over each employee in the list of dictionary named under_60_hours_employee_details
    for employee in under_60_hours_employee_details[1:]:
        # Retrieve needed data from the list; each row representing each employee details
        row = [employee["Employee Number"], employee["Job Role"], employee["Marital Status"], employee["Hourly Rate"]]
        rows.append(row)
    
    # Print the specific employee details in a nice format using tabulate
    print(tabulate(rows, headers=headers, tablefmt="grid"))
     
# In[ ]:
# Function to display salary information for the last decade by education level
def display_salary_info_last_10_years(last_10_years_salary_details, education_level):
    
    # Print a header message with the user-selected education level
    print(f"Displaying the salary details of employees with the education level, {education_level}, who joined the company in the last decade:")
    
    # Create headers for use in tabluate() function
    headers = ["Job Role", "Monthly Income", "Daily Rate", "Percentage Salary Hike"]
    
    # Create an empty list to store rows of employee job role, income, rate, and % hike
    rows = []
    
    # Loop over each employee in the list of dictionary named last_10_years_salary_details
    for employee in last_10_years_salary_details[1:]:
        # Retrieve each needed employee data in rows and store in variable 'row'
        row = [employee["Job Role"], employee["Monthly Income"], employee["Daily Rate"], employee["Percentage Salary Hike"]]
        rows.append(row)
    
    # Print the employee data in a tabular format
    print(tabulate(rows, headers=headers, tablefmt="grid"))
        
# In[ ]:
# Function to display the top 3 job roles with the most hires based on education level
def display_top_3_job_roles(top_3_job_roles, educational_level):
    
    # Print a header message with the user-selected education level
    print(f"Displaying the top 3 job roles with the most employees with educational level, {educational_level}:\n")
    
    # Create headers for the tabulate() table
    headers = ["Job Role", "Number of Employees"]
    
    # Print the top 3 job roles in a tabular format
    print(tabulate(top_3_job_roles, headers=headers, tablefmt="grid", showindex=False)) # showindex to remove the index
    
# In[ ]:
# Function to display employees' average monthly rate based on education level
def display_average_monthly_rate(educational_level, average_monthly_rate):
    
    # Format the monthly rate by adding the dollar sign ($) and approximating to two decimal places
    formatted_rate = f"${average_monthly_rate:.2f}"
    
    # Print the formatted monthly rate
    print(f"\nThe average monthly rate of employees with education level '{educational_level}' is {formatted_rate}.")
    
# In[ ]:
# Function to display the employees' average duration of employment in a specific department
def display_average_employment_duration(average_employment_duration, department):
    
    # Format the years to two decimal places
    formatted_years = f"{average_employment_duration:.2f} years"
    
    # Print the formatted years
    print(f"\nThe average duration of employment for employees in {department} department is {formatted_years}.")
    
# In[ ]:
# Function to display the top 10 earners' department and gender based on education level
def display_top_10_earners(education_input, complete_data):
    print(f"\nDisplaying the department and gender of the top 10 earners with the education level: '{education_input}':\n")
    
    # Create headers for the tabulate() table
    headers = ["Department", "Gender", "Monthly Income"]
    
    # Print the top 10 earners' department and gender in a tabular format
    print(tabulate(complete_data, headers=headers, tablefmt="grid", showindex=False))
#!/usr/bin/env python
# coding: utf-8

# In[ ]:
import pandas as pd
import tui

# In[ ]:
# Function to compute the top 3 job roles with the most hires based on education level
def compute_top_3_job_roles(data):
    while True:
        # Ask user to enter an education level
        educational_level = input("Please, enter the education level: ")
    
        # Print message stating that the analysis operation has started
        tui.started(operation_name=f"Analysing the job roles with the most hires based on the education level: {educational_level}...")
    
        # Filter data based on the user-selected education level
        filtered_data = data[data['Education_level'] == educational_level]
        
        # Check to see whether the filtered data contains any value/item
        if len(filtered_data) == 0:
            # If the filtered data is empty, print the error message
            msg = f"No record found for the education level: {educational_level}."
            tui.error(msg)
            continue # Prompt user to enter education level again
    
        # Group the filtered data by education level and job role
        grouped_data = filtered_data.groupby(['Education_level', 'Job_Role'])
    
        # Calculate the number of employees for each job role and create a new column for this attribute
        employee_count_by_education = grouped_data.size().reset_index(name='Number_of_employees')
    
        # Sort the data in descending order of the number of employees
        sorted_data = employee_count_by_education.sort_values(by=['Education_level', 'Number_of_employees'], ascending=[True, False])
    
        # Retrieve the top 3 job roles with the highest number of hires
        top_job_roles = sorted_data[['Job_Role', 'Number_of_employees']]
        top_3_job_roles = top_job_roles.head(3)
    
        # Display the top 3 job roles with the most hires
        tui.display_top_3_job_roles(top_3_job_roles, educational_level)
    
        # Print a message stating that the operation is complete
        tui.completed()
        break # Exit the loop if completed without errors
    
# In[ ]:
# Function to compute the average monthly rate of employees by education level
def compute_average_monthly_rate(data):
    while True:
        # Ask user to enter the education level to analyse
        educational_level = input("Please, enter the education level to analyse: ")
    
        # Print message stating that the operation has started
        tui.started(operation_name=f"Computing the average monthly rate of employees with education level: {educational_level}...")
    
        # Filter the rows where the education level matches the user-selected one
        filtered_data = data[data['Education_level'] == educational_level]
        
        # Check to see whether the filtered data contains any value/item
        if len(filtered_data) == 0:
            # If the filtered data is empty, print the error message
            msg = f"No record found for the education level: {educational_level}."
            tui.error(msg)
            continue # Prompt user to enter education level again
    
        # Calculate the mean of the monthly rate of employees with the user-specified education level
        average_monthly_rate = filtered_data['Monthly_Rate'].mean()
    
        # Print a message stating the calculated average monthly income
        tui.display_average_monthly_rate(educational_level, average_monthly_rate)
    
        # Print statement marking the completion of the operation
        tui.completed()
        break # Exit the program if successfully completed
    
# In[ ]:
# Function to calculate the average employment duration of specified departments
def compute_average_employment_duration(data):
    while True:
        # Prompt user to enter the department name
        department = input("Please, enter the department name: ")
    
        # Print message stating that the operation has started
        tui.started(operation_name=f"Computing the average duration of employment for employees in {department} department...")
    
        # Filter the rows where the department matches the user-selected one
        filtered_data = data[data['Department'] == department]
        
        # Check to see whether the filtered data contains any value/item
        if len(filtered_data) == 0:
            # If the filtered data is empty, print the error message
            msg = f"No record found for the department: {department}."
            tui.error(msg)
            continue # Prompt user to enter the department name again
    
        # Calculate the mean of the years that employees in the user-specified department have spent at the company
        average_employment_duration = filtered_data['Years_At_Company'].mean()
    
        # Print a message stating the calculated average employment duration
        tui.display_average_employment_duration(average_employment_duration, department)
    
        # Print statement marking the completion of the operation
        tui.completed()
        break # Exit the program if successfully completed
    
# In[ ]:
# Function to compute the top 10 earners of a particular education level by gender and department
def compute_top_10_earners(data):
    while True:
        # Prompt user to enter the education level
        education_input = input("""Enter the education level: """)
    
        # Print message saying that the operation has started
        operation_name = f"Sorting the top company earners with education level, {education_input}, by gender and department..."
        tui.started(operation_name)
    
        # Filter data based on the user-selected education level
        filtered_data = data[data['Education_level'] == education_input]
        
        # Check to see whether the filtered data contains any value/item
        if len(filtered_data) == 0:
            # If the filtered data is empty, print the error message
            msg = f"No record found for the education level: {education_input}."
            tui.error(msg)
            continue # Prompt user to enter education level again
    
        # Sort the filtered data by Monthly Income in descending order
        sorted_data = filtered_data.sort_values(by='Monthly_Income', ascending = False)
    
        # Extract the top 10 entries, who are the top 10 earners
        top_earners = sorted_data.head(10)
    
        # Retrieve the department, gender, and monthly income of these top 10 earners and remove the indices
        complete_data = top_earners[['Department', 'Gender', 'Monthly_Income']].reset_index(drop=True)
    
        # Display the top 10 earners and their details
        tui.display_top_10_earners(education_input, complete_data)
    
        # Print statement marking the completion of the operation
        tui.completed()
        break # End program if program runs well
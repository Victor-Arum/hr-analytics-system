#!/usr/bin/env python
# coding: utf-8

# In[ ]:
import matplotlib.pyplot as plt
import pandas as pd

# In[ ]:
# Function to display the proportion of company employees by their education level using a pie chart
def show_employee_proportion_by_education_levels(data):
    
    # Group the employees by their education level
    group_employees = data.groupby('Education_level')
    
    # Compute the number of employees in each education level
    employee_data = group_employees.size()
    
    # Retrieve and store each education level and their corresponding number of employees
    education_levels = employee_data.index.tolist()
    number_of_employees = employee_data.tolist()
    
    # Create a new figure
    fig = plt.figure(figsize=(10,6))

    # Plot a pie chart
    plt.pie(number_of_employees,labels=education_levels, autopct='%1.1f%%')

    # Set a title and legend
    plt.title("Pie Chart Showing the Proportion Of Employees Based On Their Education Levels")
    plt.legend(loc='upper right',bbox_to_anchor=(1.6,1))

    # Show the chart
    plt.show()
    
# In[ ]:
# Function to compare the frequency of employee training in each education field using a bar chart
def compare_training_frequency_by_education_field(data):
    
    # Group education field and training frequency
    grouped_data = data.groupby('Education_Field')['Training_Times_Last_Year'].size()
    
    # Retrieve and store the education fields and corresponding training frequency 
    education_field = grouped_data.index.tolist()
    training_frequency = grouped_data.tolist()
    
    # Create a new figure
    fig = plt.figure(figsize=(15,8)) 
    
    # Plot a bar chart
    plt.bar(education_field,training_frequency, width=0.5)
    
    # Set the labels for x and y axis
    plt.xlabel("Education Field", fontsize=14)
    plt.ylabel("Training Frequency", fontsize=14)
    
    # Set the title
    plt.title("A Bar Chart Showing The Frequency Of Employee Training In Each Education Field", fontsize=16)
    
    # Show the bar chart
    plt.show()
    
# In[ ]:
# Function to show how job satisfaction scores change across different job levels for each department
def show_job_satisfaction_by_job_level_and_department(data):
    
    # Group data by Department and Job Level, then calculate the mean of job satisfaction
    grouped_data = data.groupby(['Department', 'Job_Level'], as_index=False)['Job_Satisfaction'].mean()

    # Get unique department names and retrieve as a list
    departments = grouped_data['Department'].unique().tolist()
    
    # Extract job levels and job satisfaction scores into separate lists
    job_level = grouped_data['Job_Level'].tolist()
    job_satisfaction = grouped_data['Job_Satisfaction'].tolist()
    
    # Create job levels lists for each department
    hr_job_level = [job_level[0], job_level[1], job_level[2], job_level[3], job_level[4]]
    rd_job_level = [job_level[5], job_level[6], job_level[7], job_level[8], job_level[9]]
    sales_job_level = [job_level[10], job_level[11], job_level[12], job_level[13], job_level[14]]
    
    # Create job satisfaction scores lists for each department
    hr_job_satisfaction = [job_satisfaction[0], job_satisfaction[1], job_satisfaction[2], job_satisfaction[3], job_satisfaction[4]]
    rd_job_satisfaction = [job_satisfaction[5], job_satisfaction[6], job_satisfaction[7], job_satisfaction[8], job_satisfaction[9]]
    sales_job_satisfaction = [job_satisfaction[10], job_satisfaction[11], job_satisfaction[12], job_satisfaction[13], job_satisfaction[14]]

    # Create a new figure
    fig = plt.figure(figsize=(15,8))
    
    # Plot job satisfaction scores for HR department
    plt.plot(hr_job_level, hr_job_satisfaction, 'r--', marker='o', label="HR")

    # Plot job satisfaction scores for R&D department
    plt.plot(rd_job_level, rd_job_satisfaction, 'b:', marker='o', label="R&D")

    # Plot job satisfaction scores for Sales department
    plt.plot(sales_job_level, sales_job_satisfaction, 'g-', marker='o', label="Sales")
    
    # Set labels and title
    plt.xlabel('Job Level', fontsize=14)
    plt.ylabel('Job Satisfaction', fontsize=14)
    plt.title('How Job Satisfaction Scores Change Across Different Job Levels for Each Department', fontsize=16)
    
    # Show legend
    plt.legend()
    
    # Show the line plot
    plt.show()
    
# In[ ]:
# Function to show the average salary of each job role in the company using a bar chart
def show_average_salary_by_job_role(data):
    
    # Calculate the average salary of each job role
    average_salary_by_job_role = data.groupby('Job_Role')['Monthly_Income'].mean()
    
    # Retrieve and store the job roles and corresponding monthly incomes
    job_role = average_salary_by_job_role.index.tolist()
    monthly_income = average_salary_by_job_role.tolist()
    
    # Create a new figure
    fig = plt.figure(figsize=(15,8)) 
    
    # Plot a bar chart
    plt.bar(job_role,monthly_income, width=0.4)
    
    # Set x and y labels and title
    plt.xlabel("Job Roles", fontsize=14)
    plt.ylabel("Monthly Income", fontsize=14)
    plt.title("A Bar Chart Showing The Average Salary Of Employees In Each Job Role", fontsize=16)
    
    # Rotate x axis  labels so that one can read them better
    plt.xticks(rotation=45)
    
    # Show the bar chart
    plt.show()    
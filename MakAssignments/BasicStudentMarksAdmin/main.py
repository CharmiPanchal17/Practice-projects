import pandas as pd
import os

def addStudentInfo():

    csv_filename = "StudentData.csv"
    if not os.path.exists(csv_filename):
        df = pd.DataFrame(columns=['AdminNo.', 'Name', 'Math', 'English', 'SST'])

        df.to_csv(csv_filename, index=False)

    number_of_students = int(input("How many students'information do you want to add?: "))

    for i in range(number_of_students):
        student_admin_no = input(f"Enter the admin number of student {i+1}: ")
        name = input(f"Enter the name of student {i+1}: ")
        math = int(input(f"Enter the math score of student {i+1}: "))
        english = int(input(f"Enter the English score of student {i+1}: "))
        sst = int(input(f"Enter the SST score of student {i+1}: "))
        
        data = pd.DataFrame({      #for creating a dataframe from the user input
            'AdminNo.': [student_admin_no], 
            'Name': [name], 
            'Math': [math], 
            'English': [english], 
            'SST': [sst]
        })

        data.to_csv(csv_filename, mode='a', header=False, index=False )

addStudentInfo()
import os
import statistics

your_reg_number = '24/X/21516/PS' #update your registration number
your_name = 'PANCHAL CHARMI' #update your name

def print_menu():
    print("--------------------MENU--------------------")
    print("1 - Add student with marks")
    print("2 - Delete student, given an admin_no")
    print("3 - View statistics about the grades")
    print("4 - View student grades")
    print("5 - Edit student grades")
    print("6 - Print Gradebook")
    print("m - Print menu")
    print("c - Clear Screen")
    print("q - Quit system\n")

print()
print(f"Welcome to students Gradebook\nBy".upper())
print(f"{your_name} - {your_reg_number}\n")

#Print menu for first time
print_menu()

#initialize the gradebook
grade_book = dict()

while True:
    choice = input("\n----------------------------\nEnter your choice from the menu: ")

    if choice == '1':
        admin_no = int(input("Enter the admin number of the student to add: "))
        if admin_no not in grade_book:
            name = input("Enter the name of the student: \n")

            try:
                Math = int(input("Enter the marks got in math: "))
                if Math < 0 or Math > 100:
                    print("Please enter marks between 0 and 100\n")
                    Math = int(input("Enter the marks got in math: "))

            except ValueError:
                while True:
                    try:
                        Math = int(input("Enter the marks got in math: "))
                        if 0 <= Math <= 100:
                            break
                        else:
                            print("Please enter marks between 0 and 100\n")

                    except ValueError:
                        print("Please enter a valid integer.\n")
                        
            try:
                SST = int(input("Enter the marks got in SST: "))
                if SST < 0 or SST > 100:
                    print("Please enter marks between 0 and 100\n")
                    SST = int(input("Enter the marks got in SST: "))

            except ValueError:
                while True:
                    try:
                        SST = int(input("Enter the marks got in SST: "))
                        if 0 <= SST <= 100:
                            break
                        else:
                            print("Please enter marks between 0 and 100\n")

                    except ValueError:
                        print("Please enter a valid integer.\n")

            try:
                Science = int(input("Enter the marks got in Science: "))
                if Science < 0 or Science > 100:
                    print("Please enter marks between 0 and 100\n")
                    Science = int(input("Enter the marks got in Science: "))

            except ValueError:
                while True:
                    try:
                        Science = int(input("Enter the marks got in Science: "))
                        if 0 <= Science <= 100:
                            break
                        else:
                            print("Please enter marks between 0 and 100\n")

                    except ValueError:
                        print("Please enter a valid integer.\n")

            try:
                English = int(input("Enter the marks got in English: "))
                if Math < 0 or Math > 100:
                    print("Please enter marks between 0 and 100\n")
                    English = int(input("Enter the marks got in English: "))

            except ValueError:
                while True:
                    try:
                        English = int(input("Enter the marks got in English: "))
                        if 0 <= English <= 100:
                            break
                        else:
                            print("Please enter marks between 0 and 100\n")

                    except ValueError:
                        print("Please enter a valid integer.\n")
            
            grade_book[admin_no] = {
            'name': name, 
            'Math': Math, 
            'SST': SST, 
            'Science': Science,
            'English': English
            }

            print(f"Student: '{name}' has been added.\n") #Include details for added student and current number of students in grade book.
        else:
            print(f"Student with admin number '{admin_no}' already exists.\n")

    elif choice == '2':
        #Code to delete a student. Teacher/User admin_no for student to delete
        admin_no = int(input("Enter the admin number of the student to delete: "))

        if admin_no in grade_book:
            del grade_book[admin_no]
            print(f"Student with admin_no {admin_no} deleted.")
        else:
            print(f"Student with admin_no {admin_no} not found in the gradebook.")
    
    
    elif choice == '3':
        if len(grade_book) == 0:
            print("No students found in gradebook.")
            continue
        else:
            math_marks = [details['Math'] for details in  grade_book.values()]  #list comprehension. It iterates over every gradebook
            sst_marks = [details['SST'] for details in  grade_book.values()]
            science_marks = [details['Science'] for details in  grade_book.values()]
            english_marks = [details['English'] for details in  grade_book.values()]

            
            def SubjectStatistics(subject, marks):
                print(f"---Statistics for {subject}---")
                print(f"Mean marks for {subject}: {statistics.mean(marks)}")

                try:
                    print(f"Mode marks for {subject}: {statistics.mode(marks)}")
                    modal_frequency = marks.count(statistics.mode(marks))
                    print(f"Modal frequency for {subject}: {modal_frequency}")

                except statistics.StatisticsError:
                    print(f"No mode found for {subject}.")

                print(f"Lowest mark for {subject}: {min(marks)}")
                print(f"Highest mark for {subject}: {max(marks)}\n")

            #outputing
            SubjectStatistics("Maths", math_marks)
            SubjectStatistics("SST", sst_marks)
            SubjectStatistics("Science", science_marks)
            SubjectStatistics("English", english_marks)

    elif choice == '4':
        admin_no = int(input("Enter the admin number of the student to view: "))
        if admin_no in grade_book:
            print(f"Student name: {grade_book[admin_no]['name']}")
            print(f"Math: {grade_book[admin_no]['Math']}\nSST: {grade_book[admin_no]['SST']}\nScience: {grade_book[admin_no]['Science']}\nEnglish: {grade_book[admin_no]['English']}")
        else:
            print(f"Student with admin_no '{admin_no}' not found.")

    elif choice == '5':
        admin_no = int(input("Enter the admin number of the student to edit: "))

        if admin_no in grade_book:
            Math = int(input("Enter the new math marks: "))
            SST = int(input("Enter the new SST marks: "))
            Science = int(input("Enter the new Science marks: "))
            English = int(input("Enter the new English marks: "))

            grade_book[admin_no] = {
                'name': grade_book[admin_no]['name'],
                'Math': Math,
                'SST': SST,
                'Science': Science,
                'English': English
            }
            print(f"Student with admin number '{admin_no}' has been edited.")
        else:
            print(f"Student with admin_no '{admin_no}' not found.")

    elif choice == '6':
        print("Gradebook of students with detail score details:")
        print(f"Current gradebook has {grade_book.keys().__len__()} students.\n")  #for counting the students in the gradebook
        for admin_no, details in grade_book.items():
            print(f"{admin_no}: {details}")
    
    elif choice == 'm':
        print_menu()   
    elif choice == 'c':
        os.system('cls') #Only for windows       
    elif choice == 'q':
        print('Bye bye')
        break



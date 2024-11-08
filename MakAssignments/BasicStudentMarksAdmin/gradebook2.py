import os
import statistics
from abc import ABC, abstractmethod

grade_book = dict()

class GradeBook(ABC):
    def __init__(self):
        self.__grades = {}

    @abstractmethod
    def add_student(self):
        pass

    @abstractmethod
    def delete_student(self):
        pass

    @abstractmethod
    def view_statistics(self):
        pass

    @abstractmethod
    def view_student(self):
        pass

    @abstractmethod
    def edit_student(self):
        pass

    @abstractmethod
    def view_gradebook(self):
        pass
    

class TeacherView(GradeBook):
    def __init__(self, staff_id, teacher_name):
        super().__init__()
        self.staff_id = staff_id
        self.teacher_name = teacher_name

    def add_student(self):
        try:
            admin_no = int(input("Enter the admin number of the student to add: "))
            if admin_no not in grade_book:
                student_name = input("Enter the name of the student: \n")
                Math = self.get_marks("Math")
                SST = self.get_marks("SST")
                Science = self.get_marks("Science")
                English = self.get_marks("English")

                grade_book[admin_no] = {
                    'name': student_name,
                    'Math': Math,
                    'SST': SST,
                    'Science': Science,
                    'English': English
                }
                print(f"Student: '{student_name}' has been added.")
            else:
                print(f"Student with admin number '{admin_no}' already exists.")
        except ValueError:
            print("Invalid input.")

    def get_marks(self, subject):
        while True:
            try:
                mark = int(input(f"Enter the marks for {subject} (0-100): "))
                if 0 <= mark <= 100:
                    return mark
                else:
                    print("Marks must be between 0 and 100.")
            except ValueError:
                print("Please enter a valid integer.")

    def delete_student(admin_no):
        admin_no = int(input("Enter the admin number of the student to delete: "))

        if admin_no in grade_book:
            del grade_book[admin_no]
            print(f"Student with admin_no {admin_no} deleted.")
        else:
            print(f"Student with admin_no {admin_no} not found in the gradebook.")
    
    def view_statistics(self):
        if len(grade_book) == 0:
            print("No students found in gradebook.")
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

    def view_student(admin_no):
        admin_no = int(input("Enter the admin number of the student to view: "))
        if admin_no in grade_book:
            print(f"Below are the details of the student with Admin_no: {admin_no}\nStudent name: {grade_book[admin_no]['name']}")
            print(f"Math: {grade_book[admin_no]['Math']}\nSST: {grade_book[admin_no]['SST']}\nScience: {grade_book[admin_no]['Science']}\nEnglish: {grade_book[admin_no]['English']}")
        else:
            print(f"Student with admin_no '{admin_no}' not found.")

    def edit_student(admin_no):
        try:
            admin_no = int(input("Enter the admin number of the student to edit: "))
            if admin_no in grade_book:
                Math = self.get_marks("Math")
                SST = self.get_marks("SST")
                Science = self.get_marks("Science")
                English = self.get_marks("English")

                grade_book[admin_no].update({"Math": Math, "SST": SST, "Science": Science, "English": English})
                print(f"Student with admin number '{admin_no}' has been edited.")
            else:
                print(f"Student with admin_no '{admin_no}' not found.")
        except ValueError:
            print("Invalid input.")


    def view_gradebook(self):
        print("Gradebook of students with detail score details:")
        print(f"Current gradebook has {grade_book.keys().__len__()} students.\n")  #for counting the students in the gradebook
        for admin_no, details in grade_book.items():
            print(f"{admin_no}: {details}")

    def teacher_menu(self):
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

class StudentView(GradeBook):
    def __init__(self, student_id, student_name):
        super().__init__()
        self.student_id = student_id
        self.student_name = student_name

    def view_student(admin_no):
        admin_no = int(input("Enter the admin number of the student to view: "))
        if admin_no in grade_book:
            print(f"Below are the details of the student with Admin_no: {admin_no}\nStudent name: {grade_book[admin_no]['name']}")
            print(f"Math: {grade_book[admin_no]['Math']}\nSST: {grade_book[admin_no]['SST']}\nScience: {grade_book[admin_no]['Science']}\nEnglish: {grade_book[admin_no]['English']}")
        else:
            print(f"Student with admin_no '{admin_no}' not found.")

    def student_menu(self):
        print("--------------------MENU--------------------")
        print("1 - View student grades")
        print("m - Print menu")
        print("c - Clear Screen")
        print("q - Quit system\n")

class View(TeacherView, StudentView):
    def __init__(self):
        self.staff_id = None
        self.teacher_name = None
        self.student_id = None
        self.student_name = None

    def setup(self):
        user_type = input("---LOGIN DETAILS---\nWho is viewing?\n1. Teacher\n2. Student\nEnter choice: ")
        if user_type == "1":
            self.staff_id = input("Enter teacher's ID: ")
            self.teacher_name = input("Enter teacher's name: ")
            self.teacher_menu()
            while True:
                choice = input("Enter your choice: ")
                if choice == "1":
                    self.add_student()
                elif choice == "2":
                    self.delete_student()
                elif choice == "3":
                    self.view_statistics()
                elif choice == "4":
                    self.view_student()
                elif choice == "5":
                    self.edit_student()
                elif choice == "6":
                    self.view_gradebook()
                elif choice == 'm':
                    self.teacher_menu()   
                elif choice == 'c':
                    os.system('cls') #Only for windows       
                elif choice == 'q':
                    print('Bye bye')
                    break
            
        elif user_type == "2":
            self.student_id = input("Enter student ID: ")
            self.student_name = input("Enter student name: ")
            self.student_menu()
            while True:
                choice = input("Choice: ")
                if choice == "1":
                    self.view_student()
                elif choice == "m":
                    self.student_menu()
                elif choice == 'c':
                    os.system('cls') #Only for windows 
                elif choice == "q":
                    print("Goodbye!")
                    break
            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    user1 = View()
    user1.setup()
            



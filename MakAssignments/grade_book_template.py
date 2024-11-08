import json
import statistics
import os

STUDENT_NAME = "PANCHAL CHARMI"
STUDENT_NUMBER = "2400721516"
REGISTRATION_NUMBER = "24/X/21516/PS"

class Student:
    def __init__(self, admin_no, name):
        self.admin_no = admin_no
        self.name = name
        self.marks = {}

    def set_marks(self, subject, marks):
        if subject in ['Math', 'SST', 'Science', 'English']:
            if 0<= marks <=100:
                self.marks[subject] = marks
                return True
            else:
                return False
        else:
            return False
            
    def get_marks(self, subject):
        return self.marks.get(subject, None)
    def edit_marks(self, subject, new_marks):
        if subject in ['Math', 'SST', 'Science', 'English']:
            if 0<= new_marks <=100:
                self.marks[subject] = new_marks
                return True
            else:
                return False
        else:
            return False

class Gradebook(Student):
    gradebook = {}
    def __init__(self, filename='previous_data.json'):
        self.filename = filename
        self.load_data()

    def load_data(self):
        if os.path.exists(self.filename) and os.path.getsize(self.filename) > 0:
            try:
                with open(self.filename, 'r') as f:
                    Gradebook.gradebook = json.load(f) #opening a non-empty file
            except json.JSONDecodeError:
                print("Error occured")
                Gradebook.gradebook = {}
        else:
            Gradebook.gradebook = {}

    def save_data(self):
        with open(self.filename, 'w') as f:
            json.dump(Gradebook.gradebook, f, indent=4)

    def add_student(self, student, filename='previous_data.json'):
        self.load_data()
        admin_no = student.admin_no
        if admin_no in Gradebook.gradebook:
            print(f"Student with admin number '{admin_no}' already exists.")
            return False

        try:
            student_name = student.name
            for subject in ['Math', 'SST', 'Science', 'English']:
                while True:
                    try:
                        marks = int(input(f"Enter the marks for {subject}: "))
                        if student.set_marks(subject, marks):
                            break
                        else:
                            print("Please enter marks between 0 and 100.")
                    except ValueError:
                        print("Please enter a valid integer.")

            Gradebook.gradebook[admin_no] = {
                'name': student_name,
                'Math': student.get_marks("Math"),
                'SST': student.get_marks("SST"),
                'Science': student.get_marks("Science"),
                'English': student.get_marks("English")
            }

            self.save_data()
            print(f"Student: '{student_name}' has been added.")
            return True
        except ValueError:
            print("Invalid input.")
            return False

    def get_student(self, admin_no):
        if admin_no in Gradebook.gradebook:
            student_data = Gradebook.gradebook[admin_no]
            student = Student(admin_no, student_data['name'])
            student.marks = {
                'Math': student_data['Math'],
                'SST': student_data['SST'],
                'Science': student_data['Science'],
                'English': student_data['English']
            }
            return student
        else:
            print(f"Student with admin number '{admin_no}' not found.")
            return None

    def delete_student(self, admin_no):
        if admin_no in Gradebook.gradebook:
            del Gradebook.gradebook[admin_no]
            self.save_data()
            print(f"Student with admin_no {admin_no} deleted.")
        else:
            print(f"Student with admin_no '{admin_no}' not found in the gradebook.")
            return False


    def view_statistics(self):
        subjects = ['Math', 'SST', 'Science', 'English']
        stats = {}
        for subject in subjects:
            marks = [student[subject] for student in Gradebook.gradebook.values() if subject in student]
            stats.update({
                f'Average_{subject}': statistics.mean(marks) if marks else None,
                f'Max_{subject}': max(marks) if marks else None,
                f'Min_{subject}': min(marks) if marks else None,
                f'Mode_{subject}': statistics.mode(marks) if marks else None,
                f'Mode_Freq_{subject}': marks.count(statistics.mode(marks)) if marks else None,
            })
        return stats

    def view_student_grades(self, admin_no):
        if admin_no in Gradebook.gradebook:
            student_grades = {
                'Maths': Gradebook.gradebook[admin_no]['Math'],
                'English': Gradebook.gradebook[admin_no]['English'],
                'Science': Gradebook.gradebook[admin_no]['Science'],
                'SST': Gradebook.gradebook[admin_no]['SST']
            }
            return student_grades
        else:
            print(f"Student with admin number '{admin_no}' not found.")
            return None
        
    def print_gradebook(self):
        return {
            'total_students': len(Gradebook.gradebook),
            'student_details': {str(admin_no): data['name'] for admin_no, data in Gradebook.gradebook.items()}
        }
def print_menu():
    print("--------------------Menu--------------------")
    print("1 - Add student")
    print("2 - Delete student, given an admin_no")
    print("3 - View statistics about the grades")
    print("4 - View student grades")
    print("5 - Edit student grades")
    print("6 - Print Gradebook")
    print("m - Print menu")
    print("c - Clear Screen")
    print("q - Quit system\n")

def main():
    gradebook = Gradebook()
    print_menu()

    while True:
        choice = input("\nSelect an option: ").strip().lower()
        if choice == '1':
            try:
                admin_no = int(input("Enter the admin_no of student to add: "))
                if admin_no in gradebook.gradebook:
                    print(f"Student with admin number '{admin_no}' already exists.")
                    continue  

                name = input("Enter the name of the student: ")
                student = Student(admin_no, name)
                
                if gradebook.add_student(student):
                    print(f"Student '{student.name}' has been added.")
                else:
                    print("Failed to add student.")
            except ValueError:
                print("Please enter a valid admin_no.")

        elif choice == '2':
            try:
                admin_no = int(input("Enter the admin_no of student to delete: "))
                gradebook.delete_student(admin_no)
            except ValueError:
                print("Please enter a valid admin_no.")
        elif choice == '3':
            stats = gradebook.view_statistics()
            for key, value in stats.items():
                print(f"{key}: {value}")

        elif choice == '4':
            try:
                admin_no = int(input("Enter the admin_no of student to view: "))
                student = gradebook.view_student_grades(admin_no) 
                if student:
                    print(f"\n--- Grades for {Gradebook.gradebook[admin_no]['name']} ---")
                    for subject, grade in student.items():
                        print(f"{subject}: {grade}")
                else:
                    print(f"Student with admin number '{admin_no}' not found.")
            except ValueError:
                print("Please enter a valid admin_no.")
    
        elif choice == '5':
            try:
                admin_no = int(input("Enter the admin_no of student to edit: "))
                student = gradebook.get_student(admin_no)
                if student:
                    try:
                        subject = input("Enter the subject to edit: ")
                        if subject in ['Math', 'SST', 'Science', 'English']:
                            new_marks = int(input("Enter the new marks: "))
                            if student.edit_marks(subject, new_marks):
                                gradebook.gradebook[admin_no][subject] = new_marks
                                gradebook.save_data()
                                print("Marks updated successfully.")
                            else:
                                print("Invalid marks. Please enter marks between 0 and 100")
                        else:
                            print("Invalid subject. Please enter from [Math, SST, Science, or English].")
                    except ValueError:
                        print("Please enter a valid integer for marks.")
                else:
                    print("Student not found.")
            except ValueError:
                print("Please enter a valid admin_no.")

        elif choice == '6':
            gradebook_data = gradebook.print_gradebook()
            print("\nGradebook of students")
            print(f"Total Students: {gradebook_data['total_students']}")
            for admin_no, name in gradebook_data['student_details'].items():
                print(f"Admin No: {admin_no}, Name: {name}")
        elif choice == 'm':
            print_menu()
        elif choice == 'c':
            print("\033c", end="")  # Clear screen
        elif choice == 'q':
            gradebook.save_data()
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()

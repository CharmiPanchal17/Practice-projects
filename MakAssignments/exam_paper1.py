class Student:
    total_students = 0
    
    def __init__(self, full_name, registration_number, student_number):
        self.full_name = full_name
        self.registration_number = registration_number
        self.student_number = student_number
        self.id_number = Student.total_students + 1
        Student.total_students += 1

    def print_statement(self):
        print(f"Name: {self.full_name}")
        print("University: Makerere")
        print("College: Not Assigned")
        print(f"Reg No: {self.registration_number}")
        print(f"Student No: {self.student_number}")
        print(f"ID No: {self.id_number}")
        print(f"Total Students: {Student.total_students}\n")
    
    def edit_registration_number(self, new_registration_number):
        self.registration_number = new_registration_number


class CEDAT_Student(Student):
    college = "CEDAT"


class CoCIS_Student(Student):
    college = "CoCIS"


class EDUC_Student(Student):
    college = "Education"


class EASLIS_Student(CoCIS_Student):
    school = "EASLIS"


class SCIT_Student(CoCIS_Student):
    school = "SCIT"


class CS_Student(CoCIS_Student):
    department = "Computer Science"
    
    def print_statement(self):
        print(f"Name: {self.full_name}")
        print("University: Makerere")
        print(f"College: {self.college}")
        print(f"Reg No: {self.registration_number}")
        print(f"Student No: {self.student_number}")
        print(f"Department: {self.department}")
        print(f"ID No: {self.id_number}")
        print(f"Total Students: {Student.total_students}\n")


class SE_Student(CoCIS_Student):
    department = "Networks"
    
    def print_statement(self):
        print(f"Name: {self.full_name}")
        print("University: Makerere")
        print(f"College: {self.college}")
        print(f"Reg No: {self.registration_number}")
        print(f"Student No: {self.student_number}")
        print(f"Department: {self.department}")
        print(f"ID No: {self.id_number}")
        print(f"Total Students: {Student.total_students}\n")


# Create students as specified
student1 = Student(full_name="john", registration_number="100", student_number="100")
student2 = SE_Student(full_name="doe", registration_number="200", student_number="200")
student3 = CS_Student(full_name="mary", registration_number="300", student_number="300")

# Call the print_statement method on each student
student1.print_statement()
student2.print_statement()
student3.print_statement()

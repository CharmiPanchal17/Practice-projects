class Student:
 
    def __init__(self, admin_no, name):
        self.admin_no = admin_no
        self.name = name
        self.marks = {}

    def add_student(self,student):
        gradebook = {}
        admin_no = student.admin_no
        if admin_no in gradebook:
            print(f"Student with {admin_no} already exists")


        try:
            name= student.name
            for subject in ["Math", "SST", "English", "Science"]:
                marks = int(input(f"Enter the marks for {subject}: "))

                if 0<= marks <=100:
                    self.marks[subject] = marks
                else:
                    print("Marks must be between 0 and 100")


                gradebook[admin_no]= {
                    "name": name,
                    "Math": self.marks.get("Math"),
                    "SST": self.marks.get("SST"),
                    "English": self.marks.get("English"),
                    "Science": self.marks.get("Science"),
                }
        except ValueError:
            pass


        



def print_menu():
    print("----------------Menu ----------------")
    print("1 - Add student")
    print("2 - Delete student, given an admin_no")
    print("3 - View statistics about the grades")
    print("4 - View student grades")
    print("5 - Edit student grades")
    print("6 - Print Gradebook")
    print("m - Print menu")
    print("q - Quit system\n")

def main():
    gradebook = Student(admin_no=None, name=None)
    print_menu()
    
    while True:
        choice = input("Enter your choice: ").strip().lower()

        if choice== "1":
            admin_no = input("enter admin number: ")
            name = input("enter name: ")
            student = Student(admin_no, name)
            student.add_student(student)
        # elif choice == "2":

        # elif choice == "3":

        # elif choice == "4":

        # elif choice == "5":

        # elif choice == "6":

        # elif choice == "m":
        #     print_menu()

        else:
            print("Invalid choice. Please try again.")
if __name__ == "__main__":
    main()
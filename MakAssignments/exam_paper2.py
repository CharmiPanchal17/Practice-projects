import sys

# Models
class Student:
    def __init__(self, unique_number, name, date_of_birth, course, registration_number):
        self.unique_number = unique_number
        self.name = name
        self.date_of_birth = date_of_birth
        self.course = course
        self.registration_number = registration_number
        self.borrowed_books = []  # Stores tuples of (ISBN, serial_number)

class Book:
    def __init__(self, unique_number, author, title, serial_number, number_of_copies):
        self.unique_number = unique_number
        self.author = author
        self.title = title
        self.serial_number = serial_number
        self.number_of_copies = number_of_copies
        self.available_copies = number_of_copies

# Main Application
class LibraryApp:
    def __init__(self):
        self.students = {}
        self.books = {}
        self.password = "admin"
        self.default_password_changed = False

    def login(self):
        while True:
            print("\n--- Librarian Login ---")
            entered_password = input("Enter Password: ")
            if entered_password == self.password:
                if not self.default_password_changed:
                    print("\nYou must change the default password.")
                    self.change_password()
                print("Login Successful!")
                break
            else:
                print("Incorrect password. Try again.")

    def change_password(self):
        while True:
            new_password = input("Enter new password: ")
            confirm_password = input("Confirm new password: ")
            if new_password == confirm_password:
                self.password = new_password
                self.default_password_changed = True
                print("Password changed successfully!")
                break
            else:
                print("Passwords do not match. Try again.")

    def add_student(self):
        print("\n--- Add Student ---")
        unique_number = input("Enter unique number: ")
        if unique_number in self.students:
            print("Student with this unique number already exists!")
            return
        name = input("Enter name: ")
        date_of_birth = input("Enter date of birth (YYYY-MM-DD): ")
        course = input("Enter course: ")
        registration_number = input("Enter registration number: ")
        self.students[unique_number] = Student(unique_number, name, date_of_birth, course, registration_number)
        print("Student added successfully!")

    def add_book(self):
        print("\n--- Add Book ---")
        isbn = input("Enter ISBN (13-digit number): ")
        if isbn in self.books:
            print("Book with this ISBN already exists!")
            return
        author = input("Enter author: ")
        title = input("Enter title: ")
        serial_number = input("Enter serial number: ")
        number_of_copies = int(input("Enter total number of copies: "))
        self.books[isbn] = Book(isbn, author, title, serial_number, number_of_copies)
        print("Book added successfully!")

    def rent_book(self):
        print("\n--- Rent Book ---")
        student_number = input("Enter student unique number: ")
        if student_number not in self.students:
            print("Student is not registered!")
            return
        isbn = input("Enter ISBN: ")
        if isbn not in self.books:
            print("Book with this ISBN does not exist!")
            return
        book = self.books[isbn]
        if book.available_copies <= 0:
            print("No available copies of this book!")
            return
        student = self.students[student_number]
        if len(student.borrowed_books) >= 3:
            print("Student cannot borrow more than 3 books!")
            return
        serial_number = input("Enter serial number: ")
        if (isbn, serial_number) in student.borrowed_books:
            print("Student already possesses this book!")
            return
        student.borrowed_books.append((isbn, serial_number))
        book.available_copies -= 1
        print(f"Book '{book.title}' rented to student '{student.name}' successfully!")

    def print_students_with_book(self):
        print("\n--- Students with a Book ---")
        isbn = input("Enter ISBN: ")
        serial_number = input("Enter serial number: ")
        if isbn not in self.books:
            print("Book with this ISBN does not exist!")
            return
        print(f"Students possessing the book '{self.books[isbn].title}':")
        for student in self.students.values():
            if (isbn, serial_number) in student.borrowed_books:
                print(f" - {student.name} (ID: {student.unique_number})")

    def print_student_details(self):
        print("\n--- Student Details ---")
        student_number = input("Enter student unique number: ")
        if student_number not in self.students:
            print("Student not found!")
            return
        student = self.students[student_number]
        print(f"Name: {student.name}")
        print(f"Date of Birth: {student.date_of_birth}")
        print(f"Course: {student.course}")
        print(f"Registration Number: {student.registration_number}")
        print(f"Borrowed Books: {student.borrowed_books}")

    def print_book_details(self):
        print("\n--- Book Details ---")
        isbn = input("Enter ISBN: ")
        if isbn not in self.books:
            print("Book not found!")
            return
        book = self.books[isbn]
        print(f"Title: {book.title}")
        print(f"Author: {book.author}")
        print(f"Serial Number: {book.serial_number}")
        print(f"Total Copies: {book.number_of_copies}")
        print(f"Available Copies: {book.available_copies}")

    def quit_application(self):
        print("Exiting application. Goodbye!")
        sys.exit()

    def run(self):
        self.login()
        while True:
            print("\n--- Library Management System ---")
            print("1. Add Student")
            print("2. Add Book")
            print("3. Rent Book")
            print("4. List Students with a Book")
            print("5. Student Details")
            print("6. Book Details")
            print("7. Quit")
            choice = input("Enter your choice: ")
            if choice == "1":
                self.add_student()
            elif choice == "2":
                self.add_book()
            elif choice == "3":
                self.rent_book()
            elif choice == "4":
                self.print_students_with_book()
            elif choice == "5":
                self.print_student_details()
            elif choice == "6":
                self.print_book_details()
            elif choice == "7":
                self.quit_application()
            else:
                print("Invalid choice. Try again!")

# Start the application
if __name__ == "__main__":
    app = LibraryApp()
    app.run()

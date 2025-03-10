import getpass
import datetime

# Global variable to hold the librarian's password, initially set to "Admin"
librarian_password = "Admin"
password_changed = False

class Student:
    def __init__(self, unique_number, name, date_of_birth, course, registration_number):
        self.unique_number = unique_number
        self.name = name
        self.date_of_birth = date_of_birth
        self.course = course
        self.registration_number = registration_number
        self.borrowed_books = []

    def borrow_book(self, book):
        if book.available_copies > 0:
            self.borrowed_books.append(book)
            book.available_copies -= 1
            print(f"Book '{book.title}' borrowed by {self.name}.")
        else:
            print("No available copies to borrow.")

    def return_book(self, book):
        if book in self.borrowed_books:
            self.borrowed_books.remove(book)
            book.available_copies += 1
            print(f"Book '{book.title}' returned by {self.name}.")
        else:
            print("This book was not borrowed by the student.")


class Book:
    def __init__(self, unique_number, author, title, serial_number, number_of_copies):
        self.unique_number = unique_number
        self.author = author
        self.title = title
        self.serial_number = serial_number
        self.number_of_copies = number_of_copies
        self.available_copies = number_of_copies

# Dictionary to store student and book records
students = {}
books = {}

def change_password():
    global librarian_password, password_changed
    new_password = input("Enter new password: ")
    librarian_password = new_password
    password_changed = True
    print("Password successfully changed.")

def login():
    global password_changed
    while True:
        if not password_changed:
            print("You must change the default password.")
            change_password()

        password = getpass.getpass("Enter password: ")
        if password == librarian_password:
            print("Login successful!")
            break
        else:
            print("Incorrect password. Try again.")

def add_student():
    unique_number = input("Enter student unique number: ")
    name = input("Enter student name: ")
    date_of_birth = input("Enter student date of birth (YYYY-MM-DD): ")
    course = input("Enter student course: ")
    registration_number = input("Enter student registration number: ")
    student = Student(unique_number, name, date_of_birth, course, registration_number)
    students[unique_number] = student
    print(f"Student '{name}' added successfully.")

def add_book():
    unique_number = input("Enter book unique number (13-digit ISDN): ")
    author = input("Enter book author: ")
    title = input("Enter book title: ")
    serial_number = input("Enter book serial number: ")
    number_of_copies = int(input("Enter number of copies: "))
    book = Book(unique_number, author, title, serial_number, number_of_copies)
    books[unique_number] = book
    print(f"Book '{title}' added successfully.")

def main():
    print("Welcome to the Library Management System")
    login()
    
    while True:
        print("\nOptions:")
        print("1. Add Student")
        print("2. Add Book")
        print("3. Borrow Book")
        print("4. Return Book")
        print("5. Exit")

        choice = input("Enter your choice: ")
        if choice == "1":
            add_student()
        elif choice == "2":
            add_book()
        elif choice == "3":
            student_id = input("Enter student unique number: ")
            book_id = input("Enter book unique number: ")
            if student_id in students and book_id in books:
                students[student_id].borrow_book(books[book_id])
            else:
                print("Student or book not found.")
        elif choice == "4":
            student_id = input("Enter student unique number: ")
            book_id = input("Enter book unique number: ")
            if student_id in students and book_id in books:
                students[student_id].return_book(books[book_id])
            else:
                print("Student or book not found.")
        elif choice == "5":
            print("Exiting the system.")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()

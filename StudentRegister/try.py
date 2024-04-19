# this is the base class.
# Student registration..
import csv
import getpass

class Registration:
    # A loop that creates the total number of students that have entered data.
    # data_entry= 0

    def __init__(self):

        # Entry of the name..
        print("Enter the students name:")
        self.FirstName = input("Enter Your First Name: ").lower()
        self.LastName = input("Enter Your Last Name: ").lower()

        #Entering gender...
        while True:
            self.Gender = input("Enter Male or Female: ").lower()
            if self.Gender in ["male", "female"]:
                break
            else:
                print("INVALID INPUT!,Enter the vaild answer.")

        #Entering the age...
        print("Choose Month or Year for Age selection.")
        print("1.Month(s)")
        print("2. Year(s)")
        selection= input("Enter Your Choice.: ")

        if selection == "1":
            while True:
                self.Age = int(input("Enter Your Age in Months: "))
                if self.Age <=12:
                    break
                else: 
                        print("Please Enter the Valid Age!!")

        elif selection == "2":
            while True:
                self.Age = int(input("Enter Your Age in Years: "))
                if self.Age <= 7:
                    break
                else: 
                    print("Please Enter the Valid Age!!")

        else:
            print("Please Enter the Valid Age!!")

       
    # Entering the allergies...
        self.Allergies = input("Enter In Your Allergies: ").split()

        #Entering the class...
        print ("The following displays the grade your child is in, please select.")
        while True:       
            print("1.Top class")
            print("2.Baby class")
            print("3.Middle class")
            grade_choice = input("Select one of the choices: ")

            if grade_choice == "1":
                self.Grade = "Top class"
                break
            elif grade_choice == "2":
                self.Grade = "Baby class"
                break
            elif grade_choice == "3":
                self.Grade = "Middle class"
                break
            else:
                print("ENTER A VALID INPUT")


        #Entering the phonenumber...
class Phonenumber(Registration):
    def __init__(self):
        self.phonenumber= "+256"
        while True:
            self.phone_number = input("Enter a valid Phonenumber of 9 digits: ")
            if len(self.phone_number) == 9:
                print(self.phonenumber + " " + self.phone_number)
                break
            else:
                print("INVALID PHONENUMBER")

class Email(Registration):
    def __init__(self):
        self.email= "<EMAIL>"
        while True:
            self.email = input("Enter a valid Email: ")
            if "@" in self.email:
                print(self.email)
                break
            else:
                print("INVALID EMAIL")

                
class Password(Registration):
    def __init__(self):
        self.password= "<PASSWORD>"
        while True:
            self.password = getpass.getpass("Enter a valid Password: ")
            if len(self.password) >= 8:
                print(self.password)
                break
            else:
                print("INVALID PASSWORD")


    # Registration.data_entry += 1 

# print(f"The Total Entry of Students: {Registration.data_entry}")

# froming objects out of the class
reg = Registration()
print(f"First name: {reg.FirstName}")
print(f"Last name: {reg.LastName}")
print(f"Gender: {reg.Gender}")
print(f"Age: {reg.Age}")
print(f"Allergies: {reg.Allergies}")
print(f"Grade: {reg.Grade}")

phonenumber = Phonenumber()
print(f"Phone Number: {phonenumber.phonenumber} {phonenumber.phone_number}")

email = Email()
print(f"Email: {email.email}")

password = Password()
print(f"Password: {password.password}")
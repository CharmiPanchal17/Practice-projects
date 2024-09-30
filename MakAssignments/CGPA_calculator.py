#The CGPA program

student_name= input("Enter your name: ")
student_number = input("Enter your student number: ")

course1_mark= int(input("\nEnter your marks obtained in course unit 1: "))
course1_creditunit = int(input("Enter the credit unit of course 1: "))

course2_mark= int(input("\nEnter your marks obtained in course unit 2: "))
course2_creditunit = int(input("Enter the credit unit of course 2: "))

course3_mark= int(input("\nEnter your marks obtained in course unit 3: "))
course3_creditunit = int(input("Enter the credit unit of course 3: "))

course4_mark= int(input("\nEnter your marks obtained in course unit 4: "))
course4_creditunit = int(input("Enter the credit unit of course 4: "))

def grade_conversion(mark):

    if mark >= 90:
        return "A"
    elif mark >= 80:
        return "B"
    elif mark >= 70:
        return "C"
    elif mark >= 60:
        return "D"
    elif mark >= 50:
        return "E"
    else:
        return "F"

def grade_point(grade):

    if grade == "A":
        return 5.0

    elif grade == "B":
        return 4.0

    elif grade == "C":
        return 3.0

    elif grade == "D":
        return 2.0

    elif grade == "E":
        return 1.0

    else:
        return 0.0

course1_grade = grade_conversion(course1_mark)
course1_point = grade_point(course1_grade)

course2_grade = grade_conversion(course2_mark)
course2_point = grade_point(course2_grade)

course3_grade = grade_conversion(course3_mark)
course3_point = grade_point(course3_grade)

course4_grade = grade_conversion(course4_mark)
course4_point = grade_point(course4_grade)

CGPA = ((course1_point*course1_creditunit)+(course1_point*course2_creditunit)+(course3_point*course3_creditunit)+(course4_point*course4_creditunit))/(course1_creditunit+course2_creditunit+course3_creditunit+course4_creditunit)

print("\n--------------------------------")
print(f"Student Name: {student_name}")

print(f"Student Number: {student_number}")

print(f"The CGPA obtained is: {CGPA}")
print("--------------------------------")

#Basic Calculator

num1= int(student_number[-1])
num2= int(student_number[-2])

print(f"The last two digits of your student number are '{num1}' and '{num2}'")

sum = num1+num2
print(f" The Sum of the two digits is: {sum}")

difference = num1-num2
print(f" The difference between the two digits is: {difference}")

product = num1*num2
print(f" The product of the two digits is: {product}")

quotient = num1/num2
print(f" The quotient of the two digits is: {quotient}")
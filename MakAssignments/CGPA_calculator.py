student_name= input("Enter your name: ")
student_number = input("Enter your student number: ")

course1_mark= int(input("Enter your marks obtained in course unit 1: "))
course1_creditunit = int(input("Enter the credit unit of course 1: "))

course2_mark= int(input("Enter your marks obtained in course unit 2: "))
course2_creditunit = int(input("Enter the credit unit of course 2: "))

course3_mark= int(input("Enter your marks obtained in course unit 3: "))
course3_creditunit = int(input("Enter the credit unit of course 3: "))

course4_mark= int(input("Enter your marks obtained in course unit 4: "))
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

print(f"\nStudent Name: {student_name}")

print(f"\nStudent Number: {student_number}")

print(f"CGPA: {CGPA}")
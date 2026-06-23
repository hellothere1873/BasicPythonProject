from  class_and_functions import *


while True:
    print("Student assignment stuff")
    print("1. Add student.")
    print("2. Add teacher.")
    print("3. Create course.")
    print("4. Enroll student.")
    print("5. Add grade.")
    print("6. Print GPA.")
    print("7. Print course average.")
    print("8. Update database.txt")
    print("Press any other key to quit.")
    answer = input("Please choose.")

    if answer == "1":
        name = input("")
        age = int(input(""))
        SID = input("")
        add_student(name, age, SID)
    elif answer == "2":
        name = input("")
        age = int(input(""))
        TID = input("")
        add_teacher(name, age, TID)
    elif answer == "3":
        course = input("")
        TID = input("")
        create_course(course, TID)
    elif answer == "4":
        course = input("")
        SID = input("")
        enroll_student(course, SID)
    elif answer == "5":
        course = input("")
        SID = input("")
        grade = int(input(""))
        add_grade(SID, course, grade)
    elif answer == "6":
        SID = input("")
        print_gpa(SID)
    elif answer == "7":
        course = input("")
        print_course_average(course)
    elif answer == "8":
        updatefile()
    else:
        break
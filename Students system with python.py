students = [
    {"name": "Ahmed", "age": 20, "grades": [80, 90, 70]},
    {"name": "Mona", "age": 19, "grades": [95, 85, 90]}
]

def ask():
    print('''
    1. Add Student
    2. Display All Students
    3. Search for a Student
    4. Calculate Student Average
    5. Display Top Student
    6. Display Statistics
    7. Display the highest and lowest grade 
    8. update a student's grades.
    9. Exit
    ''')
    x= int(input(" Choose the number of the option you want : "))
    if x != 9 :
        ask()

def add_student():
    name = input("Please enter your name : ").lower().strip()
    age = int(input("Please enter your age : "))
    grades = []

    for i in range (3):
        x = float(input(f"Enter grade {i+1} "))
        while x < 0 or x > 100:
            print("Grade must be between 0 and 100 ")
            x = float(input(f"Enter grade {i + 1} : "))

        grades.append(x)

    student = {
     "name": name,
     "age": age,
     "grades": grades
    }

    for i in students:
        if i["name"] == name :
            print(f"There is already {name} in the system")
            break 
    else:students.append(student)

def display_students():
    if len(students) ==  0 :
        print(" There is no data available.")
    else:
        for student in students:
            print("Name: ", student["name"])
            print("Age: ", student["age"])
            print("Grades: ", student["grades"])

def search_student(name):
    for student in students :
        if student["name"] == name :
            print (student)
            break
    else: print("Student not found ")

def calculate_average(grades):
    return sum(grades) / len(grades)

def show_average (name):
    for student in students:
        if name == student["name"]:
            print(calculate_average(student["grades"]))
            break
    else: print("Student not found ,please enter a valid name. ")

def display_top_student():
    top = 0
    name = ""
    for student in students:
        average = calculate_average(student["grades"])
        if average > top:
            top = average
            name = student["name"]

    print("Top student: ", name)
    print("Average: ", top)

def passed ():
    passed_count = 0
    failed_count = 0
    for student in students:
        average = calculate_average(student["grades"])
        if average >= 50:
            passed_count += 1
        else:
            failed_count += 1

    return passed_count, failed_count        

def display_statistics():
    total = len(students)
    sum = 0
    for student in students:
        sum += calculate_average(student["grades"])
    if total == 0:
        print("There is no data available.")
    else:
        print("Total students:", total)
        print("Overall average:", sum / total)
        passed_count, failed_count = passed()
        print("Passed students:", passed_count)
        print("Failed students:", failed_count)

    names = set()
    for student in students:
        names.add(student["name"])
    print("Unique student names:", names)

def highest_lowest():
    highest = 0
    lowest = 100
    for student in students:
        for grade in student["grades"]:
            temp = grade
            if temp > highest:
                highest = temp

            if temp<lowest:
                lowest=temp
    
    print("Highest : ", highest)
    print("Lowest : ", lowest)

def update_grades(name):
    for student in students :
        if student["name"]== name :
            for i in range(3) :
                x = float(input(f"Enter grade {i+1} "))
                while x < 0 or x > 100:
                    print("Grade must be between 0 and 100 ")
                    x = float(input(f"Enter grade {i+ 1} : "))    
                student["grades"][i] = x

            break            

while True:

    print('''
    ===== Student Management System =====
    1. Add Student
    2. Display All Students
    3. Search for a Student
    4. Calculate Student Average
    5. Display Top Student
    6. Display Statistics
    7. Display the highest and lowest grade 
    8. update a student's grades.
    9. Exit
    ''')

    choice = int(input("Choose an option: "))

    if choice == 1:
        add_student()

    elif choice == 2:
        display_students()

    elif choice == 3:
        search_student(input("Enter a name to search for a student : ").lower().strip())

    elif choice == 4:
        show_average(input("Enter a name to show its average: ").lower().strip())

    elif choice == 5:
        display_top_student()

    elif choice == 6:
        display_statistics()

    elif choice == 7:
        highest_lowest()

    elif choice == 8:
        update_grades(input("Enter a student's name to update its grade : ").lower().strip())

    elif choice == 9:
        print("Thanks")
        break

    else:
        print("Invalid choice.")

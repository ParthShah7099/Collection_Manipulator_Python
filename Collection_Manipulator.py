'''

PR.3 Collection Manipulator

Create a python program called Student Data Organizer that manages a collection of student
records. This project will apply intermediate-level concepts such as string formatting and
manipulation, collection data types (List, Tuple, Set and Dictionary), mutability and
immutability, type casting and the del keyword.

'''
students = []

print("Welcome to the Student Data Organizer!")

while True:
    print("\nSelect an option:")
    print("1. Add Student")
    print("2. Display All Students")
    print("3. Update Student Information")
    print("4. Delete Student")
    print("5. Display Subjects Offered")
    print("6. Exit")
    choice = input("Enter your choice: ")

    if choice == '1':
        print("\nEnter student details:")
        student_id = input("Student ID: ")
        name = input("Name: ")
        age = int(input("Age: "))
        grade = input("Grade: ")
        dob = input("Date of Birth (YYYY-MM-DD): ")
        subjects = input("Subjects (comma-separated): ").split(',')
        id_dob = (student_id, dob)

        
        student_info = {
            'ID and DOB': id_dob,
            'Name': name,
            'Age': age,
            'Grade': grade,
            'Subjects': set(subjects)  
        }

        
        students.append(student_info)
        print("\nStudent added successfully!")

    elif choice == '2':
        print("\n---------- Display All Students ----------")
        if students:
            for student in students:
                print(f"Student ID: {student['ID and DOB'][0]} | Name: {student['Name']} | Age: {student['Age']} | Grade: {student['Grade']} | Subjects: {', '.join(student['Subjects'])}")
        else:
            print("\nNo Student Found...")

    elif choice == '3':
        student_id = input("\nEnter the Student ID to update: ")
        found = False
        for student in students:
            if student['ID and DOB'][0] == student_id:
                found = True
                print("Current Information:")
                print(f"Name: {student['Name']}, Age: {student['Age']}, Grade: {student['Grade']}, Subjects: {', '.join(student['Subjects'])}")
                student['Name'] = input("Enter new Name: ")
                student['Age'] = int(input("Enter new Age: "))
                student['Grade'] = input("Enter new Grade: ")
                student['Subjects'] = set(input("Enter new Subjects (comma-separated): ").split(','))
                print("\nStudent information updated successfully!")
                break
        if found == False:
            print("\nStudent ID not found.")

    elif choice == '4':
        student_id = input("Enter Student ID to delete: ")
        found = False
        for i in range(len(students)):
            if students[i]['ID and DOB'][0] == student_id:
                del students[i]
                print("\nStudent deleted successfully!")
                found = True
                break
        if found == False:
            print("\nStudent ID not found.")

    elif choice == '5':
        subjects = set()
        for student in students:
            subjects.update(student['Subjects'])
        print("\n---------- Subjects Offered ----------")
        print(', '.join(subjects))

    elif choice == '6':
        print("\nThank you for using the Student Data Organizer!")
        break

    else:
        print("\nInvalid choice. Please try again.")

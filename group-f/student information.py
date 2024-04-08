# Department maintains a student information. The file contains roll number, name, 
# division and address. Allow user to add, delete information of student. Display 
# information of particular employee. If record of student does not exist an appropriate 
# message is displayed. If it is, then the system displays the student details. Use sequential 
# file to main the data.  

import os

def add_student_info():
    roll_number = input("Enter roll number: ")
    name = input("Enter name: ")
    division = input("Enter division: ")
    address = input("Enter address: ")

    with open("student_info.txt", "a") as file:
        file.write(f"{roll_number},{name},{division},{address}\n")
    print("Student information added successfully.")

def delete_student_info():
    roll_number = input("Enter roll number of student to delete: ")

    with open("student_info.txt", "r") as file:
        lines = file.readlines()

    found = False
    with open("student_info.txt", "w") as file:
        for line in lines:
            if line.split(",")[0] != roll_number:
                file.write(line)
            else:
                found = True

    if found:
        print("Student information deleted successfully.")
    else:
        print("Student not found.")

def display_student_info():
    roll_number = input("Enter roll number of student to display: ")

    with open("student_info.txt", "r") as file:
        for line in file:
            info = line.strip().split(",")
            if info[0] == roll_number:
                print("Roll Number:", info[0])
                print("Name:", info[1])
                print("Division:", info[2])
                print("Address:", info[3])
                return

    print("Student not found.")

def main():
    while True:
        print("\n1. Add Student Information")
        print("2. Delete Student Information")
        print("3. Display Student Information")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            add_student_info()
        elif choice == '2':
            delete_student_info()
        elif choice == '3':
            display_student_info()
        elif choice == '4':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()

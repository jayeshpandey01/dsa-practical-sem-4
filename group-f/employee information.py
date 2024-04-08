# Company maintains employee information as employee ID, name, designation and salary. 
# Allow user to add, delete information of employee. Display information of particular 
# employee. If employee does not exist an appropriate message is displayed. If it is, then 
# the system displays the employee details. Use index sequential file to maintain the data. 

import os

# Function to add employee information to the file
def add_employee(employee_id, name, designation, salary):
    with open("employee_data.txt", "a") as file:
        file.write(f"{employee_id},{name},{designation},{salary}\n")

# Function to delete employee information from the file
def delete_employee(employee_id):
    temp_file = open("temp.txt", "w")
    with open("employee_data.txt", "r") as file:
        for line in file:
            if line.split(',')[0] != employee_id:
                temp_file.write(line)
    temp_file.close()
    os.remove("employee_data.txt")
    os.rename("temp.txt", "employee_data.txt")

# Function to display information of a particular employee
def display_employee(employee_id):
    with open("employee_data.txt", "r") as file:
        for line in file:
            data = line.split(',')
            if data[0] == employee_id:
                print("Employee ID:", data[0])
                print("Name:", data[1])
                print("Designation:", data[2])
                print("Salary:", data[3])
                return
        print("Employee not found.")

# Main function to handle user input and operations
def main():
    while True:
        print("\n1. Add employee")
        print("2. Delete employee")
        print("3. Display employee")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            employee_id = input("Enter Employee ID: ")
            name = input("Enter Name: ")
            designation = input("Enter Designation: ")
            salary = input("Enter Salary: ")
            add_employee(employee_id, name, designation, salary)
            print("Employee added successfully.")
        elif choice == '2':
            employee_id = input("Enter Employee ID to delete: ")
            delete_employee(employee_id)
            print("Employee deleted successfully.")
        elif choice == '3':
            employee_id = input("Enter Employee ID to display: ")
            display_employee(employee_id)
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

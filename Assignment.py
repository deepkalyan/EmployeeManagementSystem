
employees = {
    101: {'name': 'Satya', 'age': 27, 'department': 'HR', 'salary': 50000},
    102: {'name': 'Anita', 'age': 30, 'department': 'Finance', 'salary': 65000},
    103: {'name': 'Ravi', 'age': 25, 'department': 'IT', 'salary': 55000}
}

menu = ["Add Employee", "View All Employees", "Search for Employee", "Exit"]


def add_employee():
    while True:
        try:
            emp_id = int(input("Enter Employee ID: "))
            if emp_id in employees:
                print("Employee ID already exists. Please enter a unique ID.")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter a numeric Employee ID.")

    name = input("Enter Employee Name: ")
    age = int(input("Enter Employee Age: "))
    department = input("Enter Employee Department: ")
    salary = int(input("Enter Employee Salary: "))

    employees[emp_id] = {'name': name, 'age': age, 'department': department, 'salary': salary}
    print("✅ Employee added successfully!")


def view_all_employees():
    if not employees:
        print("No employees to display.")
    else:
        print(f"{'ID':<10}{'Name':<20}{'Age':<10}{'Department':<15}{'Salary':<10}")
        print("-" * 65)
        for emp_id, details in employees.items():
            print(f"{emp_id:<10}{details['name']:<20}{details['age']:<10}{details['department']:<15}{details['salary']:<10}")


def search_employee():
    try:
        emp_id = int(input("Enter Employee ID to search: "))
    except ValueError:
        print("Invalid input. Please enter a numeric Employee ID.")
        return

    if emp_id in employees:
        details = employees[emp_id]
        print(f"\nEmployee Found:")
        print(f"Name: {details['name']}")
        print(f"Age: {details['age']}")
        print(f"Department: {details['department']}")
        print(f"Salary: {details['salary']}")
    else:
        print("Employee not found.")


def exit_program():
    print("Exiting the program. Goodbye!")
    quit()


def main():
    while True:
        print("\n===== Employee Management System =====")
        for i, option in enumerate(menu, 1):
            print(f"{i}. {option}")
        choice = input("Select an option (1-4): ")

        if choice == '1':
            add_employee()
        elif choice == '2':
            view_all_employees()
        elif choice == '3':
            search_employee()
        elif choice == '4':
            exit_program()
        else:
            print("Invalid choice. Please select a valid option.")


if __name__ == "__main__":
    main()

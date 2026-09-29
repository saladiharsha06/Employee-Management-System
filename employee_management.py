import json
import os


class Employee:
    def __init__(self, emp_id, name, age, department, salary):
        self.emp_id = emp_id
        self.name = name
        self.age = age
        self.department = department
        self.salary = salary

    def to_dict(self):
        return {
            "ID": self.emp_id,
            "Name": self.name,
            "Age": self.age,
            "Department": self.department,
            "Salary": self.salary
        }


class EmployeeManagement:
    def __init__(self):
        self.filename = "employee_data.json"
        self.employees = self.load_data()

    def load_data(self):
        if os.path.exists(self.filename):
            try:
                with open(self.filename, "r") as file:
                    data = json.load(file)

                    if isinstance(data, list):
                        return data

                    return []

            except (json.JSONDecodeError, FileNotFoundError):
                return []

        return []

    def save_data(self):
        try:
            with open(self.filename, "w") as file:
                json.dump(self.employees, file, indent=4)

        except IOError:
            print("Error while saving employee data.")

    def add_employee(self):
        print("\n----- Add Employee -----")

        emp_id = input("Enter Employee ID: ").strip()

        if not emp_id:
            print("Employee ID cannot be empty!")
            return

        for emp in self.employees:
            if str(emp["ID"]) == emp_id:
                print("Employee ID already exists!")
                return

        name = input("Enter Name: ").strip()

        if not name:
            print("Name cannot be empty!")
            return

        try:
            age = int(input("Enter Age: "))

            if age <= 0:
                print("Age must be greater than 0!")
                return

            department = input("Enter Department: ").strip()

            if not department:
                print("Department cannot be empty!")
                return

            salary = float(input("Enter Salary: "))

            if salary < 0:
                print("Salary cannot be negative!")
                return

        except ValueError:
            print("Please enter valid numeric values for age and salary.")
            return

        emp = Employee(
            emp_id,
            name,
            age,
            department,
            salary
        )

        self.employees.append(emp.to_dict())
        self.save_data()

        print("Employee added successfully!")

    def search_employee(self):
        print("\n----- Search Employee -----")

        emp_id = input("Enter Employee ID to search: ").strip()

        for emp in self.employees:
            if str(emp["ID"]) == emp_id:
                print("\nEmployee Found")
                print("----------------------")
                print(f"ID: {emp['ID']}")
                print(f"Name: {emp['Name']}")
                print(f"Age: {emp['Age']}")
                print(f"Department: {emp['Department']}")
                print(f"Salary: {emp['Salary']}")
                print("----------------------")
                return

        print("Employee not found!")

    def update_employee(self):
        print("\n----- Update Employee -----")

        emp_id = input("Enter Employee ID to update: ").strip()

        for emp in self.employees:
            if str(emp["ID"]) == emp_id:

                print("\nCurrent Employee Details")
                print(f"Name: {emp['Name']}")
                print(f"Age: {emp['Age']}")
                print(f"Department: {emp['Department']}")
                print(f"Salary: {emp['Salary']}")

                name = input("\nEnter New Name: ").strip()

                if not name:
                    print("Name cannot be empty!")
                    return

                try:
                    age = int(input("Enter New Age: "))

                    if age <= 0:
                        print("Age must be greater than 0!")
                        return

                    department = input("Enter New Department: ").strip()

                    if not department:
                        print("Department cannot be empty!")
                        return

                    salary = float(input("Enter New Salary: "))

                    if salary < 0:
                        print("Salary cannot be negative!")
                        return

                except ValueError:
                    print("Please enter valid numeric values.")
                    return

                emp["Name"] = name
                emp["Age"] = age
                emp["Department"] = department
                emp["Salary"] = salary

                self.save_data()

                print("Employee updated successfully!")
                return

        print("Employee not found!")

    def delete_employee(self):
        print("\n----- Delete Employee -----")

        emp_id = input("Enter Employee ID to delete: ").strip()

        for emp in self.employees:
            if str(emp["ID"]) == emp_id:

                print("\nEmployee Found")
                print(f"Name: {emp['Name']}")
                print(f"Department: {emp['Department']}")

                confirmation = input(
                    "Are you sure you want to delete this employee? (yes/no): "
                ).lower()

                if confirmation == "yes":
                    self.employees.remove(emp)
                    self.save_data()
                    print("Employee deleted successfully!")
                else:
                    print("Delete operation cancelled.")

                return

        print("Employee not found!")

    def display_all(self):
        print("\n----- All Employees -----")

        if not self.employees:
            print("No employees found!")
            return

        print(
            f"{'ID':<10}"
            f"{'Name':<20}"
            f"{'Age':<8}"
            f"{'Department':<20}"
            f"{'Salary':<12}"
        )

        print("-" * 70)

        for emp in self.employees:
            print(
                f"{str(emp['ID']):<10}"
                f"{emp['Name']:<20}"
                f"{str(emp['Age']):<8}"
                f"{emp['Department']:<20}"
                f"{emp['Salary']:<12.2f}"
            )

    def run(self):
        while True:

            print("\n===== Employee Management System =====")
            print("1. Add Employee")
            print("2. Search Employee")
            print("3. Update Employee")
            print("4. Delete Employee")
            print("5. Display All Employees")
            print("6. Exit")

            choice = input("Enter your choice: ").strip()

            if choice == "1":
                self.add_employee()

            elif choice == "2":
                self.search_employee()

            elif choice == "3":
                self.update_employee()

            elif choice == "4":
                self.delete_employee()

            elif choice == "5":
                self.display_all()

            elif choice == "6":
                print("Exiting Employee Management System...")
                break

            else:
                print("Invalid choice! Please select 1-6.")


if __name__ == "__main__":
    emp_system = EmployeeManagement()
    emp_system.run()
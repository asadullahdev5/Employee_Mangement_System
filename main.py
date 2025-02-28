import csv

class Employee:
    def __init__(self, name="Default Name", Id="000", position="Unknown", salary="0", email="default@example.com"):
        self._name = name
        self._Id = Id
        self._position = position
        self._salary = salary
        self._email = email

    def display(self):
        print(f"Employee info:\n Name: {self._name} \n ID: {self._Id} \n Position: {self._position} \n Salary: {self._salary} \n Email: {self._email}")

    def update(self, name=None, Id=None, position=None, email=None, salary=None):
        if name:
            self._name = name
        if salary:
            self._salary = salary
        if email:
            self._email = email
        if position:
            self._position = position
        if Id:
            self._Id = Id
        print("Employee information updated successfully!")
        return name, Id, position, email, salary


class EmployeeManager:
    def __init__(self, filename='employees_csv.csv'):
        self.filename = filename
        self.employees = []

    def GET_employee(self):
        name = input("Enter the employee name: ")
        Id = input("Enter the employee ID: ")
        position = input("Enter the employee position: ")
        salary = input("Enter the employee salary: ")
        email = input("Enter the employee email: ")
        save_input = input("Please type 'save' to save data: ")

        if save_input == "save":
            new_employee = Employee(name, Id, position, salary, email)
            self.employees.append(new_employee)
            with open(self.filename, 'a', encoding='UTF8') as employee_table:
                writer = csv.writer(employee_table)
                writer.writerow([new_employee._name, new_employee._Id, new_employee._position, new_employee._salary, new_employee._email])
            print("Employee data saved to CSV!")
        else:
            print("Your data is not valid")

    def list_employees(self):
        print("Employee list:")
        for emp in self.employees:
            emp.display()

    def delete_employee(self, Id):
        for emp in self.employees:
            if emp._Id == Id:
                self.employees.remove(emp)
                print(f"Employee with ID {Id} has been deleted successfully!")
                return
        print(f"No employee found with ID {Id}.")

    def search_employee(self, Id):
        for emp in self.employees:
            if emp._Id == Id:
                return emp
        return None


def menu():
    employee_manager = EmployeeManager()
    while True:
        print("Welcome to the Employee Management System. Kindly choose from the menu:")
        print("1. Search for Employee")
        print("2. Add Employee")
        print("3. Update Employee")
        print("4. Delete Employee")
        print("5. List All Employees")
        print("6. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            Id = input("Enter the Employee ID: ")
            employee = employee_manager.search_employee(Id)
            if employee:
                employee.display()
            else:
                print("Employee not found.")
        elif choice == '2':
            employee_manager.GET_employee()
        elif choice == '3':
            Id = input("Enter the Employee ID to update: ")
            employee = employee_manager.search_employee(Id)
            if employee:
                name = input("Enter new name (or leave blank to keep current): ")
                position = input("Enter new position (or leave blank to keep current): ")
                salary = input("Enter new salary (or leave blank to keep current): ")
                email = input("Enter new email (or leave blank to keep current): ")
                employee.update(name, Id, position, email, salary)
            else:
                print("Employee not found.")
        elif choice == '4':
            Id = input("Enter the Employee ID to delete: ")
            employee_manager.delete_employee(Id)
        elif choice == '5':
            employee_manager.list_employees()
        elif choice == '6':
            print("Exiting the system.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    menu()
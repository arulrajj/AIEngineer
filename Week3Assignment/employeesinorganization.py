
class Employee:
    def __init__(self, name, emp_id, department):
        self.name = name
        self.emp_id = emp_id
        self.department = department

    def display_info(self):
        print(f"Employee name: {self.name}")
        print(f"Employee ID: {self.emp_id}")
        print(f"Department: {self.department}")


class Manager(Employee):
    def __init__(self, name, emp_id, department, team_size):
        super().__init__(name, emp_id, department)
        self.team_size=team_size

    def display_info(self):
        print(f"Employee name: {self.name}")
        print(f"Employee ID: {self.emp_id}")
        print(f"Department: {self.department}")
        print(f"Team size: {self.team_size}")

class Developer(Employee):
    def __init__(self, name, emp_id, department, programming_language):
        super().__init__(name, emp_id, department)
        self.programming_language = programming_language

    def display_info(self):
        print(f"Employee name: {self.name}")
        print(f"Employee ID: {self.emp_id}")
        print(f"Department: {self.department}")
        print(f"Expertise in Programming Language: {self.programming_language}")

if __name__ == "__main__":
    print("Employee details from Manager class:")
    m1 = Manager("Babu", "604", "Digital Assurance", 10)
    m1.display_info()

    print("Employee details from Developer class:")
    d1 = Developer("Arul", "610", "Developer", "Python")
    d1.display_info()
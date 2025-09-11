
class Student:


    def __init__(self, name, grade, department):
        self.name = name
        self.grade = grade
        self.department = department

    def print_info(self):
        print(f"Name: {self.name}")
        print(f"Grade: {self.grade}")
        print(f"Department: {self.department}")

    def update_grade(self, new_grade):
        self.grade = new_grade


if __name__ == "__main__":
    student1 = Student("Jack", "A", "Computer Science")
    student2 = Student("Nikhil", "A+", "Mechanical Engineering")
    student3 = Student("Rindel", "B", "Electrical Engineering")

    print("Student1 Info:")
    student1.print_info()
    print("Student2 Info:")
    student2.print_info()
    print("Student3 Info:")
    student3.print_info()

    student2.update_grade("A-")
    print("Updated Student Info:")
    student2.print_info()

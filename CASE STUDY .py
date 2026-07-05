class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")


class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id

    def enroll_course(self, course):
        print(f"{self.name}has enrolled in {course}")

    def displat_info(self):
        super().display_info()
        print(f"Student ID: {self.student_id}")


class Lecturer(Person):

    def __init__(self, name, age, employee_id):
        super().__init__(name, age)
        self.employee_id = employee_id

    def teach_course(self, course):
        print(f"{self.name}has enrolled in {course}")


if __name__ == "__main__":
    s1 = Student("Ama Mensah", 20, "STU2O25001")
    print("---Student Info---")
    s1.display_info()
    s1.enroll_course("Python OOP")
    print()
    I1 = Lecturer("Dr.Kofi Mensah", 45, "EMp10012")
    print("--- Lecturer Info ---")
    I1.display_info()
    I1.teach_course("Software Engineering")





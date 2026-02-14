class Person:
    def __init__(self, name):
        self.name = name


class Student(Person):
    def __init__(self, name, gpa):
        super().__init__(name)
        self.gpa = gpa

    def display(self):
        print(f"Student: {self.name}, GPA: {self.gpa}")


# Ввод
name, gpa = input().split()
gpa = float(gpa)

# Создание объекта
student = Student(name, gpa)

# Вывод
student.display()

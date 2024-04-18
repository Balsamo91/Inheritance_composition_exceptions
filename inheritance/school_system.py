
"""
Simple school system program with OOP.
1. Create Students
2. Create Teachers
3. List all people
"""

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Student(Person):
    def __init__(self, name, age, grade):
        super().__init__(name, age)
        self.grade = grade

    def display(self):
        print(f"Student: {self.name}, Age: {self.age}, Grade: {self.grade}")

class Teacher(Person):
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject

    def display(self):
        print(f"Teacher: {self.name}, Age: {self.age}, Teaches: {self.subject}")

def create_person(type):
    name = input("Enter name: ")
    age = int(input("Enter age: "))

    if type == 'student':
        grade = input("Enter grade: ")
        return Student(name, age, grade)
    elif type == 'teacher':
        subject = input("Enter subject")
        return Teacher(name, age, subject)
    
people = []

while True:
    choice = input("Provide user type you want to create (student/teacher): ")
    if choice.lower() == 'student':
        student = create_person(choice.lower())
        people.append(student)
    elif choice.lower() == 'teacher':
        teacher = create_person(choice.lower())
        people.append(teacher)
    elif choice.lower() == 'exit':
        break
    else:
        print("Invalid option!")

    for person in people:
        person.display()

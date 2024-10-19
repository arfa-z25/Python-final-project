# Base class
class Person:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}, Address: {self.address}")

# Student class inheriting from Person
class Student(Person):
    def __init__(self, name, age, address, student_id, major):
        super().__init__(name, age, address)
        self.student_id = student_id
        self.major = major
        self.courses = []  # List of courses the student is enrolled in
    
    def enroll(self, course):
        self.courses.append(course)
        print(f"{self.name} has enrolled in {course.course_name}")

    def display_student_info(self):
        self.display_info()
        print(f"Student ID: {self.student_id}, Major: {self.major}")
        print("Courses enrolled in:")
        for course in self.courses:
            print(f"- {course.course_name}")

# Teacher class inheriting from Person
class Teacher(Person):
    def __init__(self, name, age, address, employee_id, subject):
        super().__init__(name, age, address)
        self.employee_id = employee_id
        self.subject = subject

    def teach_course(self, course):
        course.assign_teacher(self)
        print(f"{self.name} is now teaching {course.course_name}")

    def display_teacher_info(self):
        self.display_info()
        print(f"Employee ID: {self.employee_id}, Subject: {self.subject}")

# Admin class inheriting from Person
class Admin(Person):
    def __init__(self, name, age, address, admin_id, department):
        super().__init__(name, age, address)
        self.admin_id = admin_id
        self.department = department

    def manage_department(self, department):
        print(f"{self.name} is managing the {department.department_name} department")

    def display_admin_info(self):
        self.display_info()
        print(f"Admin ID: {self.admin_id}, Department: {self.department}")

# New Course class
class Course:
    def __init__(self, course_name, course_code, department):
        self.course_name = course_name
        self.course_code = course_code
        self.department = department
        self.teacher = None

    def assign_teacher(self, teacher):
        self.teacher = teacher
        print(f"{teacher.name} has been assigned to teach {self.course_name}")

    def display_course_info(self):
        print(f"Course: {self.course_name}, Code: {self.course_code}, Department: {self.department.department_name}")
        if self.teacher:
            print(f"Taught by: {self.teacher.name}")

# New Department class
class Department:
    def __init__(self, department_name, department_head):
        self.department_name = department_name
        self.department_head = department_head
        self.courses = []

    def add_course(self, course):
        self.courses.append(course)
        print(f"{course.course_name} has been added to the {self.department_name} department")

    def display_department_info(self):
        print(f"Department: {self.department_name}, Head: {self.department_head}")
        print("Courses offered:")
        for course in self.courses:
            print(f"- {course.course_name}")

# Main flow of the program (testing the system)

# Creating departments
cs_department = Department("Computer Science", "Dr. Jane Doe")
math_department = Department("Mathematics", "Dr. John Smith")

# Creating courses
course1 = Course("Introduction to Programming", "CS101", cs_department)
course2 = Course("Data Structures", "CS201", cs_department)
course3 = Course("Calculus", "MATH101", math_department)

# Adding courses to departments
cs_department.add_course(course1)
cs_department.add_course(course2)
math_department.add_course(course3)

print()

# Creating teacher and assigning to a course
teacher1 = Teacher("Mr. Roberts", 40, "456 College Rd", "T123", "Computer Science")
teacher1.teach_course(course1)

print()

# Creating a student and enrolling in courses
student1 = Student("Alice", 19, "123 Main St", "S456", "Computer Science")
student1.enroll(course1)
student1.enroll(course2)

# Displaying information
print("\nStudent Information:")
student1.display_student_info()

print("\nTeacher Information:")
teacher1.display_teacher_info()

print("\nDepartment Information:")
cs_department.display_department_info()

print("\nCourse Information:")
course1.display_course_info()

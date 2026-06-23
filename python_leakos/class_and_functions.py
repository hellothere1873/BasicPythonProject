class Person:
    def __init__(self, name, age, id_number):
        self.name = name
        self.age = age
        self.id_number = id_number

    def get_attributes(self):
        return f"Name: {self.name}, Age: {self.age}, ID: {self.id_number}"
    

class Student(Person):
    def __init__(self, name, age, id_number):
        super().__init__(name, age, id_number)
        self.grades = {}

    def add_grade(self, grade, course):
        self.grades[course] = grade

    
    def calculate_gpa(self):
        total = sum(self.grades.values())
        count = len(self.grades)
        result = total/count
        return f"GPA of {self.name}, with SID of {self.id_number} == {result}"
    

    def get_attributes(self):
        base = super().get_attributes()
        classes = ", ".join([f"{course}: {grade} " for course, grade in self.grades.items()])
        if not self.grades:
            return f"{base}, No classes have been assigned to this student yet: {classes}"
        else:
            return f"{base}, Classes: {classes}"

class Teacher(Person):
    def __init__(self, name, age, id_number):
        super().__init__(name, age, id_number)
        self.course_teaching = []

    def assign_course(self, course_name):
        self.course_teaching.append(course_name)
        return f"Ok assigned {course_name} to TID: {self.id_number}"
    
    def get_attributes(self):
        base = super().get_attributes()
        classes = (", ".join(self.course_teaching))
        if not self.course_teaching:
            return f"{base}, No classes have been assigned to this teacher yet: {classes}"
        else:
            return f"{base}, Classes they teach: {classes}"
        







class Course():
    def __init__(self):
        self.students = {}
        self.teachers = {}

    def add_student(self, student):
        self.students[student.id_number] = student

    def add_teacher(self, teacher):
        self.teachers[teacher.id_number] = teacher

    def average_grade(self, course):
        total = 0
        count = 0
        for student_id in self.students:
            student = self.students[student_id]  
            if course in student.grades:
                total += student.grades[course]
                count += 1

        if count == 0:
            return f"There's no such course"
            

            
        average = total / count
        return f"Average grade for {course}: {average:.2f}"
            

    def get_attributes(self):
        result = []

        for student in self.students.values():
            result.append(student.get_attributes())

        for teacher in self.teachers.values():
            result.append(teacher.get_attributes())

        return "\n".join(result)



t1 = Teacher("Argy", 50, "T123")
s1 = Student("Argy", 20, "S123")
s2 = Student("bargy", 20, "S133")


s2.add_grade(15, "English")
s1.add_grade(20, "English")
t1.assign_course("English")
print(t1.get_attributes())
print(s1.get_attributes())


my_course = Course()
my_course.add_student(s1)
my_course.add_student(s2)
my_course.add_teacher(t1)

def add_student(name, age, id_number):
    s = Student(name, age, id_number)
    my_course.add_student(s)

def add_teacher(name, age, id_number):
    t = Teacher(name, age, id_number)
    my_course.add_student(t)

def create_course(course_name, teacher_id):
    t = my_course.teachers[teacher_id]
    print(t.assign_course(course_name))
    
def enroll_student(course_name, student_id):
    s = my_course.students[student_id]
    s.add_grade(0 , course_name)
    print("Ok {student_id} enrolled in {course_name}")

def add_grade(student_id, course_name, grade):
    s = my_course.students[student_id]
    s.add_grade(grade , course_name)
    print("Ok {student_id}, has {grade} in course {course_name}")

def print_gpa(student_id):
    s = my_course.students[student_id]
    print(s.calculate_gpa())

def print_course_average(course_name):
    print(my_course.average_grade(course_name))

def updatefile():
    with open("database.txt", "w") as f:
        f.write("Everthing\n")
        f.write(my_course.get_attributes())
        

print_course_average("English")



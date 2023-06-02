# school management system usign python program implement to OOP concept

class Student:
    def __init__(self, id, name, student_class, status) -> None:
        self.id = id
        self.name = name
        self.student_class = student_class
        self.status = status

    def __repr__(self) -> str:
        return repr({
            'id': self.id,
            'name': self.name,
            'student_clas': self.student_class,
            'status': self.status
        })

class Teacher:
    def __init__(self, id, name, subject, status) -> None:
        self.id = id
        self.name = name
        self.subject = subject
        self.status = status

    def __repr__(self) -> str:
        return repr({
            'id': self.id,
            'name': self.name,
            'subject': self.subject
        })
    
class School:
    def __init__(self, name) -> None:
        self.name = name
        self.teachers = []
        self.students = []

    def add_teacher(self, id, name, subject, status):
        teacher = Teacher(id, name, subject, status)
        self.teachers.append(teacher)

    def enroll(self, name, student_class, status, fee):
        if(fee < 6500):
            print(f'student {name} not enough fee, you need {6500 - fee} more')
        else:
            id = len(self.students) + 1
            student = Student(id, name, student_class, status)
            extra = fee - 6500
            student.__dict__['fees'] = fee - extra
            self.students.append(student.__dict__)
            print(f'Student {student.name} enrolled success, here your exatra mony returned: {fee - 6500}')

    def __repr__(self) -> str:
        print(f'-----------------Welcome to {self.name}-----------------')

        print(f'----------------Ouer teachers---------------------')
        for teacher in self.teachers:
            print(teacher)

        print(f'----------------Ouer students---------------------')
        for student in self.students:
            print(student)
        return 'All done for now'

# starting object created here 
student = Student('144369', 'Habibor Rahaman', 'Bsc in CSE', 'student')
teacher = Teacher('672736', 'guido van russam', 'python programming language', 'teacher')

print(student.__dict__)
print(teacher.__dict__)

for key, value in student.__dict__.items():
    print(f'{key}: {value}')

print('\n')

for key, value in teacher.__dict__.items():
    print(f'{key}: {value}')

school = School('Bright school')
school.add_teacher(123123, 'Habibor Rahaman', 'Data Stucture', 'CSE Teacher')
school.add_teacher(123123, 'Apurbo shaha', 'Data Stucture', 'CSE Teacher')
school.add_teacher(123123, 'Mahir Shahriar', 'Algorithm', 'CSE Teacher')

school.enroll('Habibor Rahaman', 'Bsc in CSE', 'student', 6900)
school.enroll('Abdue Rahaman Rifat', 'Bsc in EEE', 'student', 6700)
school.enroll('Arafat shuvo', 'Bsc in EEE', 'student', 6500)

print(school)

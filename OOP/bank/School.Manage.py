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
        if(fee <= 6500):
            print(f'not enough fee, you need {6500 - fee} more')
        else:
            id = len(self.students) + 1
            student = Student(id, name, student_class, status)
            student.__dict__['fees'] = fee
            self.students.append(student.__dict__)
            print(f'Student enrolled success, here your exatra mony returned: {fee - 6500}')




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
school.enroll('Habibor Rahaman', 'Bsc in CSE', 'student', 6700)
print(school.teachers)
print(school.students)

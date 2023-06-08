# School managment systrm in python

class School:
    def __init__(self, name, address, email, phone, created) -> None:
        self.name = name
        self.address = address
        self.email = email
        self.phone = phone
        self.created = created
        self.teachers = {}
        self.classrooms = {}

    def add_classroom(self, classroom):
        self.classrooms[classroom.name] = classroom

    def add_techer(self, subject, teacher):
        self.teachers[subject] = teacher

    def student_admission(self, student):
        className = student.classroom.name
        if className in self.classrooms:
            self.classrooms[className].add_student(student)

        else:
            print(f'No classroom as name {className}') 

    @staticmethod
    def calcualte_grade(marks):
        if 80 <= marks <= 100:
            return 'A+'
        elif 70 <= marks <= 80:
            return 'A'
        elif 60 <= marks <= 70:
            return 'A-'
        elif 50 <= marks <= 60:
            return 'B'
        elif 40 <= marks <= 50:
            return 'C'
        elif 33 <= marks <= 40:
            return 'D'
        else:
            return 'F'
        
    @staticmethod
    def grade_to_value(grade):
        grade_map = {
            'A+': 5.00,
            'A': 4.00,
            'A-': 3.50,
            'B': 3.00,
            'C': 2.00,
            'D': 1.00,
            'F': 0.00,
        }
        return grade_map[grade]
    
    @staticmethod
    def value_to_grade(value):
        if 4.5 <= value <= 5.00:
            return 'A+'
        elif 3.5 <= value <= 4.5:
            return 'A'
        elif 3.00 <= value <= 3.5:
            return 'A-'
        elif 2.5 <= value <= 3.0:
            return 'B'
        elif 2.0 <= value <= 2.5:
            return 'C'
        elif 1.0 <= value <= 2.0:
            return 'D'
        else:
            return 'F'

    def __repr__(self) -> str:
        print('----------ALL CLASSROOM------------')
        for key, valu in self.classrooms.items():
            print(key)

        print('----------------STUDENTS-------------')
        eight = self.classrooms['eight']
        print(len(eight.students))
        for student in eight.students:
            print(f'name: {student.name}')

        print('------------SUBJECTS---------------')
        for subjec in eight.subjects:
            print(f'subject: {subjec.name} \t teache: {subjec.teacher.name}')
        
        print('--------------STUDENTS EXAM MARKS---------------')
        for student in eight.students:
            for key, valu in student.marks.items():
                print(f'name: {student.name} {key} : {valu} grade: {student.subject_grade[key]}')
            print('\n')
        return ''

class ClassRoom:
    def __init__(self, name, ) -> None:
        self.name = name
        self.students = []
        self.subjects = []

    def add_student(self, student):
        serial_id = f'{self.name} - {len(self.students) + 1}'
        student.id = serial_id
        student.classroom = self.name
        self.students.append(student)

    def add_subject(self, subject):
        self.subjects.append(subject)

    def take_semester_final(self):
        #take exam
        for subject in self.subjects:
            subject.exam(self.students)

        # calculate final grade
        for student in self.students:
            student.calculate_final_grade()

    def __str__(self) -> str:
        return f'{self.name} - {len(self.students)}'
    
    def get_top_student(self):
        pass

class Subject:
    def __init__(self, name, teacher) -> None:
        self.name = name
        self.teacher = teacher
        self.max_marks = 100
        self.pass_marks = 40

    def exam(self, students):
        for student in students:
            mark = self.teacher.evaluate_exam()
            student.marks[self.name] = mark
            student.subject_grade[self.name] = School.calcualte_grade(mark)
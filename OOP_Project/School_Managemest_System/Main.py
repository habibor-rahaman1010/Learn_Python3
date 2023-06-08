from School import School, ClassRoom, Subject
from Person import Student, Teacher


def Main():
    school = School('Rajdia Avoy', 'Rajdia Serajdikhan Munshiganj', 'rajsiaavoy12@gmail.com', '0178237823', 1918)

    eight = ClassRoom('eight')
    school.add_classroom(eight)
    nine = ClassRoom('nine')
    school.add_classroom(nine)
    ten = ClassRoom('ten')
    school.add_classroom(ten)

    # students
    student_1 = Student('Nafiz rafsan', eight)
    school.student_admission(student_1)
    
    student_2 = Student('Mafuz', eight)
    school.student_admission(student_2)
    
    student_3 = Student('Allen Souvo', eight)
    school.student_admission(student_3)

    #subject
    physics_teacher = Teacher('Nikhil Sir')
    physics = Subject('Physics', physics_teacher)
    eight.add_subject(physics)

    data_stucture_teacher = Teacher('Aburpu Shaha')
    data_stucture = Subject('Data Stucture', data_stucture_teacher)
    eight.add_subject(data_stucture)

    algorithm_teacher = Teacher('Mahir shahariar')
    algorithm = Subject('Algorithm', algorithm_teacher)
    eight.add_subject(algorithm)

    # take exam here
    eight.take_semester_final() 

    print(school)


if __name__ == '__main__':
    Main()
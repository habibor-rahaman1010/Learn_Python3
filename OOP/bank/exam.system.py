#exam system implement using python...

class AnualExam:
    def __init__(self, name, examAttend, subject) -> None:
         self.name = name
         self.examAttend = examAttend
         self.subject = subject

    def examStartTime(self):
         print(f'Exam starting time {10}:am') 
    
    def examEndTime(self):
        print(f'Exam ending time {1}:am') 

    def examiner(self):
         print(f'Exam attend {self.examAttend} students.')

    def attentNewExaminner(self, attend):
         self.examAttend += attend
         
              
         

my_exam = AnualExam('Annual Exam', 35, 'Data Stucture')
my_exam.examStartTime()
my_exam.examEndTime()
my_exam.examiner()
my_exam.attentNewExaminner(29)
my_exam.examiner()
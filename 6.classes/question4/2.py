class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
 
        
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
 
best_student = Student()
best_student.name = 'Ruoy'
best_student.surname = 'Eman'
best_student.gender = 'your_gender'
best_student.finished_courses += ['Git']
best_student.courses_in_progress += ['Python']
best_student.grades['Git'] = [10, 10, 10, 10, 10]
best_student.grades['Python'] = [10, 10]
 
print(best_student.finished_courses)
print(best_student.courses_in_progress)
print(best_student.grades)
 
cool_mentor = Mentor()
cool_mentor.name = 'Some'
cool_mentor.surname = 'Buddy'
cool_mentor.courses_attached += ['Python']
print(cool_mentor.courses_attached)
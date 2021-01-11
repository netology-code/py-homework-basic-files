class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
 
    def add_courses(self, course_name):
        self.finished_courses.append(course_name)    
 
 
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        
    def rate_hw(self, student, course, grade):
        student.grades[course] = [grade]
 
        
best_student = Student('Ruoy', 'Eman', 'your_gender')
cool_mentor = Mentor('Some', 'Buddy')
cool_mentor.rate_hw(best_student, 'Python', 10)
 
print(best_student.grades)

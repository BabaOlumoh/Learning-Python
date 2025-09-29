import statistics
class Student:
    def __init__(self, name, student_id, grades):
        self.name = name
        self.student_id = student_id
        self.grades = grades
        
    def add_grade(self, subject, score):
        self.grades.update({subject:score})

    def calculate_average(self):
        result = statistics.mean(list(self.grades.values()))
        return result

    def display_info(self):
        return f"Name: {self.name}, Student_ID: {self.student_id}, Grades: {self.grades}, Average: {self.calculate_average()}"
        
    def __str__(self):
        return f"{self.name} - {self.student_id}: {self.grades}"

class School:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def show_all_students(self):
        for student in self.students:
            print(student)

    def find_student(self, student_id):
        for student in self.students:
            if student_id == student.student_id:
                print(student)
                return True
        print(f"{student_id} not found")
        return False

john = Student("John", "MAT001", {"Math": 85, "English": 90, "Science": 78, "History": 88})
mary = Student("Mary", "MAT002", {"Math": 70, "English": 82, "Science": 75, "History": 80})
david = Student("David", "MAT003", {"Math": 95, "English": 89, "Science": 92, "History": 94})
sarah = Student("Sarah", "MAT004", {"Math": 60, "English": 65, "Science": 58, "History": 62})
grace = Student("Grace", "MAT005", {"Math": 78, "English": 85, "Science": 80, "History": 76})

model = School()
model.students = [john, mary, david, sarah, grace]
mel = Student("Mel", "MAT006", {"Math": 90, "English": 95, "Science": 82, "History": 83})
model.add_student(mel)
model.show_all_students()
model.find_student("MAT007")
mel.calculate_average()
john.display_info()
john.add_grade("Math", 90)
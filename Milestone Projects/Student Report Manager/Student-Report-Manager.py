import statistics
import datetime
class Student:
    def __init__(self, name, student_id, grades, average):
        self.name = name
        self.student_id = student_id
        self.grades = grades
        self.average = average

    def add_grade(self, subject, score):
        self.grades.update({subject:score})

    def calculate_average(self):
        self.average = statistics.mean(list(self.grades.values()))
        return self.average

    def display_info(self):
        return f"Name: {self.name} | Student_ID: {self.student_id} | Grades: {self.grades} | Average {self.average}" 

    def generate_report(self):
        getdate = datetime.datetime.now()
        title = getdate.strftime("%Y%m%d")
        with open(f"singlereport{title}.txt", "a+") as f:
            f.write(Student.display_info(self))

    def __str__(self):
        return f"{self.name} {self.student_id} {self.average}"
        

class School:
    def __init__(self):
        self.students= []

    def add_student(self, student):
        self.students.append(student)

    def show_all_students(self):
        for student in self.students:
            print(student.display_info())

    def find_student(self, student_id):
        for student in self.students:
            if student_id == student.student_id:
                print(student.display_info())
                return None
        print(f"{student_id} not found!")
        return None

    def generate_all_reports(self):
        gen_getdate = datetime.datetime.now()
        gen_title = gen_getdate.strftime("%Y%m%d")
        for student in self.students:
            with open(f"report{gen_title}.txt", "a+") as f:
                f.write(f"{student.display_info()}\n")

    def back_reports(self):
        pass

    def delete_all_reports(self):
        pass

john = Student("John", "MAT001", {"Math": 85, "English": 90, "Science": 78, "History": 88}, 0)
mary = Student("Mary", "MAT002", {"Math": 70, "English": 82, "Science": 75, "History": 80}, 0)
david = Student("David", "MAT003", {"Math": 95, "English": 89, "Science": 92, "History": 94}, 0)
sarah = Student("Sarah", "MAT004", {"Math": 60, "English": 65, "Science": 58, "History": 62}, 0)
grace = Student("Grace", "MAT005", {"Math": 78, "English": 85, "Science": 80, "History": 76}, 0)

model = School()
model.students = [john, mary, david, sarah, grace]
mel = Student("Mel", "MAT006", {"Math": 83, "English": 90, "Science": 85, "History": 81}, 0)


def menu():
    print("1. Add student \n2. Add grade to student \n3. Show all student \n4. Generate all reports \n5. Backup reports \n6. Delete all reports \n7. Quit \nChoose option between 1-7: ")

starter = True
while starter:
    try:
        menu()
        user_choice = int(input())
        if user_choice == 1:
            model.add_student(mel)
            print("Done")
        elif user_choice == 2:
            john.add_grade("Chem", 7)
            print("Done")
        elif user_choice == 3:
            model.show_all_students()
        elif user_choice == 4:
            model.generate_all_reports()
        elif user_choice == 5:
            model.back_reports()
        elif user_choice == 6:
            model.delete_all_reports()
        elif user_choice == 7:
            starter = False
        else:
            print("Invalid option")
    except:
        print("Invalid Input!!! \nEnter digit between 1-7 only")
    


# Manages a collection of students and their grades
class SiliconStudents:

    def __init__(self):
        # Maps student name -> list of letter grades
        students = {}
        self.students = students

    def add_student(self, student):
        # Store the student's grades keyed by their name
        self.students[student.name] = student.grades

    def remove_student(self, name):
        # Delete a student record by name
        del self.students[name]

    def print_names_and_gpa(self):
        # Assumes all students are enrolled in the same number of classes
        total_number_of_classes = 6
        for name in self.students:
            grades = self.students[name]
            grade_count_value = 0
            # Convert each letter grade to its 4.0-scale point value
            for grade in grades:
                if grade == "A":
                    grade_count_value += 4
                if grade == "B":
                    grade_count_value += 3
                if grade == "C":
                    grade_count_value += 2
                if grade == "D":
                    grade_count_value += 1
                if grade == "F":
                    grade_count_value += 0

            # Divide total points by class count to get GPA
            gpa = round(grade_count_value / total_number_of_classes, 2)
            print(f"Name: {name} -- GPA: {gpa}")
   
        


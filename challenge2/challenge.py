from student import Student
from silicon_students import SiliconStudents


if __name__ == "__main__":

    #Create 3 students along with associated grades
    student_one_grades = ["A", "B", "B", "C", "A", "D"]
    student_one = Student("Jeff", student_one_grades)

    student_two_grades = ["B", "B", "F", "C", "A", "C"]
    student_two = Student("Vader", student_two_grades)

    student_three_grades = ["A", "A", "B", "A", "A", "A"]
    student_three = Student("Lisa", student_three_grades)

    #Initiate the students class
    ss = SiliconStudents() 

    #Add all the students
    print("All Students....")
    ss.add_student(student_one)
    ss.add_student(student_two)
    ss.add_student(student_three)
    
    #Print out all students and GPAs
    ss.print_names_and_gpa()

    #Remove one student
    print("\nRemove Vader...")
    ss.remove_student("Vader")

    #Reprint students and GPAs
    print("\n")
    ss.print_names_and_gpa()
   





# create a class of student
class Student:
    # create a class variable for the student class
    student_year = 2026
    num_students = 0

    # declares a constructor for the student class
    def __init__(self,name,age):
        self.name = name
        self.age = age
        # this gets the numbers of the students in the school
        Student.num_students += 1

# create an instance of the class student
st1 = Student("George", 22)
st2 = Student("Matthew", 23)
st3 = Student("Bob", 24)

# let's print the total number of students in the school
print(f"There are {Student.num_students} Students Admitted in the school")
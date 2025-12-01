# Grade Calculator
# Problem: Assign a letter grade based on a student's scores: A(90-100), B(80-89), C(70-79), D(60-69), F(below 60)

student_grade = int(input("Enter your grade: "))
if student_grade >= 90 and student_grade <= 100:
    print("You got Grade A")
elif student_grade >= 80 and student_grade < 90:
    print("You got Grade B")
elif student_grade >= 70 and student_grade < 80:
    print("You got Grade C")
elif student_grade >= 60 and student_grade < 70:
    print("You got Grade D")
else:
    print("You got Grade F")

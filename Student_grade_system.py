# Student Grade System

name = input("Enter student name: ")
marks = float(input("Enter marks (0-100): "))

if marks >= 90:
    grade = "A"
elif marks >= 75:
    grade = "B"
elif marks >= 50:
    grade = "C"
elif marks >= 35:
    grade = "D"
else:
    grade = "Fail"

print("\nStudent Name:", name)
print("Marks:", marks)
print("Grade:", grade)

from student import student 
# from (file) import (class)

student1 = student("Jim", "Business", 3.1, False)
student2 = student("Pam", "Arts", 2.5, True)

print(student1.name)
print(student1.major)
print(student1.gpa)
print(student1.probation)

print(student2.name)
print(student2.major)
print(student2.gpa)
print(student2.probation)
print(student2.on_honor_roll())
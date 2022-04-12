import shutil

#"r": Read the file; "w":Write the file
#"a":Append the file/ad info; "r+":Read and Write info

open("empleados.txt", "w") # create new file in the folder
employee_file = open("employees.txt", "r") # original
shutil.copyfile("employees.txt", "empleados.txt")
empleados_file = open("empleados.txt", "a") # copy

print(employee_file.readable()) #True or False
print(employee_file.read())
#print(employee_file.readlines())
#for employee in employee_file.readlines():
#    print(employee)

empleados_file.write("\nToby - Human Resources")

employee_file.close()
empleados_file.close()

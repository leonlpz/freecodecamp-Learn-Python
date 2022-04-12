def say_hi(name, age):
    print("Hello " + name + "you are " + str(age))

def cube(num):
    print("The third power of " + str(num) + " is =")
    return num**3

say_hi("Mike, ", 35)

result = cube(4)
print(result)
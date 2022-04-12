a = 2**3

def raise_to_power(base_num, pow_num):
    result = 1
    for index in range(pow_num):
        result = result * base_num
    return result

num1 = input("Enter the base number: ")
num2 = input("Enter the power number: ")
print("The result is: " + str(raise_to_power(int(num1), int(num2))))
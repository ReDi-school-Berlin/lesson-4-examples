# A function that does not return a value
def greet(name):
    print("Hello " + name)

greet("Harika")
greet("Bende")
x = greet("Harika")
print(x) #prints None, because the function does not return anything


def sum_two_numbers(num1, num2):
    return num1 + num2 

def sum_three_numbers(num1, num2, num3):
    return num1 + num2 + num3

x = sum_two_numbers(4,3)
print(x)


y = sum_three_numbers(6,7,8)
print(y)
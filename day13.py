# A function with parameters and return value

def greet_user(name):
    greeting = f"Hello, {name}! You’re doing amazing!"
    return greeting

# Use the function
user_name = input("Enter your name: ")
message = greet_user(user_name)
print(message)


# A function to add two numbers and return the result
def add_numbers(x, y):
    return x + y


# Using the function
num1 = float(input("Enter a number: "))
num2 = float(input("Enter another number: "))
result = add_numbers(num1, num2)
print(f"The sum is: {result}")


# new function - challenge
def multiply_numbers(a, b)
    return (a*b)

# Call the function
num3 = float(input("Enter a number to multiply: "))
num4 = float(input("Enter another number to multiply: "))
product = multiply_numbers(num3, num4)
print(f"The product is: {product}")

# Function to add two numbers
def add_numbers(a, b):
    return a + b

# Input: two numbers
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# Adding the numbers
result = add_numbers(num1, num2)

# Output the result
print("The sum of {} and {} is {}".format(num1, num2, result))

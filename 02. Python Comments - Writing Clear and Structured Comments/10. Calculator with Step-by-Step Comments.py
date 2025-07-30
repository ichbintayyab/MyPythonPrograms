# Simple calculator that adds, substract, multiplies, and divides two numbers.

# Get first number
num1 = float(input("Enter first number: "))

# Get second number
num2 = float(input("Enter second number: "))

# Ask the user to choose an operation
print("Choose operation:")
print("1. Addition")
print("2. Substraction")
print("3. Multiplication")
print("4. Division")

choice = input("Enter choise (1/2/3/4): ")

# Perform operation based on user's choise
if choice == '1':
    result = num1 + num2 # Add numbers
    print("Result:", result)
elif choice == '2':
    result = num1 - num2 # Substract numbers
    print("Result:", result)
elif choice == '3':
    result = num1 * num2 # Multiply numbers
    print("Result:", result)
elif choice == '4':
    if num2 != 0:
        result = num1 / num2 # Divide numbers
        print("Result:", result)
    else:
        print("Error: Cannot divided by 0")
else:
    print("Invalid Choice!")

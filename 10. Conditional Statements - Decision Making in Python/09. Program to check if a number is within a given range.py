# Input from user
number = int(input("Enter a number: "))

# Define the range
start = 10
end = 100

# Check if number is within range
if start <= number <= end:
    print(f"The number is within the range {start} to {end}.")
else:
    print(f"The number is outside the range {start} to {end}.")
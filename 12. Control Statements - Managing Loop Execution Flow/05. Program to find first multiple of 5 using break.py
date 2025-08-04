# Example: Find and print first multiple of 5 from a lit

numbers = [3, 7, 8, 10, 15, 20]

for num in numbers:
    if num % 5 == 0: # Check if multiple of 5
        print("First multiple of 5 is:", num)
        break # Stop after finding the first one
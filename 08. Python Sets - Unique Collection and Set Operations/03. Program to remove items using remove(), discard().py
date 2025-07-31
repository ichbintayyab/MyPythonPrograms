# Creating a set of numbers
numbers = {10, 20, 30, 40, 50}

# Using remove() - will raise an error if the item doesn't exist
numbers.remove(20)

# Printing the result
print("Number after using remove():", numbers)

# Using discard() - will NOT raise and error if the item doesn't exist
numbers.discard(10)    # This won't give any error

# Displaying the updated set
print("Updated set:", numbers)
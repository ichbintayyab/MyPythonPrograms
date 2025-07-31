# Creating a list of numbers
numbers = [1, 2, 3, 4, 5]

# Removing a specific item using remove()
numbers.remove(3)   # Removes the number 3

# Removing the last item using pop()
last_item = numbers.pop()

# Printing the updated list
print("Updated list after remove and pop:", numbers)
print("Item removed using pop()", last_item)
# Global variable
counter = 0

def increase_counter():
    global counter # Declare that we are using the global variable
    counter += 1

# Call function multiple times
increase_counter()
increase_counter()
increase_counter()

# Print updated global variable
print("Counter after function calls:", counter)
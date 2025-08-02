# Tuples are immutable - we cannot change their elements
numbers = (1, 2, 3)

# Trying to change the first element (will raise an error)
try:
    numbers[0] = 10
except TypeError as e:
    print("Error:", e)
# This is a regular comment: it is ignored by Python

def divide(a, b):
    """
    This is a docstring: it describes the function
    and can be accessed using help() or print(funtion_name.__doc__)
    """
    return a / b
# You cannot access single-line comment using help()
help(divide)
print(divide(10, 5)) # Output: 2.0
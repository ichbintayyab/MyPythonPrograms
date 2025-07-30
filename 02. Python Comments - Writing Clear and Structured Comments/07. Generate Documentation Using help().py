def substract(x, y):
    """
    Substracts y from x and return the result

    parameters:
    x (int): First number
    y (int): Second number

    returns:
    int: result of substraction
    """
    return x - y
# Print documention using help
help(substract) # This shows __docstring__
# We can also access docstring using:
# print(substract.__doc__) # This shows __docstring__
print(substract(10, 2)) # Output: 8



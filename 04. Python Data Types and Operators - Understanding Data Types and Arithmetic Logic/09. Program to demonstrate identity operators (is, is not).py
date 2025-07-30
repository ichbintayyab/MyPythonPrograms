# Indentify Operators
a = [1, 2, 3]
b = a
c = [1, 2, 5]

print("a is b:", a is b)            # True, both refer to the same object
print("a is c:", a is c)            # False, different objects with same values
print("a is not b:", a is not b)
print("a is not c:", a is not c)
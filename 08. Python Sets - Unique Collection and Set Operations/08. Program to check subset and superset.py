# Creating two sets
set1 = {1, 2, 3}
set2 = {1, 2, 3, 4, 5}

# Checking if set1 is a subset of set2 using .issubset()
print("Is set1 a subset of set2?", set1.issubset(set2))

# Checking if set1 is a superset of set2 using .issuperset()
print("Is set1 a superset of set2?", set2.issuperset(set1))
# Creating two sets
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

# Performing difference: element in set1 not in set 2 - Method 1
difference_set = set1 - set2

# Displaying the result
print("Difference of set1 and set2:", difference_set)

# Another method to performing difference using .difference() - Method 2
print("Difference of set1 and set2 using .difference():", set1.difference(set2))


# Creating two sets
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

# Performing intersection using & - Method 1
intersection_set = set1 & set2

# Displaying the result
print("Intersection of set1 and set2:", intersection_set)

# Another method to performing intersection using .intersection() - Method 2
print("Intersection of set1 and set 2 using .intersection():", set1.intersection(set2))
# Creating dictionary of a student
student = {
    "Name": "Sandman",
    "Age": 20,
    "Gender": "Male"
}

# Using pop() to remove 'grade'
removed_gender = student.pop("Gender")
print("Removed grade:", removed_gender)
print("Student info:", student)

# Using popitem() to remove the last inserted item
last_item = student.popitem()
print("Last item removed:", last_item)

# Final dictionary
print("Final Dictionary:", student)
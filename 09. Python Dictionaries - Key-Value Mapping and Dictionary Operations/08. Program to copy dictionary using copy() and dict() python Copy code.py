# Original Dictionary
person = {
    "name": "Sandman",
    "age": 20
}

# First copy using copy()
copy1 = person.copy()

# Second copy using dict()
copy2 = dict(person)

# Print both copies
print("Copy using copy():", copy1)
print("Copy using dict():", copy2)
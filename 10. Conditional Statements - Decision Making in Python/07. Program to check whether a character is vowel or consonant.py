# Input from user
char = input("Enter a single alphabet: ")

# Convert to lowercase for easy comparison
char = char.lower()

# Check if it's is vowel
if char in ('a', 'e', 'i', 'o', 'u'):
    print(f"{char} is a vowel.")
else:
    print(f"{char} is a consonant.")
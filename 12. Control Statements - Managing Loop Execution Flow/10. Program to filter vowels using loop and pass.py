# Example: Print only consonants from a string

text = "Hello World"

for char in text:
    if char.lower() in "aeiou": # Check if vowel
        pass # Do nothing for vowels
    else:
        print(char)
# Example: Skip number 5 in the loop

for number in range(1, 11):
    if number == 5:
        continue # Skip the rest of this iteration and go to the next
    print(number) # This will not print when number is 5
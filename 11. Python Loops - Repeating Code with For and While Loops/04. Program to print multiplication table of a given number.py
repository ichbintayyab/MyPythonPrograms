number = int(input("Enter a number: "))

print("Multiplication Table for", number)
for i in range(1, 11): # Loop from 1 to 10
    print(f"{number} x {i} = {number * i}")
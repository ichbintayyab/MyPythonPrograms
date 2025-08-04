# Example: Break only inner loop when condition is met

for i in range(1, 4):  # Outer loop
    for j in range(1, 6):  # Inner loop
        print(f"i = {i}, j = {j}")
        if j == 3:
            print("Breaking inner loop")
            break  # Only breaks the inner loop

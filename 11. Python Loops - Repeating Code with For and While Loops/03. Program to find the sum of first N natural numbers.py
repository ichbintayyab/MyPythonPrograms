N = int(input("Enter a postive number: "))
total_sum = 0

for num in range(1, N + 1):
    total_sum += num # Add each number to the sum

print("Sum of first", N, "natural number is:", total_sum)
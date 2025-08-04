start = int(input("Enter start of range: "))
end = int(input("Enter end of range: "))

print("Prime numbers between", start, "and", end, "are:")

for num in range(start, end + 1):
    if num > 1: # Prime numbers are greater than 1
        is_prime = True
        for i in range(2, int(num ** 0.5) + 1): # Check divisors up to sqrt(num)
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            print(num)

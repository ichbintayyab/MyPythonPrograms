number = int(input("Enter a number: "))
reverse_num = 0

while number > 0:
    digit = number % 10     # Get the last number
    reverse_num = reverse_num * 10 + digit
    number //= 10           # Remove the last digit

print("Reversed number is:", reverse_num)
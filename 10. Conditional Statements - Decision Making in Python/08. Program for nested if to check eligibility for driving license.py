# Input from user
age = int(input("Enter your age: "))
has_id = input("Do you have a valid ID? (yes/no): ").lower()

# Check if eligible to vote
if age >= 18:
    if has_id == 'yes':
        print("You are eligible for a driving license.")
    else:
        print("You ust have a Valid ID to apply for a license.")
else:
    print("You are not eligible for a driving license.")
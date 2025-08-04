# Example: Else runs only if while loop ends normally (not by break)

count = 1
while count <= 5:
    print(count)
    count += 1
else:
    print("While loop completed without break.")
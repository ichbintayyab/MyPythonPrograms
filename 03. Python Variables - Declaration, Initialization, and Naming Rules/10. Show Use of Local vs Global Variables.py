# Global variable
value = 50

def show_local():
    value = 100 # Local variable with the same name
    print("Inside function (local):", value)

show_local()
print("Outside function (globale)", value)
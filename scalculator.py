import math

def sqrt(x):
    return math.sqrt(x)

def factorial(x):
    return math.factorial(int(x))

def ln(x):
    return math.log(x)

def power(x, b):
    return math.pow(x, b)

while True:
    print("\nScientific Calculator")
    print("1. Square Root")
    print("2. Factorial")
    print("3. Natural Log")
    print("4. Power")
    print("5. Exit")
    choice = input("Enter choice: ")
    if choice == '5':
        break
    if choice == '1':
        x = float(input("Enter number: "))
        print(f"Square root of {x} is {sqrt(x)}")
    elif choice == '2':
        x = float(input("Enter number: "))
        print(f"Factorial of {x} is {factorial(x)}")
    elif choice == '3':
        x = float(input("Enter number: "))
        print(f"Natural log of {x} is {ln(x)}")
    elif choice == '4':
        x = float(input("Enter base: "))
        b = float(input("Enter exponent: "))
        print(f"{x} raised to the power of {b} is {power(x, b)}")
    else:
        print("Invalid choice")
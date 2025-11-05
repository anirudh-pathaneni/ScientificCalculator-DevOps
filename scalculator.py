import math

def sqrt(x):
    if x < 0:
        print("Invalid input: Square root not defined for negative numbers")
        return None
    return math.sqrt(x)

def factorial(x):
    if x < 0:
        print("Invalid input: Factorial not defined for negative numbers")
        return None
    if not x.is_integer():
        print("Invalid input: Factorial is only defined for whole numbers")
        return None
    return math.factorial(int(x))

def ln(x):
    if x <= 0:
        print("Invalid input: Natural logarithm not defined for zero or negative numbers")
        return None
    return math.log(x)

def power(x, b):
    return math.pow(x, b)


def calculator():
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
            result = sqrt(x)
            if result is not None:
                print(f"Square root of {x} is {result}")
        elif choice == '2':
            x = float(input("Enter number: "))
            result = factorial(x)
            if result is not None:
                print(f"Factorial of {x} is {result}")
        elif choice == '3':
            x = float(input("Enter number: "))
            result = ln(x)
            if result is not None:
                print(f"Natural log of {x} is {result}")
        elif choice == '4':
            x = float(input("Enter base: "))
            b = float(input("Enter exponent: "))
            result = power(x, b)
            if result is not None:
                print(f"{x} raised to the power of {b} is {result}")
        else:
            print("Invalid choice")

if __name__ == "__main__":
    calculator()
#Test
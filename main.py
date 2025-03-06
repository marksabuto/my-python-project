# main.py
def greet(name):
    return f"Hello, {name}!"

if __name__ == "__main__":
    user_name = input("Enter your name: ")
    print(greet(user_name))

    # main.py

def greet(name):
    return f"Hello, {name}!"

def add_numbers(a, b):
    return a + b

def is_even(number):
    return number % 2 == 0

def menu():
    print("Welcome to My Python Project!")
    print("1. Greet me")
    print("2. Add two numbers")
    print("3. Check if a number is even or odd")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")
    return choice

if __name__ == "__main__":
    while True:
        choice = menu()

        if choice == "1":
            name = input("Enter your name: ")
            print(greet(name))
        elif choice == "2":
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            result = add_numbers(num1, num2)
            print(f"The sum is: {result}")
        elif choice == "3":
            number = int(input("Enter a number: "))
            if is_even(number):
                print(f"{number} is even.")
            else:
                print(f"{number} is odd.")
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

# main.py

def greet(name):
    return f"Hello, {name}!"

def add_numbers(a, b):
    return a + b

def is_even(number):
    return number % 2 == 0

def calculator():
    print("\nCalculator")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Back to main menu")

    operation = input("Choose an operation (1-5): ")
    if operation == "5":
        return

    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    if operation == "1":
        result = add_numbers(num1, num2)
        print(f"The sum is: {result}")
    elif operation == "2":
        result = num1 - num2
        print(f"The difference is: {result}")
    elif operation == "3":
        result = num1 * num2
        print(f"The product is: {result}")
    elif operation == "4":
        if num2 == 0:
            print("Error: Cannot divide by zero!")
        else:
            result = num1 / num2
            print(f"The quotient is: {result}")
    else:
        print("Invalid operation. Please try again.")

def menu():
    print("\nWelcome to My Python Project!")
    print("1. Greet me")
    print("2. Add two numbers")
    print("3. Check if a number is even or odd")
    print("4. Calculator")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")
    return choice

if __name__ == "__main__":
    while True:
        choice = menu()

        if choice == "1":
            name = input("Enter your name: ")
            print(greet(name))
        elif choice == "2":
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            result = add_numbers(num1, num2)
            print(f"The sum is: {result}")
        elif choice == "3":
            number = int(input("Enter a number: "))
            if is_even(number):
                print(f"{number} is even.")
            else:
                print(f"{number} is odd.")
        elif choice == "4":
            calculator()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
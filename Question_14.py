# Q14: Menu-driven program

while True:
    print("\n--- MENU ---")
    print("1. Add")
    print("2. Subtract")
    print("3. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))
        print("Result:", a + b)

    elif choice == 2:
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))
        print("Result:", a - b)

    elif choice == 3:
        print("Exiting...")
        break

    else:
        print("Invalid choice!")
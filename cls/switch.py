choice = input("Enter operation (+, -, /, %): ")

a = int(input("Enter a value: "))
b = int(input("Enter a value: "))

if choice == "+":
    print("Sum:", a + b)

elif choice == "-":
    print("Sub:", a - b)

elif choice == "/":
    print("Div:", a / b)

elif choice == "%":
    print("Mod:", a % b)

else:
    print("Invalid choice")

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

if __name__ == "__main__":
    print("Simple Calculator")
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    print("Select operation:")
    print("1. Addition")
    print("2. Subtraction")
    choice = input("Enter choice (1/2): ")

    if choice == '1':
        print("Result: ", add(num1, num2))
    elif choice == '2':
        print("Result: ", subtract(num1, num2))
    else:
        print("Invalid choice")

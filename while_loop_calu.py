while True:
    print("Select an option: ")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")

    choice = input("Enter choice (1/2/3/4/5): ")

    if choice == '5':
        print("Exiting the program.")
        break
    elif choice == '1':
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        add = num1+num2
        print("The sum of two number is ",add)
    elif choice == '2':
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        sub = num1-num2
        print("The sub of two number is ",sub)
        
    elif choice == '3':
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        mul = num1*num2
        print("The mul of two number is ",mul)
    elif choice == '4':
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        div = num1/num2
        print("The sub of two number is ",div)
    
    else:
        print("Invalid input. Please try again.")
        break
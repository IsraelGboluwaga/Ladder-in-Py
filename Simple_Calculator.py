def go_back():
    print "Press enter to continue"
    user_input_2 = raw_input(": ")
    if user_input_2 == "":
        calc()

def calc():
    while True:
        print("Options")
        print("Enter 'add' to add two numbers")
        print("Enter 'minus' to find the difference between two numbers")
        print("Enter 'multiply' to multiply two numbers (Product)")
        print("Enter 'divide' to divide two numbers")
        print("To continue, press selected option, then enter || To exit, enter 'quit'")
        user_input = raw_input(": ")
        if user_input.lower() == "quit":
            break
        elif user_input == "":
            print "Please select an option"
            calc()
        elif user_input.lower() == "add":
            num1= float(input("Enter first number: "))
            num2= float(input("Enter second number: "))
            result = num1 + num2
            print("The sum of the two numbers is " + str(result))
            go_back()
        elif user_input.lower() == "minus":
            num1= float(input("Enter first number: "))
            num2= float(input("Enter second number: "))
            result = num1 - num2
            print("The difference between the two numbers is "+ str(result))
            go_back()
        elif user_input.lower() == "multiply":
            num1= float(input("Enter first number: "))
            num2= float(input("Enter second number: "))
            result = num1 * num2
            print("The product of the two numbers is "+ str(result))
            go_back()
        elif user_input.lower() == "divide":
            num1= float(input("Enter first number: "))
            num2= float(input("Enter second number: "))
            result = num1/num2
            print("The division of the two numbers is "+ str(result))
            go_back()
        else:
            print "Invalid Input", "\n", "Please select a valid option"
            calc()

    print('Thanks for using this calculator!')


calc()
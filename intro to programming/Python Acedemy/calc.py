# This function is the main function of the calculator program. 
#Must retype to call function and work. 
def calculator():
    print("Welcome to the Calculator")
    print("Choose the operation you would like to perform: Addition, Subtraction, Multiplication, Division, or Exponent")
    #This is the function that will be performed
    choice = input("Which function did you choose?")
    num1 = float(input("What is your 1st number?: "))
    num2 = float(input("What is your 2nd number?: "))

    def add(num1, num2):
        return num1+  num2
    def subtract(num1, num2):
        return num1 - num2
    def multiplication(num1, num2):
        return num1*num2
    def division(num1, num2):
        return num1/num2
    def exponent(num1, num2):
        return num1**num2
    
    if choice == "Addition":
        result = add(num1, num2)
        print(f"The result of your addition is {result}")
    elif choice == "Subtraction":
        result = subtract(num1, num2)
        print(f"The result of your subtraction is {result}")
    elif choice == "Multiplication":
        result = multiplication(num1, num2)
        print(f"The result of your multiplication is {result}")
    elif choice == "Division":
        result = division(num1, num2)
        print(f"The result of your division is {result}")
    elif choice == "Exponent":
        result = exponent(num1, num2)
        print(f"The result of your exponent is {result}")
    else:
        print("Invalid input")
calculator()


continued = input("would you wish to continue: Yes or No? ")
print(continued)
if continued == "Yes":
    calculator()
if continued == "No":
    print("Have a good day.")













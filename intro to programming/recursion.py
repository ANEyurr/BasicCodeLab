def my_recursion():
    choice = input("would you like to play a game, y or n: ")
    choice.lower()
    if(choice == "y"):
        my_recursion()
    elif(choice == "n"):
        print("Have a lovely day.")
    else:
        print("No idea what you said, please use 'y' or 'n' only.")
        my_recursion()
my_recursion()

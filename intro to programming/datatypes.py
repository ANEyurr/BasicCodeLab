# "#" Coments the code- se that humans r3ead it, programs ignore it. ignores it
# Uses comments to communicate what your code does
# strings - strings are words/characters
first_name = "Alyssa" #strings have to be inside of "double quotes" or 'single quotes' 
# the quotes have to match, not one double and one single. 
print(first_name)
#Built in functions to strings
print(first_name.capitalize())
the_phrase = "Coding is the most awesome thing to learn ever in this universe and beyond. This statement isn't even that bold"
print(the_phrase.count("this"))
xyz = the_phrase.istitle
print(f"istitle {xyz}")
#Side Note: the assignment operator and variables. "=" is the assignment operator. It is a command tha says the variable name is equal to the value. So First_name = "Alyssa" is a command telling first_name is "Alyssa"
#int --> Integers. These are whole numbers
user_age = 16
print(user_age)
#floats --> these are numbers with decimal points.
patient_temp = 96.5
print(patient_temp)
#boolean -->true and/or flase 
x=5
y = 10
z = 10
w = 100
print(x==y)
print(y==z)
if(x == y):
    print(f"If this prints it's true. x: {x} equals {y}")
if(x == z):
    print(f"If this prints true. y: {y} equals {z}")
#additional boolean operators
# == equal to
#>=greater than or eaqual to
#<=less than or equal to 
#<less than
#>greater than
#!= not equal
print(w == y)
print(w <= y)
print(w >= y)
print(w < y)
print(w > y)
print(w != y)


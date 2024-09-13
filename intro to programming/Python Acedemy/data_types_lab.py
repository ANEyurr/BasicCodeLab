my_int = 42
my_float = 16.5
print("The value of my_int is;", my_int)
print("The value of my_float is:",  my_float)
addition = my_int + my_float
subtraction = my_int - my_float
multiplication = my_int * my_float
division = my_int / my_float
power = my_int ** my_float
modulus = my_int % my_float
floor_division = my_int // my_float
print("addition result:", addition)
print("Subtraction result:", subtraction)
print("multiplication result:", multiplication)
print("division result:", division)
print("Power result:", (power), power)
print("Subtraction result:", modulus)
print("floor division result:", (my_int//my_float), floor_division)

first_name = "Regina"
last_name = "George"
full_name = first_name + " " + last_name
print("Your new name is:", full_name)
name_length = len(full_name)
print("The lenth of your name is:", name_length, "characters")
message = " Have a lovely evening " + full_name + "!"
print(message)

wands = ["unicorn", "ash", "pheonix"]
print("Top 3 types of wands:", wands )  
wands.append("oak")
print("Top 4 types of wands:", wands)
print("The #2 type of wand is:", wands[1])
print("The #1 type of wand is:", wands[0])
print("The #4 type of wand is:", wands[3])
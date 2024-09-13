# Functions are blocks of code that do nothing until called soomewhere
#Don't repeat yourself
#With functions you would be able to write the code once then call it somewhere else

# #def is what notifies the code that a function is abt to start. 
#( Parethesis are for the parameter. The block below has none.: lets code know the block of code that follows is part of thje function. INDENT


def my_function ():
    #Anything indented is part of the function. Not indented means it is outside the function. Russian nesting dolls, each line needs indented to be a child of the code
    print("my function")
    
#in order for this code to work you must call it, you do thjat by writing the nam eof the funtion with the (). Not indented because it is not apart of the same block
my_function()



def npc_greeting():
    print("Hello traveler. Would you like to browse my wares?")

npc_greeting()



def player_response(the_response):
    print(the_response)
answer_no = "Nah, I'm good man"
answer_yes =  "Oh yes . no skibidi ohio stuff tho"
player_response(answer_no)
player_response(answer_yes) 
npc_greeting()
player_response(answer_no)

def approach_vendor():
    npc_greeting()
    player_response = input("Enter 1 for yes, 2 for no.")
    player_response = int(player_response)

    if (player_response == 1):
        print("I'd like to buy a Skibidi Toilet.")
    elif (player_response == 2):
        print("Player vanishes like Ninja the Fortnite player streaming on Mixer. To never be heard of again like an off brand Sonic your mom says you have at home.")
    else:
        print("I'm sorry I don't speaka that language, do you have a Vegemite Sandwich?")
        print("Vender provide sandwich. You eat it with a man from Brussels.")
        # https://www.youtube.com/watch?v=XfR9iY5y94s

approach_vendor()
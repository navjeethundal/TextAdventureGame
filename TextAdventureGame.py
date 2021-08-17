#Author: Navjeet Hundal
#Version 1.0


#This program is a text based game that you go between rooms and doors to find a way out.
#Limitation: can only accept intergers from the user
#Features: (1) Entrance room with three differnt options
#(2) Kitchen where you can change the state of the lever
#(3) Pantry where you can change the state of the dial
#(4) Living room where you can go to to other rooms and pick up a string, view the soil
#(5) Attic where you can pick up cheese and drop the string into a hole
#(6) Bedroom where you can try to interact with a tomcat or feed a mouse


#Creating contants 
OPTION_1 = 1
OPTION_2 = 2
OPTION_3 = 3
OPTION_4 = 4


#Creating a function that tells the entrance room's description
#EntranceInfo(no parameters)
def EntranceInfo(Dial,Lever):
    print("""Room: Entrance Room
-------------------""","\n")
    print("""You're currently in the entrance hallway.There is a mysterious door infront
of you that that is sending out an unusual aura thats calling to you.To your
left is an entranceway into the pantry.To your right is an entranceway into
the kitchen.""","\n")

    print("The dial is currently set to",Dial)
    print("The lever is currently set to",Lever)
    print("Type '1' to try to open door")
    print("Type '2' to go through the left entryway")
    print("Type '3' to go through the right entryway")


#Creating a function that checks users input
#EntranceInputCheck(int)
def EntranceInputCheck(Entrance_room_option,Dial,Lever):

#Input check if user input is between 1-3 if not ask again
    if (Entrance_room_option > OPTION_3 or Entrance_room_option < OPTION_1):
        while (Entrance_room_option > OPTION_3 or Entrance_room_option < OPTION_1):
            print("\n")
            print("That option doesnt exist please choose from options 1-3")
            EntranceInfo(Dial,Lever)
            Entrance_room_option = int(input("What would you like to do?"))
    return Entrance_room_option #Return entrance_room_option to EntranceRoom


#Creating a function that makes the entrance room 
#EntranceRoom(str,str)
def EntranceRoom(Dial,Lever):
    Entrance = True
    while (Entrance == True):
        EntranceInfo(Dial,Lever)
        Entrance_room_option = int(input("What would you like to do?"))
        Entrance_room_option = EntranceInputCheck(Entrance_room_option,Dial,Lever)
        print("\n")

#If user picks option 1 but the dial and lever are not set to the right position then tell them its locked
        if (Entrance_room_option == OPTION_1 and (Dial != "red" or Lever != "back")):
            print("That door is locked, try to find a way to open it")
   
# Opening the door if player has pressed all the correct buttons and ending the game
        if (Entrance_room_option == OPTION_1 and Dial == "red" and Lever == "back"):
            print("""The door has been opened and pulled you in, as you look behind you it vanishes
into thin air""")
            Entrance = False #To break out of main loop 

# If player picked option 2 in entrance room take them to pantry       
        if (Entrance_room_option == OPTION_2):
            Dial = Pantry(Dial,Lever)

#If player picked option 3 take them to the kitchen
        if (Entrance_room_option == OPTION_3):
            Lever = Kitchen(Dial,Lever)


#Creating a function that tells the pantry's description
#PantryInfo(str)
def PantryInfo(Dial):
    print("""Room: Pantry
------------""","\n")
    print("""You're currently in the pantry, you can smell the aroma of delicious foods.
In front of you is a dial with 3 different settings: blue, red and green.
Behind you is the doorway back to the entrance room.""","\n")

# Telling players options for pantry           
    print("The dial is currently set to",Dial) # Telling which dial is active
    print("Type '1' to turn the dial to blue")
    print("Type '2' to turn the dial to red")
    print("Type '3' to turn the dial to green")
    print("Type '4' don't touch that dial! Return to entrance room")
    

#Creating a function that checks pantry input
#PantryInputCheck(int,str)
def PantryInputCheck(Pantry_option,Dial):

#Input check if user input is between 1-4 if not ask again
    if (Pantry_option < OPTION_1 or Pantry_option > OPTION_4):
        while (Pantry_option < OPTION_1 or Pantry_option > OPTION_4): # if input is not valid ask again
                print("\n")
                print("That option doesn't exist please choose from options 1-4")
                PantryInfo(Dial)
                Pantry_option = int(input("What would you like to do?"))
               
    return Pantry_option  #Return Pantry_option to Pantry
        

#Creating a function that changes the dial
#Pantry(str,str)
def Pantry(Dial,Lever):
    while True:
        PantryInfo(Dial)
        Pantry_option = int(input("What would you like to do?"))
        Pantry_option = PantryInputCheck(Pantry_option,Dial)
        print("\n")
        
    # Changing the dial to 'blue' if they picked option 1
        if (Pantry_option == OPTION_1):
            Dial = "blue"
            
    # Changing the dial to 'red' if they picked option 2
        if (Pantry_option == OPTION_2):
            Dial = "red"

    # Changing the dial to 'green' if they picked option 3
        if (Pantry_option == OPTION_3):
            Dial = "green"

    # If player choses option 4 break out of this loop and go back to entrance room
        if (Pantry_option == OPTION_4):
            print("\n")
            return Dial #Return Dial to EntranceRoom


#Creating a function that tells the kitchens description
#KitchenInfo(str)
def KitchenInfo(Lever):

# Letting the players know their current room and giving a description of the room
    print("""Room: Kitchen
-------------""","\n")
    print("""You're currently in the kitcken, you see many appliances around you.
In front of you is a lever that can be pushed into a forward position or pulled
in the backward position.Behind you is the doorway back to the entrance room.""","\n")

# Telling players the options for the kitchen            
    print("The lever is currently set to",Lever) # Telling which lever is active
    print("Type '1' to pull lever to the 'back' position")
    print("Type '2' to push the lever to the 'forward' positon")
    print("Type '3' don't touch the lever and return to entrance room")


#Creating a function that checks input for the kitchen
#KitchenInputCheck(int,str)
def KitchenInputCheck(Kitchen_option,Lever):

#Input check if user input is between 1-3 if not ask again
    if (Kitchen_option < OPTION_1 or Kitchen_option > OPTION_3):
        while (Kitchen_option < OPTION_1 or Kitchen_option > OPTION_3): # If input is not valid ask again
            print("\n")
            print("That option doesn't exist please choose from options 1-3")
            KitchenInfo(Lever)
            Kitchen_option = int(input("what would you like to do?"))
    return Kitchen_option #Return Kitchen_option to Kitchen


#Creating a function that changes the state of the lever
#Kitchen(str,str)
def Kitchen(Dial,Lever):
    while True:
        KitchenInfo(Lever)
        Kitchen_option = int(input("what would you like to do?"))
        Kitchen_option = KitchenInputCheck(Kitchen_option,Lever)
        print("\n")

    # Changing the lever to 'back' if they picked option 1
        if (Kitchen_option == OPTION_1):
            Lever = "back"
 
    # Changing the lever to 'forward' if they picked option 2
        if (Kitchen_option == OPTION_2):
            Lever = "forward"


    # Going back to main entrance if they picked option 3
        if (Kitchen_option == OPTION_3):
            print("\n")
            return Lever #Return Lever to EntranceRoom 
        

#Creating a function that tells the description of the living room
#LivingRoomInfo(str,str)
def LivingRoomInfo(String,Cheese):
    print("""Room: Living Room
-----------------""","\n")
    print("""You're currently in the living room in front of you is a pot of soil
and a dark entranceway that leads to the bedroom.Towards your right there are
stairs leading up to the attic.""","\n")

    print("The string is currently",String)
    print("The cheese is currently",Cheese)
    print("Type '1' to view the pot of soil")
    print("Type '2' to take the stairs up leading to the next floor")
    print("Type '3' to go through the dark entrance way")
    if (String == "not in your inventory"): # only show when player doesnt have string
        print("Type '4' to pick up the ball of string on the floor")


#Creating a function that checks living room input
#LivingRoomInputCheck(int,str,str,str)
def LivingRoomInputCheck(Living_room_option,String,Cheese,Mouse):

#Input check if string is not in your inventory user can only input 1-4 if not ask again
    if (String == "not in your inventory"): 
        while (Living_room_option > OPTION_4 or Living_room_option < OPTION_1):
            print("\n")
            print("That option doesnt exist please choose from options 1-4","\n")
            LivingRoomInfo(String,Cheese)
            Living_room_option = int(input("What would you like to do?"))

#Input check if string is gone or in your inventory user can only input 1-3 if not ask again                         
    if (String != "not in your inventory"):
        while (Living_room_option > OPTION_3 or Living_room_option < OPTION_1):
            print("\n")
            print("That option doesnt exist please choose from options 1-3","\n")
            LivingRoomInfo(String,Cheese)
            Living_room_option = int(input("What would you like to do?"))
           
    return Living_room_option # return user input to living room
        

#Creating a function that makes the living room
#LivingRoom(str,str,str)
def LivingRoom(String,Cheese,Mouse):
    Living_room = True
    Soil = "not fertilized"
    while (Living_room == True):
        LivingRoomInfo(String,Cheese)
        Living_room_option = int(input("What would you like to do?"))
        Living_room_option = LivingRoomInputCheck(Living_room_option,String,Cheese,Mouse)
        print("\n")

#If mouse is gone then the soil is fertilized and he goes back to the bedroom
        if (Mouse == "gone"):
            Soil = "fertilized"
            Mouse = "out"

#If user input is 1 and the soil hasnt been fertilized by the mouse then view the soil           
        if (Living_room_option == OPTION_1 and Soil != "fertilized"):
            print("The pot of soil looks dry")

#If user input is 1 and the mouse has fertilized the soil end game
        if (Living_room_option == OPTION_1 and Soil == "fertilized"):
            print("""The soil has been fertilized and creates a giant vine that takes you
into the sky!""")
            Living_room = False #Ending the game by breaking out of the loop

#If user input is 2 then go to the attic
        if (Living_room_option == OPTION_2):
            String, Cheese, Mouse = Attic(String,Cheese,Mouse)

#If user input is 3 then go into the bedroom
        if (Living_room_option == OPTION_3):
            String, Cheese, Mouse = Bedroom(String,Cheese,Mouse)

#If user input is 4 pick up the string            
        if (Living_room_option == OPTION_4):
            String = "in your inventory"


#Creating a function that tells the attic's description
#AtticInfo(str,str)
def AtticInfo(String,Cheese):
    print("""Room: Attic
-----------""","\n")
    print("""You're currently in the attic to your left there is a small hole.To your right
there is a table with so much cheese on it.Behind you is a staircase back down
to the living room""","\n")

    print("The string is currently",String)
    print("The cheese is currently",Cheese)
    print("Type '1' to go back to the living room ")
    print("Type '2' to pick up the cheese from the table")
    if (Cheese == "in your inventory"): #If cheese is in inventory then give option 3
        print("Type '3' to drop the cheese down the hole")
    if (String == "in your inventory"): #If string is in inventory then give option 4
        print("Type '4' to drop the string down the hole")


#Creating a function that checks input for the attic
#AtticInputCheck(int,str,str,str)
def AtticInputCheck(Attic_option,String,Cheese,Mouse):

#Input check if you dont have string but have cheese user can only input 1-3 if not ask again
    if (String != "in your inventory" and Cheese == "in your inventory"):
        while (Attic_option < OPTION_1 or Attic_option > OPTION_3): # If input is not valid ask again
            print("\n")
            print("That option doesn't exist please choose from options 1-3")
            AtticInfo(String,Cheese)
            Attic_option = int(input("What would you like to do?"))

#Input check if string is in your inventory and cheese is not user can only input 1-2 or 4 if not ask again           
    if (String == "in your inventory" and Cheese == "not in your inventory"):
        while ((Attic_option < OPTION_1 or Attic_option > OPTION_2) and Attic_option != OPTION_4): # If input is not valid ask again
            print("\n")
            print("That option doesn't exist please choose from options 1-2 or 4")
            AtticInfo(String,Cheese)
            Attic_option = int(input("What would you like to do?"))

#Input check if string is in your inventory and cheese is too user can only input 1-4 if not ask again           
    if (String == "in your inventory" and Cheese == "in your inventory"):
        while (Attic_option < OPTION_1 or Attic_option > OPTION_4): # If input is not valid ask again
            print("\n")
            print("That option doesn't exist please choose from options 1-4")
            AtticInfo(String,Cheese)
            Attic_option = int(input("What would you like to do?"))

#Input check if string is not in your inventory and no cheese user can only input 1-2 if not ask again            
    if (String != "in your inventory" and Cheese == "not in your inventory"):
        while (Attic_option < OPTION_1 or Attic_option > OPTION_2): # If input is not valid ask again
            print("\n")
            print("That option doesn't exist please choose from options 1-2")
            AtticInfo(String,Cheese)
            Attic_option = int(input("What would you like to do?"))
    return Attic_option # return Attic_option to living room


#Creating a function that makes the attic
#Attic(str,str,str)
def Attic(String,Cheese,Mouse):
    while True:
        AtticInfo(String,Cheese)
        Attic_option = int(input("What would you like to do?"))
        Attic_option = AtticInputCheck(Attic_option,String,Cheese,Mouse)
        print("\n")

#If user input is 1 go back to the living room
        if (Attic_option == OPTION_1):
            print("\n")
            return String, Cheese, Mouse; # using a tuple to return three values to Living Room

#If user input is 2 pick up the cheese        
        if (Attic_option == OPTION_2):
            print("You picked up the cheese")
            Cheese = "in your inventory"

#If user input is 3 try to drop cheese into the hole          
        if (Attic_option == OPTION_3):
            print("The cheese is too big")

#If user input is 4 drop the string down the hole     
        if (Attic_option == OPTION_4):
            print("You dropped the string down the hole")
            String = "gone"
            Mouse = "out"


#Creating a function that tells the bedroom description
#BedroomInfo(str,str,str)
def BedroomInfo(String,Cheese,Mouse):

#If mouse is hiding giving description of the bedroom
    if (Mouse == "hiding"):
        print("""Room: Bedroom
-------------""","\n")
        print("""You're currently in the bedroom in front of you is a small hole next to the
bed with a mouse hiding in it and a tomcat watching the hole trying to get
the mouse.Behind you is a dark entranceway back to the living room.""","\n")

#If mouse is out giving a description of the bedroom
    if (Mouse == "out"):
        print("""Room: Bedroom
-------------""","\n")
        print("""You're currently in the bedroom in front of you is a small hole next to the bed
and next to it is a mouse wondering in the room.Behind you is a dark entranceway
back to the living room.""","\n")

#If mouse is gone giving a desscription of the bedroom
    if (Mouse == "gone"):
        print("""Room: Bedroom
-------------""","\n")
        print("""You're currently in the bedroom in front of you is a small hole next to the bed.
It seems like the mouse has wondered off somewhere.Behind you is a dark
entranceway back to the living room.""","\n")

    print("The string is currently",String)
    print("The cheese is currently",Cheese)
    print("The mouse is currently",Mouse)
    print("Type '1' to go back to the living room ")
    if (String == "in your inventory"): #If string is in your inventory give option 2
        print("Type '2' to use the string to play with the cat")
    if (Cheese == "in your inventory") and (Mouse == "out"): #If cheese in your inventory and mouse out give option 3
        print("Type '3' to feed the mouse the cheese")


#Creating a function that checks the bedroom input
#BedroomInputCheck(int,str,str,str)
def BedroomInputCheck(Bedroom_option,String,Cheese,Mouse):

#Input check if string is not in your inventory user can only input 1 if not then ask again
    if (String == "not in your inventory" and Cheese == "in your inventory") or (String == "not in your inventory" and Cheese == "not in your inventory"):
        while (Bedroom_option < OPTION_1 or Bedroom_option > OPTION_1): # If input is not valid ask again
            print("\n")
            print("That option doesn't exist please choose from options 1-1")
            BedroomInfo(String,Cheese,Mouse)
            Bedroom_option = int(input("What would you like to do?"))

#Input check if string is gone and cheese is not in your inventory user can only input 1 if not ask again
    if (String == "gone" and Cheese == "not in your inventory"):
        while (Bedroom_option < OPTION_1 or Bedroom_option > OPTION_1): # If input is not valid ask again
            print("\n")
            print("That option doesn't exist please choose from options 1-1")
            BedroomInfo(String,Cheese,Mouse)
            Bedroom_option = int(input("What would you like to do?"))

#Input check if string is in your inventory user can only input 1-2 if not then ask again           
    if (String == "in your inventory" and Cheese == "in your inventory") or (String == "in your inventory" and Cheese == "not in your inventory"):
        while (Bedroom_option < OPTION_1 or Bedroom_option > OPTION_2): # If input is not valid ask again
            print("\n")
            print("That option doesn't exist please choose from options 1-2")
            BedroomInfo(String,Cheese,Mouse)
            Bedroom_option = int(input("What would you like to do?"))

#Input check if string is gone and cheese in inventory user can only input 1 or 3 if not then ask again
    if (String == "gone" and Cheese == "in your inventory" and Mouse == "out"):
        while (Bedroom_option < OPTION_1 or Bedroom_option >= OPTION_2 and Bedroom_option != OPTION_3):
            print("\n")
            print("That option doesn't exist please choose from options 1 or 3")
            BedroomInfo(String,Cheese,Mouse)
            Bedroom_option = int(input("What would you like to do?"))
    return Bedroom_option #Return user input to Bedroom         


#Creating a function that makes the bedroom
#Bedroom(str,str,str)
def Bedroom(String,Cheese,Mouse):
     while True:
        BedroomInfo(String,Cheese,Mouse)
        Bedroom_option = int(input("What would you like to do?"))
        Bedroom_option = BedroomInputCheck(Bedroom_option,String,Cheese,Mouse)
        print("\n")

#If user input is 1 go back to living room               
        if (Bedroom_option == OPTION_1):
            print("\n")
            return String, Cheese , Mouse; # using a tuple to return two values

#If user input is 2 try to distract the cat        
        if (Bedroom_option == OPTION_2):
            print("The cat looks at you briefly then goes back to watching the hole")

#If user input is 3 feed the mouse           
        if (Bedroom_option == OPTION_3):
            print("You fed the cheese to the mouse and he wondered off somewhere")
            Mouse = "gone"
            Cheese = "not in your inventory"
        

#Creating the start function
#start(no parameter)
def start():
    Dial = "nothing"
    Lever = "nothing"
    String = "not in your inventory"
    Cheese = "not in your inventory"
    Mouse = "hiding"
    print("The door that brought you to this house has disappeared, find another way out!")
    EntranceRoom(Dial,Lever)
    LivingRoom(String,Cheese,Mouse)

#calling the start function
start()

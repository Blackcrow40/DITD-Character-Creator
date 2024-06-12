import random

class_list = ["Warrior", "Scout", "Mage", "Priest" ]
size_list = ["Small", "Medium",  "Large"]

def main():

    player_class = random.choice(class_list)
    player_size = random.choice(size_list)
    roll_1d6 = random.randint(1, 6)

#! MAINS STATS
    Strength = roll_1d6
    Nimbleness = roll_1d6
    Durability = roll_1d6
    Comprehension = roll_1d6
    Grace = roll_1d6
    
    pass 
#! Player Size Adjustments 
    if player_size == "Small":
        Durability -= 1
        Nimbleness += 1

    elif player_size == "Large":
        Durability += 1
        Nimbleness -= 1


    pass
#! Player Class Adjustments 

            #? WARRIOR 
    if player_class == "Warrior":
        Strength += roll_1d6
        health = roll_1d6 + int(6) + Durability
        stamina = int(4) 
        starting_equipment =  "5 gold Pieces, A club, A dagger, 20 feet of rope and a suit of Light Armour"
        
            #? SCOUT
    elif player_class == "Scout":
        Nimbleness += roll_1d6
        health = int(6) + Durability
        stamina = int(4) 
        starting_equipment = "5 gold Pieces, A club, Two daggers, and 20 feet of rope"
        
            #? MAGE
    elif player_class == "Mage":
        Comprehension += roll_1d6
        health = int(4) + Durability
        stamina = int(6) 
        starting_equipment = "5 gold Pieces, A club, A dagger, A Spellcasting Focus and 20 feet of rope"
      
            #? PRIEST
    elif player_class == "Priest":
        Grace += roll_1d6
        health = int(6) + Durability
        stamina = int(5) 
        starting_equipment = "5 gold Pieces, A club, A dagger, A symbol of your faith and 20 feet of rope"
        
        pass
    
    

    print()
    print("- - - -")
    print("You are a", player_size, player_class)
    print("You have", health, "Health and", stamina, "Stamina!")
    print("- - - -")
    print("You Have", starting_equipment)
    print("- - - -")
    print()
    print("       ---STATS---")
    print()
    print("Your Strength is", Strength)
    print("- - - -")
    print("Your Nimbleness is", Nimbleness)
    print("- - - -")
    print("Your Durability is", Durability)
    print("- - - -")
    print("Your Comprehension is", Comprehension)
    print("- - - -")
    print("Your Grace is", Grace)
    print("- - - -")
    

if __name__ == '__main__':
    main()
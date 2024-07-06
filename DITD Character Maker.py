import random

class_list = ["Warrior", "Scout", "Mage", "Priest" ]
size_list = ["Small", "Medium",  "Large"]

#! Warrior Specials
warrior_specials = [
    
     'POWER STRIKE: When using this ability, you immediately make a weapon attack. You gain +2 on a attack roll for every one Stamina expend',
                    
     'BLOW BACK: After dealing damage with a weapon attack, you can push the target 5 feet back .This special may be used in conjunction with other attack specials as a part of the same attack. Costs 1 Stamina', 
    
     "SPINNING ATTACK: When using this ability, you immediately make a melee weapon attack. It deals the weapon's damage to all adjacent creatures. This special may be used in conjunction with Power Strike. Costs 3 Stamina.",
    
     'CHARGE: Warrior must move at least 10 feet in a straight line, and then make a melee attack. The attack does an extra 1d6 damage. This special may be used in conjunction with other attack specials Costs 1 stamina.',

     'HOLD FIRM: For the next round, you add +5 to your defense stat. Costs 1 stamina.',

     'POWER LEAP: You jump 20 feet forward. Costs 1 Stamina',

     'KNOCK DOWN: When using this ability, you immediately make a Demolish check with a +10 bonus break something. Costs 2 stamina',

     'RALLY: Up to two creatures (aside from you) that can hear you within gain +3 to their next attack, or skill check made within 1 minute. Costs 1 stamina.',     
                    ]

#! Scout Specials
scout_specials = [
    
     "STUNNING STRIKE: Used when attacking with a close melee weapon. If the target takes damage they cannot attack, or move on their next turn. Costs 3 Stamina",
    
     "POISON STRIKE: 4 Used when attacking with a close melee weapon. The attack does an extra 1d6 poison damage, and the target is poisoned for three rounds. Costs 2 Stamina",

     "TRACK: When using this ability, you immediately make an awareness check with a +5 bonus to find hidden creatures. Costs 2 Stamina",

     "POWER LEAP: You jump 20 feet forward. Costs 1 Stamina",

     "BLINSENSES: Activating this ability enhances your senses for 1 minute Allows you to know the locations of creatures within ten feet  of you, even if you cannot see them. It must be possible to smell, hear, or feel the effect of the creature.For instance, an invisible ghost making no sound would remain unseen. This negates the attack penalty on melee weapons while blinded. Costs 2 stamina. ",

     "MUFFLED STEPS: For 5 minutes you make no sound while walking, and any Sneak Checks are based at a +5. Costs 2 Stamina",
     
     "SPEED BURST: Your speed increases by 10 feet per round for 1 minutes",
     
     "LOCKMASTER: You take a +10 to lockpicking for 1 minute. Costs 2 stamina",
                        ]
    
#! Priest Specials
priest_specials = [
    
     "SIMPLE BLESSING- Touch Range. The targeted creature gains +2 to their next weapon attack, or skill check.", 
     
     "SIMPLE WARD- Touch Range:  The targeted creature gains +2 to their defensive score until your next turn. ",
     
     "SIMPLE SMITE -  Close melee. 1d6+1 luminous damage. This attack does +3 to undead. ",

     "HEAL - Touch range: 1d6 healing. Costs 1 stamina",
     
     "FLAME:  25 foot range 2d6 Flame damage. Costs 1 stamina",

     "SPEED BLESSING: 10 foot range Increases one creature's speed by 10 feet per round for 10 rounds. Costs 1 stamina",

     "STANDARD BLESSING: The targeted creature gains +4 to their next weapon attack, or skill check. Costs 1 stamina.",

     "REPEL THE DEAD: 10 foot range onto an undead creature. 1d6 special damage contest by the target's Grace. The undead creature must use their movement to move away from the caster of the spell on their next turn. Costs 1 stamina ",
        
     "SMITE: Melee - 3d6 Luminous damage. Costs 2 stamina ",

     "AIR BUBBLE: 20 foot range - One creature gains a +20 to breath hold checks for 5 minutes. Costs 3 stamina",
     
     "BLESSING OF THE OX: 10 foot range - One creature within range has their carrying capacity double for one hour. Costs 3 stamina",

     "LEAF STORM: 30 foot range - 3d6 Cutting damage to all creatures within 15 feet. Costs 3 stamina. ",
     
     "RESURRECTION: Touch range - A creature who has been dead less than 1 minute is brought back to life at 5 HP. Costs 15 stamina",
                    ]  
    
#! Mage Specials
mage_specials = [
    
     "LIGHT SPARK: 5 foot range - 1d6 Electric Damage. Simple Spell",
     
     "LIGHT EMBER: : 5 foot range - 1d6 Flame Damage. Simple Spell",
     
     "FROZEN TOUCH: Close Melee - 1d6+2 Ice Damage. Simple Spell (Alternatives: Dark/Ember/Shock damage for Shadow/Flame/Electric Damage)",
      
     "CREATE TRINKET: You make a small object appear in your hands such as a mirror, a file, or a food utensil. It cannot deal any damage. It disappears if you let go of it. Simple Spell",
     
     "SIMPLE WARD: 30 foot range - Adds 3 to the target defense for 1 round. Simple Spell",

     "MINOR LIGHTNING BOLT: 30 foot range - 3d6 Lightning damage to 2 creature within 30 feet. Costs 1 stamina",
     
     "ICICLE BLAST: 20 foot range - 4d6 Ice damage to 1 creature . Costs 1 Stamina",

     "MINOR SUMMONS - 10 foot range - Creates a creature with 1 in every stat. It cannot speak, but obeys your commands to the best of its ability. It has a speed of 25 It disappears after 1 hour, or if reduced to 0 hp. Costs 2 stamina",

     "ARCANE FLETCHER: You produce in your hand 1d6 arrows that disappear after 1 minute. Close inspection reveals them to be conjured. Costs 3 stamina",
     
     "FIREBLAST: 30 foot range- 3d6 Flame damage to all creatures within 15 feet. Costs 3 stamina",
     
     "WINDBLAST: 30 foot range- 2d6 Cutting damage to all creatures within 10 feet. If damage is dealt, they are knocked to the ground. Costs 3 stamina",
     
     "ICEBLAST:30 foot range- 2d6 Ice damage to all creatures within 15 feet.  If damage is dealt the target’s speed is reduced by 10 feet for 2 rounds. Costs 3 stamina",
     
     "DUSTBLAST: 20 foot range  2d6 smashing damage to all creatures within 10 feat. If damage is dealt, they are blinded for 1 round Costs 3 stamina.",

     "FIND WEAKNESS: 30 foot range - Gives you +3 to attack rolls against creatures, and +4 to demolish checks to structures. The weakness can be communicated to your allies to give them the bonus, but this will likely tip off the target. Costs 3 stamina",

     "LESSER FIRE SHIELD: Self Range, grants you a +5 to protection against fire. Costs 3 stamina.",

     "LIGHTNING BOLT: 45 foot range -6d6 Lightning damage to 3 creatures within 45 feet. Costs 5 stamina.",
     
     "FIRE SERPENT: 45 foot rage  -6d6 Fire damage to 3 creature within 45 feet. Costs 5 stamina.",

     "LESSER RAISE UNDEAD: 10 foot range. You imbue some of your energy into a corpse, or a set of bones puppet it to your will. It has the stats of a Zombie or Skeleton (see stablocks below). It is under your command, but dies after 1 hour. It can perform menial tasks like carrying items. A creature who has been animated in this fashion cannot be so animated again for another 24 hours. 10 stamina",

     "SUMMON LESSER ELEMENTAL: 10 foot range - you conjure a lesser elemental (see stablocks below) at a spot within ten feet of you which you can see. The elemental is under your command, and dies upon reaching 0 hp. 10 stamina",

     "MAJOR LIGHTNING BOLT. 60 foot range - 9d6 Lightning damage within 60 feet. Costs 12 stamina.",
    
    
                ]

def select_skills(skills, min_selected_skills, max_selected_skills):
    num_selected_skills = random.randint(min_selected_skills, max_selected_skills)
    return random.sample(skills, num_selected_skills)

def distribute_points(num_points, selected_skills, max_points_per_skill):
    
    points = {skill: 0 for skill in selected_skills}

    while num_points > 0:
        
        skill = random.choice(selected_skills)
        
        
        if points[skill] < max_points_per_skill:
            points[skill] += 1
            num_points -= 1

    return points




def main():

    player_class = random.choice(class_list)
    player_size = random.choice(size_list)
    
    #?Warrior Specials
    random_warrior_special_1 = random.choice(warrior_specials)
    random_warrior_special_2 = random.choice(warrior_specials)
    
    #?Scout Specials
    random_scout_special_1 = random.choice(scout_specials)
    random_scout_special_2 = random.choice(scout_specials)
    
    #?Priest Specials 
    random_priest_special_1 = random.choice(priest_specials)
    random_priest_special_2 = random.choice(priest_specials)
    
    #? Mage Specials
    random_mage_special_1 = random.choice(mage_specials)
    random_mage_special_2 = random.choice(mage_specials)
    
    
    #! Dice Roller 
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
    #! QUESTIONS 
    print('')
    print("- - - - - - - - - - - ")
    print('')
    special_question = input ("Would you like to have your specials randomly chosen? (Y / N)   ")
    print('')
    print("- - - - - - - - - - - ")
    print('')
    skill_question = input ("Would you like to have your skills randomly chosen? (Y / N)   ")
    print('')
    print("- - - - - - - - - - - ")
    print('')
    
    #! MAIN PRINT
    print('')
    print("- - - -")
    print("You are a", player_size, player_class)
    print("You have", health, "Health and", stamina, "Stamina!")
    print("- - - -")
    print("You Have", starting_equipment)
    print("- - - -")
    print('')
    print("       ---STATS---")
    print('')
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
    
#! Special Abilities
    
    if special_question == "y":
        #? WARRIOR
         if player_class == "Warrior":
             print('')
             print("      ----SPECIAL ABILITIES----")
             print('')
             print(random_warrior_special_1)
             print("                - - - - -")
             print(random_warrior_special_2)
             print('') 
                              
        #? SCOUT
         elif player_class == "Scout":
             print('')
             print("      ----SPECIAL ABILITIES----")
             print('')
             print(random_scout_special_1)
             print("                - - - - -")
             print(random_scout_special_2)
             print('')
             
        #? MAGE
         elif player_class == "Mage":
             print('')
             print("      ----SPECIAL ABILITIES----")
             print('')
             print(random_mage_special_1)
             print("                - - - - -")
             print(random_mage_special_2)
             print('')
        
         #? PRIEST
         elif player_class == "Priest":
             print('')
             print("      ----SPECIAL ABILITIES----")
             print('')
             print(random_priest_special_1)
             print("                - - - - -")
             print(random_priest_special_2)
             print('')
            
    elif special_question == "n":
        print('')
        print("- - - - - - ")
        print("")
        print("No Specials Chosen")
        print('')
        

#! Player Skills 
    if skill_question == "y":
        
        num_points = 6
        all_skills = ("Melee: For every five training points, you get a +1 to your defensive score while holding a melee weapon.          ",
                      
        "Close Melee: For every 5 training points, if you deal deal damage with a close melee weapon, they target takes an extra 2 damage.          ",
        
        "Range: For every 5 training points, you can add +5 to a weapon’s range. ", 
        
        "Battle Magic: For every 5 training points, you can learn one extra spell. ", 
        
        "Architecture: Based on Comprehension. ", 
        
        "Awareness: Based on Comprehension. ", 
        
        "Breath Hold: Based on Durability. ", 
        
        "Demolish: Based on Strength. ",
        
        "First Aid: Based on Grace. ", 
        
        "Influence: Based on Grace.  ",
        
        "Lockpicking: Based on Nimbleness. ",
        
        "Magic: Based on Comprehension. ",
        
        "Nature: Based on Comprehension. ",
        
        "Sneak: Based on Nimbleness. ",
        
        "Spirituality: Based on Grace. ",
        
        "Trapmaking: Based on Comprehension. "
        )
        
        min_selected_skills = 1
        max_selected_skills = 6
        max_points_per_skill = 3

        selected_skills = select_skills(all_skills, min_selected_skills, max_selected_skills)
        points_distribution = distribute_points(num_points, selected_skills, max_points_per_skill)

        print("      ----SKILLS----")
        print(" ")
        for skill in selected_skills:
            print(skill)
        print(" ")    
        print("\nPoints Distribution:")
        print(" ")
        for skill, points in points_distribution.items():
            if points > 0:
                print(f"{skill}: {points}")
        print("")
        print("------------")
        print("")        

        
        
            
            
            
    elif skill_question == "n":
        print('')
        print("- - - - - - ")
        print("")
        print("No Skills Chosen")
        print("")
        
       
    print("")
    
if __name__ == '__main__':
    main()

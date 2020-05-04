import os
import random
if __name__ == '__main__':
    loop = (1)
        # clear the screen by printing lines        
    def notes():
        done = False
        while not done:
            print_options(notesoptions)
            choice = input("Select your option: ")
            if choice in notesoptions:
                if choice == "a":
                    eyeball()
                elif choice == "b":
                    pencil()
                elif choice == "c":
                    done = True
            else:
                print("Hey that wasn't a, b, or c, what are you doing? ")
        wait_for_input()

    def pencil():
        with open('Journal.txt',"a")as journal:
            lead = input("Enter text: ")
            journal.write("\n" + lead)

    def eyeball():
        if os.path.exists('Journal.txt'):
            with open('Journal.txt', "r")as journal:
                content = journal.readlines()
                for line in content:
                    print(line, end='')
                print()            
        
    def rustsword():
        if rustsword == False:
            attack == (attack + 0)
            durability == (durability + 0)
        elif rustsword == True:
            attack == (attack + 2)
            durability == (durability + 15)
          
            if health == (health - 1):
                durability == (durability - 1)
                
            if durability == (0):
                print("rustsword broke.")
                rustsword == False
                
    def woodshield():
        if woodshield == False:
            attack == (attack + 0)
            durability1 == (durability1 + 0)
        elif rustsword == True:
            attack == (armor + 2)
            durability1 == (durability1 + 15)
          
            if armor == (armor - 1):
                durability1 == (durability1 - 1)
                
            if durability1 == (0):
                print("woodshield broke")
                woodshield == False
                
    def antswarm():
        print("A large swarm of ants aproaches.")
        if random.randomint(1,4) == 1:
            print("You escape the area!")
            loop + 2
            if loop >= 7:
                loop = 7
        if random.randomint(1,4) == 2:
            print("You escape the area!")
            loop + 1
            if loop >= 7:
                loop = 7
        if random.randomint(1,4) == 3:
            print("You escape the area!")
            loop + -1
            if loop >= 7:
                loop = 7
        if random.randomint(1,4) == 4:
            print("You escape the area!")
            loop + -2
            if loop >= 7:
                loop = 7
          
    def snakepit():
        print("You stand in a snakepit.")
        print("May god have mercy on you.")
        print("You can go to 3 blocks, labeled 1-4.")
        where = input("What do you do? ")
        if where.lower() == ("1"):
            print("_________________________________________________________________________________")
            print("You stand in a slytherin shopping site. ")
            print("Snakes dot the area. ")
            print("Would you like to buy anything? ")
            second = input("8 for bugs, 9 for, well, smaller snakes.")
            if second.lower() == ("8"):
                if gold >= 3:
                    bugs + (3)
                    gold - (3)
                    print("You buy some bugs. ")
                    wait_for_input()
                    clear_screen()
                else:
                    print("You don't buy some bugs. ")
                    wait_for_input()
                    clear_screen()
            if second.lower() == ("9"):
                if gold >= 4:
                    snakes + (1)
                    gold - (4)
                    print("You buy a snake. ")
                    wait_for_input()
                    clear_screen()
                else:
                    print("You dont buy a snake. ")
                    wait_for_input()
                    clear_screen()
        if where.lower() == ("2"):
            print("_________________________________________________________________________________")
            print("You stand at the town hall. ")
            if quest <= (1):
                print("You dont have any quests yet.")
                wait_for_input()
                clear_screen()
            if quest == (2):
                print("Figure out this quest later.")
                wait_for_input()
                clear_screen()
        if where.lower() == ("3"):
            print("_________________________________________________________________________________")
            print("You stand at the town smithy. ")
            wait_for_input()
            clear_screen()
        if where.lower() == ("4"):
            if quest == (quest >= 1):
                print("_________________________________________________________________________________")
                print("You leave... ")
                wait_for_input()
                clear_screen()
                loop = (13)
        else:
            print("_________________________________________________________________________________")
            print("Stap it. ")
            wait_for_input()
            clear_screen()      
          
          
    def town():
        print("You stand in the town hall.")
        print("You can go to 3 blocks, labeled 1-4.")
        print("Somehow, the entrance is 4.")
        print("Press 5 to talk to an npc.")
        where = input("What do you do? ")
        if where.lower() == ("1"):
            print("_________________________________________________________________________________")
            print("You stand in a food court. ")
            print("Its mostly coral and small fish. ")
            print("While you aren't intrested, someone else may be. ")
            print("Would you like to buy anything? ")
            second = input("8 for fish, 9 for coral.")
            if second.lower() == ("8"):
                if gold >= 3:
                    fish + (1)
                    gold - (3)
                    print("You buy a fish. ")
                    wait_for_input()
                    clear_screen()
                else:
                    print("You don't buy a fish. ")
                    wait_for_input()
                    clear_screen()
            if second.lower() == ("9"):
                if gold >= 2:
                    coral + (1)
                    gold - (2)
                    print("You buy a piece o' coral. ")
                    wait_for_input()
                    clear_screen()
                else:
                    print("You don't buy a piece o' coral. ")
                    wait_for_input()
                    clear_screen()
        if where.lower() == ("2"):
            print("_________________________________________________________________________________")
            print("You stand at the town hall. ")
            if quest == (0):
                print("You dont have any quests yet.")
                wait_for_input()
                clear_screen()
            if quest == (1):
                print("Go attack the warlord in his dungeon. It is strait north after you leave town, in a large hole.")
                wait_for_input()
                
        if where.lower() == ("3"):
            print("_________________________________________________________________________________")
            print("You stand at the town smithy. ")
            wait_for_input()
            clear_screen()
        if where.lower() == ("4"):
            if quest == (quest >= 1):
                print("_________________________________________________________________________________")
                print("You leave... ")
                wait_for_input()
                clear_screen()
                loop = (13)
            if quest == (0):
                print("_________________________________________________________________________________")
                print("As you  leave, a large force comes to attack the base. You are suddenly cornered by the warlord!")
                wait_for_input()
                evolvingthreat1()
                quest + 1
                print("A new quest is available!")
                wait_for_input()
                clear_screen()
        if where.lower() == ("5"):
            if random.randomint(1,5) == 1:
                print("_________________________________________________________________________________")
                print("Stop following your dreams, or they will file a restraining order. ")
                wait_for_input()
                clear_screen()
            if random.randomint(1,5) == 2:
                print("_________________________________________________________________________________")
                print("Doing a job RIGHT the first time gets the job done. Doing the job WRONG fourteen times gives you job security. ")
                wait_for_input()
                clear_screen()
            if random.randomint(1,5) == 3:
                print("_________________________________________________________________________________")
                print("INDECISION is the key to FLEXIBILITY. ")
                wait_for_input()
                clear_screen()
            if random.randomint(1,5) == 4:
                print("_________________________________________________________________________________")
                print("A person who smiles in the face of adversity…probably has a scapegoat. ")
                wait_for_input()
                clear_screen()
            if random.randomint(1,5) == 5:
                print("_________________________________________________________________________________")
                print("Never underestimate the power of very stupid people in large groups. ")
                wait_for_input()
                clear_screen()
        else:
            print("_________________________________________________________________________________")
            print("Stap it. ")
            wait_for_input()
            clear_screen()
        
          
    #EVOLVING THREAT___      
    #EVOLVING THREAT______    
    #EVOLVING THREAT_________
    def evolvingthreastencounter():
        if random.randomint(0,100) <= 1:
            evolvingthreat()      
          
    def evolvingthreat1():
        donehh = False
        if evolvingthreatform == (1):
            if evolvingthreathealth > 0:
                print("A strange and monsterous creature stands before you.")
                print("It seems to be constantly rearanging it's own body parts, and is rapidly growing.")
                second = input("What happens next happens")
                wait_for_input()
                clear_screen()
                #w
                if random.randomint(1,5) <= 2:
                    print("It is readying to pound the ground.")
                    if second.lower() == ("w"):
                        slam = True
                        print("You dodge.")
                        wait_for_input()
                        clear_screen()
                    else:
                        print("You get slamed.")
                        health - 3
                        armor - 2
                        wait_for_input()
                        clear_screen()
                #a
                if random.randomint(1,5) == 3:
                    print("It is readying to punch with the armored arm on YOUR Right, not it's.")
                    if second.lower() == ("a"):
                        print("You dodge.")
                        wait_for_input()
                        clear_screen()
                    else:
                        print("You get hit.")
                        health - 2
                        armor - 1
                        wait_for_input()
                        clear_screen()   
                #s
                if random.randomint(1,5) == 4:
                    print("It is readying to slash with the clawed arm on It's Right, not yours.")
                    if second.lower() == ("d"):
                        print("You dodge.")
                        wait_for_input()
                        clear_screen()
                    else:
                        print("You get hit.")
                        health - 3
                        wait_for_input()
                        clear_screen()    
                #d
                if random.randomint(1,5) == 5:
                    print("It is readying to stab with it's tail.")
                    if second.lower() == ("s"):
                        print("You dodge.")
                        wait_for_input()
                        clear_screen()
                    else:
                        print("You get hit.")
                        health - 2
                        armor - 2
                        wait_for_input()
                        clear_screen()    
                    #downtimeafterw(slam)
                    if slam == True:
                        print("You are now behind it. Attack at will.")
                        if second.lower() == ("1"):
                            print("You hit a weak spot!")
                            evolvingthreathealth - 10
                            wait_for_input()
                            clear_screen()
                            slam = False
                        else:
                            print("It recovers before you do anything.")
                            wait_for_input()
                            clear_screen()
                            slam = False
                            
                    if evolvingthreathealth == 0:
                        print("You defeated the creature!")
                        wait_for_input()
                        clear_screen()
                        donehh = True
                        evolvingthreathealth + (50)
                    
                
    #EVOLVING THREAT_________ 
    #EVOLVING THREAT______ 
    #EVOLVING THREAT___
                
                
                
    def stats():
        print ("health: ", health)
        print ("armor: ", armor)
        print ("attack: ", attack)
        print ("speed: ", speed)
        print ("stealth: ", stealth)
        print ("size: ", size)
        print ("perception: ", perception)
        
    def clear_screen():
        for number in range(24):
            print()

    def bag():
        print(gold)
        notes()
           # wait for user input (any input)
    def wait_for_input():
        input("press any key and enter (or just enter) when ready to return to the menu ")
            
    def print_options(options):
        # print the choices available
        for choice in options:
            print(choice, options[choice])
        
    #keys  
    key1 = False
    
    #trading items
    fish = (0)
    coral = (0)
    snakes = (0)
    bugs = (0)
    
    #evolvthreat
    evolvingthreathealth = (50)
    evolvingthreatform = (1)
    
    #didyoudodung1
    dung1comp = False
    
    #makingsurethingswork
    did = (False)
    did1 = (False)
    
    #town
    whichroomareyouin = (0)
    whichnpcisit = (0)
    townhall = (0)
    quest = (0)
    smithy = (0)
   
   #materials
    gold = (0)
    durability = (0)
    durability1 = (1)
    rustswordexist = True
    woodshieldexist = True
    
    #dontworryaboutit
    slam = False
    
    #shrimp1
    shealth = (3)
    sarmor = (1)
    sattack = (2)
    sspeed = (4)
    sstealth = (3)
    ssize = (2)
    sperception = (3)    
  
    #shrimp2
    s1health = (3)
    s1armor = (1)
    s1attack = (2)
    s1speed = (4)
    s1stealth = (3)
    s1size = (2)
    s1perception = (3)  
    
    #clam
    chealth = (1)
    carmor = (7)
    cattack = (0)
    cspeed = (0)
    cstealth = (1)
    csize = (2)
    cperception = (0)
    
    #you
    health = (10)
    armor = (5)
    attack = (4)
    speed = (3)
    stealth = (3)
    size = (3)
    perception = (5)
    
    #lobster
    lhealth = (5)
    larmor = (5)
    lattack = (4)
    lspeed = (2)
    lstealth = (2)
    lsize = (4)
    lperception = (3)
    
    #items
    shell1 = (1)
    bottle1 = (2)
    shrimp1 = (1)
    clam1 = (1)
    
    #thingsexisting
    lobster1exist = (True)
    health1exist = (True)
    soulobarny = (False)
    
    options = { 
        "1": 'Attack. ',
        "w": "Move up",
        "s": 'Move down',
        "a": "Move left",
        "d": 'Move right',
        "2": 'Observe the land',
        "3": 'Look at your surroundings',
        "4": 'Look in your bag',
        "5": 'Print your input keys',
        "6": 'Show stats',
        "7": 'Exit program'
    }
    
    notesoptions = {
        "a": 'View me. ',
        "b": 'Write. ',
        "c": 'Close me. '
    }
    
    
    
    print_options(options)
    print("_________________________________________________________________________________")
    print('Hello brave crab!')
    print('This is my python world for my freshman project.')
    print('Explore it well! Above are all the keys you will need to press on your adventure.')
    print('Note that your stats are hidden unless called upon. Certain items will boost them.')
    print('You may have to press a key multible times to interact with it correctly.')
    wait_for_input()
    clear_screen()
    
    print("_________________________________________________________________________________")
    print("Before we start, I need to make a text file displaying all the items you have.")
    print("After you pick up an item, you will be prompted to log it into Journal.txt.")
    print("Please advise.")
    notes()
    clear_screen()
    
    while True:
        while loop == (1):
            if loop == (1):
                print("_________________________________________________________________________________")
                print("You are standing in a small tide pool.")
                print("There are many alike it, but this one is yours.")
                print("You can see some glittering glass sticking out of something. How ironic.")
                print("You have heard there is a forest sanctuarry south-east of here.")
                second = input("What do you do? ")
            
                if second.lower() == ("2"):
                    print("_________________________________________________________________________________")
                    print("There is a sandy beach to your right, more tide pools to your left, a forest behind you, and ocean in front of you")
                    wait_for_input()
                    clear_screen()
                elif second.lower() == ("3"):
                    print("_________________________________________________________________________________")
                    print("It is a bottle. Attacking it will free a note. There is a strange energy surrounding the bottle.")
                    wait_for_input()
                    clear_screen()
                elif second.lower() == ("1"):
                    if bottle1 == (2):
                        print("_________________________________________________________________________________")
                        print("The bottle breaks, revealing the note.")
                        print("It reads 'Welcome, crab, to my world. I am exited to tell you'.")
                        print("'that I hope you fail horribly in an attempt to catch me. -Mystery'")
                        print("As you read it, the ink drips off. Is that a suction mark?")
                        bottle1 = (1)
                        wait_for_input()
                        clear_screen()
                    elif bottle1 == (1):
                        print("_________________________________________________________________________________")
                        print("The bottle is broken and the note is unreadable now that the ink is ruined.")
                        print("On the bright side the glass would make great cutting tools. You apply it to your claws and shell.")
                        armor = (armor + 1)
                        attack = (attack + 1)
                        notes()
                        wait_for_input()
                        clear_screen()
                    elif bottle1 == (0):
                        print("_________________________________________________________________________________")
                        print("There is nothing left of the bottle.")
                        wait_for_input()
                        clear_screen()
                elif second.lower() == ("4"):
                    print("_________________________________________________________________________________")
                    bag()
                    wait_for_input()
                    clear_screen()
                elif second.lower() == ("5"):
                    print("_________________________________________________________________________________")
                    print_options(options)
                    wait_for_input()
                    clear_screen()
                elif second.lower() == ("w"):
                    print("_________________________________________________________________________________")
                    print("As you walk to the water, soft memories of the bottle make you smile.")
                    print("You will always remember the hard jagged touch of its shiny... uhh... you know what?")
                    print("I thought this would be funny. It wasn't. Just leave.")
                    loop = (2)
                    wait_for_input()
                    clear_screen()
                elif second.lower() == ("s"):
                    print("_________________________________________________________________________________")
                    print("_________________________________________________________________________________")
                    print("As you walk to the water, soft memories of the bottle make you smile.")
                    print("You will always remember the hard jagged touch of its shiny... uhh... you know what?")
                    print("I thought this would be funny. It wasn't. Just leave.")
                    loop = (9)
                    wait_for_input()
                    clear_screen()
                elif second.lower() == ("a"):
                    print("_________________________________________________________________________________")
                    print("As you walk to the water, soft memories of the bottle make you smile.")
                    print("You will always remember the hard jagged touch of its shiny... uhh... you know what?")
                    print("I thought this would be funny. It wasn't. Just leave.")
                    loop = (4)
                    wait_for_input()
                    clear_screen()
                elif second.lower() == ("d"):
                    print("_________________________________________________________________________________")
                    print("As you walk to the water, soft memories of the bottle make you smile.")
                    print("You will always remember the hard jagged touch of its shiny... uhh... you know what?")
                    print("I thought this would be funny. It wasn't. Just leave.")
                    loop = (5)
                    wait_for_input()
                    clear_screen()
                elif second.lower() == ("7"):
                    exit(0)
                elif second.lower() == ("6"):
                    print("_________________________________________________________________________________")
                    stats()
                    wait_for_input()
                    clear_screen()
                else:
                    wait_for_input()
                    clear_screen()
            
        while loop == (2):
            if loop == (2):
                print("_________________________________________________________________________________")
                print("You are standing in the shallow end of the ocean.")
                print("The briny depths remind you of home.")
                print("There is a shell close by.")
                second = input("What do you do? ")
            
                if second.lower() == ("3"):
                    print("_________________________________________________________________________________")
                    print("There is a large hole to your right, the original tide pool behind you, ")
                    print("and deeper ocean in front of you. To your left, just a rocky area.")
                    wait_for_input()
                    clear_screen()
                    
                elif second.lower() == ("4"):
                    if shell1 == (1):
                        print("_________________________________________________________________________________")
                        print("There is a shell. It can be fitted to part of your armor.")
                        armor = (armor + 2)
                        shell1 = (0)
                        wait_for_input()
                        clear_screen()
                    elif shell1 == (0):
                        print("_________________________________________________________________________________")
                        print("You already messed with the shell.")
                        wait_for_input()
                        clear_screen()
                elif second.lower() == ("1"):
                    if shell1 == (1):
                        print("_________________________________________________________________________________")
                        print("The shell breaks.")
                        shell1 = (0)
                        wait_for_input()
                        clear_screen()
                    elif shell1 == (0):
                        print("_________________________________________________________________________________")
                        print("You already messed with the shell.")
                        wait_for_input()
                        clear_screen()
                        
                elif second.lower() == ("5"):
                    print("_________________________________________________________________________________")
                    print_options(options)
                    wait_for_input()
                    clear_screen()
                elif second.lower() == ("7"):
                    exit(0)
                elif second.lower() == ("6"):
                    print("_________________________________________________________________________________")
                    stats()
                    wait_for_input()
                    clear_screen()
                elif second.lower() == ("s"):
                    print("_________________________________________________________________________________")
                    print("You remember the bottle.")
                    print("You remember the dev's, well, quotes.")
                    print("Lets get this over with.")
                    loop = (1)
                    wait_for_input()
                    clear_screen()
                elif second.lower() == ("4"):
                    print("_________________________________________________________________________________")
                    bag()
                    wait_for_input()
                    clear_screen()
                elif second.lower() == ("a"):  
                    loop = (6)
                    print("_________________________________________________________________________________")
                    print("You head to the rocky shallows.")
                    wait_for_input()
                    clear_screen()
                else:
                    wait_for_input()
                    clear_screen()
                    
        while loop == (4):
            if loop == (4):
                print("_________________________________________________________________________________")
                print("You stand at the center of several new tide pools.")
                print("The rocky cracks could be hiding who knows what.")
                print("There are several forms of life nearby.")
                second = input("What do you do? ")
                
                if second.lower() == ("2"):
                    print("_________________________________________________________________________________")
                    print("There is a rocky beach to your right, forest behind you, ")
                    print("and your old tide pool, and,  B O T T L E  , to your left. Just rocky shallows in front of you.")
                    wait_for_input()
                    clear_screen()
                elif second.lower() == ("7"):
                    exit(0)
                elif second.lower() == ("6"):
                    print("_________________________________________________________________________________")
                    stats()
                    wait_for_input()
                    clear_screen()
                elif second.lower() == ("5"):
                    print("_________________________________________________________________________________")
                    print_options(options)
                    wait_for_input()
                elif second.lower() == ("4"):
                    if bag == (0):
                        print("_________________________________________________________________________________")
                        bag()
                        wait_for_input()
                        clear_screen()
                elif second.lower() == ("3"):
                    print("_________________________________________________________________________________")
                    print("Do you look at the right or left side of the pools?.")
                    second = input("8 for right, 9 for left.")
                    if second.lower() == ("8"):
                            if shrimp1 == (1):
                                if perception >= sstealth:
                                    if sperception < stealth:
                                        print("_________________________________________________________________________________")
                                        print("A shrimp that doesn't notice you sits pretty.")
                                        print("It bears a black stripe.")
                                        print("Of ink.")
                                        wait_for_input()
                                        clear_screen()
                                    elif sperception >= stealth:
                                        print("_________________________________________________________________________________")
                                        print("You see a shrimp. It sees you.")
                                        print("It bears a black stripe.")
                                        print("Of ink.")
                                        if sspeed >= speed:
                                            health = (health - 1)
                                            armor = (armor - 1)
                                            print("_________________________________________________________________________________")
                                            print("You get hit.")
                                            wait_for_input()
                                            gold = (gold + 3)
                                            print("_________________________________________________________________________________")
                                            print("You hit back harder. You defeat it and take it's gold.")
                                            wait_for_input()
                                            clear_screen()
                                        elif speed < sspeed:
                                            gold = (gold + 3)
                                            print("_________________________________________________________________________________")
                                            print("You swiftly defeat it and take it's gold, before it can even hit you. impressive.")
                                            wait_for_input()
                                            clear_screen()
                                if perception < sstealth:
                                    if sperception < stealth:
                                         print("_________________________________________________________________________________")
                                         print("You don't notice anything.")
                                         wait_for_input()
                                         clear_screen()
                                    elif sperception >= stealth:
                                         print("_________________________________________________________________________________")
                                         print("You don't notice anything.")
                                         wait_for_input()
                                         clear_screen()
                                         print("Suddenly, You are blind-sided by a shrimp. It gets a free hit in.")
                                         health = (health - 1)
                                         armor = (armor - 1)
                                         wait_for_input()
                                         print("In your rage, you grab it before it escapes. You defeat it and take it's gold.")
                                         gold = (gold + 3)
                                         wait_for_input()
                                         clear_screen()
                    elif second.lower() == ("9"):
                        if clam1 == (1):
                            print("_________________________________________________________________________________")
                            print("You see some clams. Opening is attempted")
                            if attack * 2 >= chealth + carmor:
                                print("You pry it open and eat it.")
                                health = (health + 2)
                                clam1 = (clam1 - 1)
                                wait_for_input()
                                clear_screen()
                            elif attack * 2 < chealth + carmor:
                                print("_________________________________________________________________________________")
                                print("You failed. Try again later.")
                                wait_for_input()
                                clear_screen()
                        if clam1 == (0):
                            print("_________________________________________________________________________________")
                            print("The clam had been pried.")
                            wait_for_input()
                            clear_screen()
                            
                elif second.lower() == ("w"):
                    loop = (6)
                    print("_________________________________________________________________________________")
                    print("You head to the rocky shallows.")
                    wait_for_input()
                    clear_screen()
                elif second.lower() == ("d"):
                    print("_________________________________________________________________________________")
                    print("You head to   B O T T L E.")
                    loop = (1)
                    wait_for_input()
                    clear_screen()
                elif second.lower() == ("s"):
                    print("_________________________________________________________________________________")
                    print("You head to the forest.")
                    loop = (8)
                    wait_for_input()
                    clear_screen()
                else:
                    wait_for_input()
                    clear_screen()
                                                    
                                        
        while loop == (6):
            if loop == (6):
                print("_________________________________________________________________________________")
                print("You stand in some rocky shallows.")
                print("The rocks appear to be covering some holes.")
                print("There are many life-forms nearby, but where? There are none in sight..")
                second = input("What do you do? ")
                
                if second.lower() == ("2"):
                    print("_________________________________________________________________________________")
                    print("There is a rocky mound to your right, tide pools behind you, ")
                    print("and shallows to your left. Just deep ocean in front of you.")
                    wait_for_input()
                    clear_screen()
                elif second.lower() == ("7"):
                    exit(0)
                elif second.lower() == ("6"):
                    print("_________________________________________________________________________________")
                    stats()
                    wait_for_input()
                    clear_screen()
                elif second.lower() == ("5"):
                    print("_________________________________________________________________________________")
                    print_options(options)
                    wait_for_input()
                elif second.lower() == ("4"):
                    print("_________________________________________________________________________________")
                    bag()   
                    wait_for_input()
                    clear_screen()
                elif second.lower() == ("3"):
                    print("_________________________________________________________________________________")
                    print("There are many rocks. You feel like opening them would be like opening a can of worms ;D.")
                    print_options(options)
                    wait_for_input()
                elif second.lower() == ("1"):
                    print("_________________________________________________________________________________")
                    print("You really did open a can of worms. you flee back to home base.")
                    loop = (1)
                    wait_for_input()
                    clear_screen()
                elif second.lower() == ("s"):
                    print("_________________________________________________________________________________")
                    print("You head to the tide pools.")
                    loop = (4)
                    wait_for_input()
                    clear_screen()
                elif second.lower() == ("d"):
                    print("_________________________________________________________________________________")
                    print("You head to the shallows.")
                    loop = (2)
                    wait_for_input()
                    clear_screen()
                
                else:
                    wait_for_input()
                    clear_screen()
            
                                        
                                        
        while loop == (5):
            if loop == (5):
                print("_________________________________________________________________________________")
                print("You stand in some sandy beach.")
                print("There is a starfish.")
                print("It is the only thing in this barren desert, exept the giant mass of water.")
                second = input("What do you do? ")
                
                if second.lower() == ("2"):
                    print("_________________________________________________________________________________")
                    print("There is more beach right, forest behind you, ")
                    print("and the origional tide pool to your left. Just a huge hole in front of you.")
                    wait_for_input()
                    clear_screen()
                elif second.lower() == ("7"):
                    exit(0)
                elif second.lower() == ("6"):
                    print("_________________________________________________________________________________")
                    stats()
                    wait_for_input()
                    clear_screen()
                elif second.lower() == ("5"):
                    print("_________________________________________________________________________________")
                    print_options(options)
                    wait_for_input()
                    clear_screen()
                elif second.lower() == ("4"):
                    print("_________________________________________________________________________________")
                    bag()
                    wait_for_input()
                    clear_screen()
                elif second.lower() == ("3"):
                    print("_________________________________________________________________________________")
                    print("There is just a starfish.")
                    wait_for_input()
                    clear_screen()
                elif second.lower() == ("1"):
                    print("_________________________________________________________________________________")
                    print("The starfish makes no reaction to your attack. Actually, you didn't do anything to it.")
                    wait_for_input()
                    clear_screen()
                elif second.lower() == ("5719448263938261092461982648615239481720495543549263936393639464936198712541056193261626874512715285612956128561265185948863622875387686591673295918275612695613693825826596196395676269385610635768253816375986396287685379217401927-9274918624-971048201740769826941"):
                    print("_________________________________________________________________________________")
                    print("The starfish dies. You beat the secret final boss. You win. Jerk.")
                    wait_for_input()
                    exit(0)
                elif second.lower() == ("w"):
                    print("_________________________________________________________________________________")
                    print("You head out.")
                    loop = (7)
                    wait_for_input()
                    clear_screen()
                elif second.lower() == ("a"):
                    print("_________________________________________________________________________________")
                    print("You head to   B O T T L E.")
                    loop = (1)
                    wait_for_input()
                    clear_screen()
                elif second.lower() == ("s"):
                    print("_________________________________________________________________________________")
                    print("You head out.")
                    loop = (10)
                    wait_for_input()
                    clear_screen()
                elif second.lower() == ("d"):
                    print("_________________________________________________________________________________")
                    print("You head to   B O T T L E.")
                    loop = (5)
                    wait_for_input()
                    clear_screen()
                    
        while loop == (7):
            if loop == (7):
                print("_________________________________________________________________________________")
                print("You stand next to a giant hole.")
                print("Do I have to say it?.")
                wait_for_input()
                print("H O L E   I S   L O V E ,   H O L E   I S   L I F E .")
                second = input("What do you do this time? ")


# NEEEEEEEEEEEEEDSSSSSSSSSSSSSSSSIINNNNNNNPPPUUUUUUTTTTTTSSSSSSSSSSSS           AAAAAAAAAHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH
                if second.lower() == ("2"):
                    print("_________________________________________________________________________________")
                    print("There is reef right, reef forward, ")
                    print("shallows left, and beach behind you.")
                    print("There is a large hole in front of you.")
                    wait_for_input()
                    clear_screen()
                elif second.lower() == ("7"):
                    exit(0)
                elif second.lower() == ("6"):
                    print("_________________________________________________________________________________")
                    stats()
                    wait_for_input()
                    clear_screen()
                elif second.lower() == ("3"):
                    print("_________________________________________________________________________________")
                    print("There is a hole. It appears to be the entrance to an underground tunnel.")
                    print("Do you want to go in?. '8' if yes, and '9' if no.")
                    if second.lower() == ("8"):
                        if dung1comp == False:
                            print("_________________________________________________________________________________")
                            print("You enter the hole.")
                            loop == (-16)
                            wait_for_input()
                            clear_screen()
                        if dung1comp == True:
                            print("_________________________________________________________________________________")
                            print("You already completed the dungeon.")
                            wait_for_input()
                            clear_screen()
                    elif second.lower() == ("9"):
                        print("_________________________________________________________________________________")
                        print("You sit there looking down the hole like a scared chihuahua. Whatever that is.")
                        wait_for_input()
                        clear_screen()
                elif second.lower() == ("5"):
                    print("_________________________________________________________________________________")
                    print_options(options)
                    wait_for_input()
                    clear_screen()
                elif second.lower() == ("4"):
                    print("_________________________________________________________________________________")
                    bag()
                    wait_for_input()
                    clear_screen()
                elif second.lower() == ("w"):
                    print("_________________________________________________________________________________")
                    print("You pack up and head out.")
                    loop = (7)
                    wait_for_input()
                    clear_screen()
                elif second.lower() == ("a"):
                    print("_________________________________________________________________________________")
                    print("You pack up and head out.")
                    loop = (2)
                    wait_for_input()
                    clear_screen()
                elif second.lower() == ("s"):
                    print("_________________________________________________________________________________")
                    print("You pack up and head out.")
                    loop = (5)
                    wait_for_input()
                    clear_screen()
                elif second.lower() == ("d"):
                    print("_________________________________________________________________________________")
                    print("You pack up and head out.")
                    loop = (7)
                    wait_for_input()
                    clear_screen()
                    
        while loop == (8):
            if loop == (8):
                print("_________________________________________________________________________________")
                print("You stand in some weeds.")
                print("The might of the forest stands before you.")
                print("Proceed with caution.")
                second = input("What do you do? ")
                if second.lower() == ("2"):
                    print("_________________________________________________________________________________")
                    print("There is tide pool in front of you, and forest elsewhere. ")
                    wait_for_input()
                    clear_screen()
                elif second.lower() == ("7"):
                    exit(0)
                elif second.lower() == ("6"):
                    print("_________________________________________________________________________________")
                    stats()
                    wait_for_input()
                    clear_screen()
                elif second.lower() == ("5"):
                    print("_________________________________________________________________________________")
                    print_options(options)
                    wait_for_input()
                    clear_screen()
                elif second.lower() == ("4"):
                    print("_________________________________________________________________________________")
                    bag()
                    wait_for_input()
                    clear_screen()
                elif second.lower() == ("3"):
                    print("_________________________________________________________________________________")
                    print("There is just trees and grass.")
                    wait_for_input()
                    clear_screen()
                elif second.lower() == ("1"):
                    print("_________________________________________________________________________________")
                    print("A tree gets cut up a little..")
                    wait_for_input()
                    clear_screen()
                elif second.lower() == ("w"):
                    print("_________________________________________________________________________________")
                    print("You head to the tide pools.")
                    loop = (4)
                    wait_for_input()
                    clear_screen()
                elif second.lower() == ("a"):
                    print("_________________________________________________________________________________")
                    print("You stay along the treeline.")
                    loop = (8)
                    wait_for_input()
                    clear_screen()
                elif second.lower() == ("s"):
                    print("_________________________________________________________________________________")
                    print("You head deeper into the forest.")
                    loop = (11)
                    wait_for_input()
                    clear_screen()
                elif second.lower() == ("d"):
                    print("_________________________________________________________________________________")
                    print("You stay along the treeling.")
                    loop = (9)
                    wait_for_input()
                    clear_screen()
        while loop == (9):
            if loop == (9):
                print("_________________________________________________________________________________")
                print("You stand in some weeds.")
                print("The might of the forest stands before you.")
                print("Proceed with caution.")
                second = input("What do you do? ")
                if second.lower() == ("2"):
                    print("_________________________________________________________________________________")
                    print("There is just the home tide pool in front of you, and forest elsewhere. ")
                    wait_for_input()
                    clear_screen()
                elif second.lower() == ("7"):
                    exit(0)
                elif second.lower() == ("6"):
                    print("_________________________________________________________________________________")
                    stats()
                    wait_for_input()
                    clear_screen()
                elif second.lower() == ("5"):
                    print("_________________________________________________________________________________")
                    print_options(options)
                    wait_for_input()
                    clear_screen()
                elif second.lower() == ("4"):
                    print("_________________________________________________________________________________")
                    bag()
                    wait_for_input()
                    clear_screen()
                elif second.lower() == ("3"):
                    print("_________________________________________________________________________________")
                    print("There is just trees and grass. Ooo and a mushroom. Its, uhh, neon green and purple?")
                    wait_for_input()
                    clear_screen()
                elif second.lower() == ("1"):
                    print("_________________________________________________________________________________")
                    print("You eat the mushroom. The soul of barny fills your heart. You will use this talent when needed most.")
                    soulobarny = True
                    wait_for_input()
                    clear_screen()
                elif second.lower() == ("w"):
                    print("_________________________________________________________________________________")
                    print("You head to the BOTTLE.")
                    loop = (1)
                    wait_for_input()
                    clear_screen()
                elif second.lower() == ("a"):
                    print("_________________________________________________________________________________")
                    print("You stay along the treeling.")
                    loop = (8)
                    wait_for_input()
                    clear_screen()
                elif second.lower() == ("s"):
                    print("_________________________________________________________________________________")
                    print("You head deeper into the forest.")
                    loop = (12)
                    wait_for_input()
                    clear_screen()
                elif second.lower() == ("d"):
                    print("_________________________________________________________________________________")
                    print("You stay along the treeline.")
                    loop = (10)
                    wait_for_input()
                    clear_screen()
        while loop == (10):
            if loop == (10):
                print("_________________________________________________________________________________")
                print("You stand in some weeds.")
                print("Ants swarm this area.")
                print("You can only do one task before they notice you.")
                second = input("What do you do? ")
                if second.lower() == ("2"):
                    print("_________________________________________________________________________________")
                    print("There is just the beach in front of you, and forest elsewhere. ")
                    wait_for_input()
                    clear_screen()
                elif second.lower() == ("7"):
                    exit(0)
                elif second.lower() == ("6"):
                    print("_________________________________________________________________________________")
                    stats()
                    wait_for_input()
                    clear_screen()
                elif second.lower() == ("5"):
                    print("_________________________________________________________________________________")
                    print_options(options)
                    wait_for_input()
                    clear_screen()
                elif second.lower() == ("4"):
                    print("_________________________________________________________________________________")
                    bag()
                    wait_for_input()
                    clear_screen()
                elif second.lower() == ("3"):
                    print("_________________________________________________________________________________")
                    print("There are antihills dotting the area.")
                    wait_for_input()
                    clear_screen()
                elif second.lower() == ("1"):
                    print("_________________________________________________________________________________")
                    print("You KICK A GIANT ANTHILL. You fight a good fight but get chased off.")
                    health = (health - 5)
                    wait_for_input()
                    clear_screen()
                elif second.lower() == ("w"):
                    print("_________________________________________________________________________________")
                    print("You head to the beach.")
                    loop = (5)
                    wait_for_input()
                    clear_screen()
                elif second.lower() == ("a"):
                    print("_________________________________________________________________________________")
                    print("You stay along the treeling.")
                    loop = (9)
                    wait_for_input()
                    clear_screen()
                elif second.lower() == ("s"):
                    print("_________________________________________________________________________________")
                    print("You head deeper into the forest.")
                    loop = (13)
                    wait_for_input()
                    clear_screen()
                elif second.lower() == ("d"):
                    print("_________________________________________________________________________________")
                    print("You cant go there.")
                    wait_for_input()
                    clear_screen()
        while loop == (11):
            if loop == (11):
                print("_________________________________________________________________________________")
                print("You stand in some weeds.")
                print("Ants swarm this area.")
                print("You can only do one task before they notice you.")
                second = input("What do you do? ")
                if second.lower() == ("2"):
                    print("_________________________________________________________________________________")
                    print("There is just forest elsewhere. ")
                    wait_for_input()
                    clear_screen()
                elif second.lower() == ("7"):
                    exit(0)
                elif second.lower() == ("6"):
                    print("_________________________________________________________________________________")
                    stats()
                    wait_for_input()
                    clear_screen()
                elif second.lower() == ("5"):
                    print("_________________________________________________________________________________")
                    print_options(options)
                    wait_for_input()
                    clear_screen()
                elif second.lower() == ("4"):
                    print("_________________________________________________________________________________")
                    bag()
                    wait_for_input()
                    clear_screen()
                elif second.lower() == ("3"):
                    print("_________________________________________________________________________________")
                    print("There are many anthills in the area. I wouldn't kick one.")
                    wait_for_input()
                    clear_screen()
                elif second.lower() == ("1"):
                    print("_________________________________________________________________________________")
                    print("You KICK A GIANT ANTHILL. You fight a good fight but get chased off.")
                    health = (health - 5)
                    wait_for_input()
                    clear_screen()
                elif second.lower() == ("w"):
                    print("_________________________________________________________________________________")
                    print("You go deeper into the forest.")
                    loop = (8)
                    wait_for_input()
                    clear_screen()
                elif second.lower() == ("a"):
                    print("_________________________________________________________________________________")
                    print("You go deeper into the forest.")
                    loop = (11)
                    wait_for_input()
                    clear_screen()
                elif second.lower() == ("s"):
                    print("_________________________________________________________________________________")
                    print("You head deeper into the forest.")
                    loop = (11)
                    wait_for_input()
                    clear_screen()
                elif second.lower() == ("d"):
                    print("_________________________________________________________________________________")
                    print("You go deeper into the forest.")
                    loop = (12)
                    wait_for_input()
                    clear_screen()
        while loop == (12):
            if loop == (12):
                print("_________________________________________________________________________________")
                print("You stand in some weeds.")
                print("Ants swarm this area.")
                print("You can only do one task before they notice you.")
                second = input("What do you do? ")
                if second.lower() == ("2"):
                    print("_________________________________________________________________________________")
                    print("There is just forest elsewhere. ")
                    wait_for_input()
                    clear_screen()
                elif second.lower() == ("7"):
                    exit(0)
                elif second.lower() == ("6"):
                    print("_________________________________________________________________________________")
                    stats()
                    wait_for_input()
                    clear_screen()
                elif second.lower() == ("5"):
                    print("_________________________________________________________________________________")
                    print_options(options)
                    wait_for_input()
                    clear_screen()
                elif second.lower() == ("4"):
                    print("_________________________________________________________________________________")
                    bag()
                    wait_for_input()
                    clear_screen()
                elif second.lower() == ("3"):
                    print("_________________________________________________________________________________")
                    print("There is an ant carrying a small metal chunk. you try to take it, but it runs off. ")
                    antswarm()
                    wait_for_input()
                    clear_screen()
                elif second.lower() == ("1"):
                    print("_________________________________________________________________________________")
                    print("You step on an ant.")
                    antswarm()
                    wait_for_input()
                    clear_screen()
                elif second.lower() == ("w"):
                    print("_________________________________________________________________________________")
                    print("You head deeper into the forest.")
                    loop = (9)
                    wait_for_input()
                    clear_screen()
                elif second.lower() == ("a"):
                    print("_________________________________________________________________________________")
                    print("You head deeper into the forest.")
                    loop = (11)
                    wait_for_input()
                    clear_screen()
                elif second.lower() == ("s"):
                    print("_________________________________________________________________________________")
                    print("You head deeper into the forest.")
                    loop = (12)
                    wait_for_input()
                    clear_screen()
                elif second.lower() == ("d"):
                    print("_________________________________________________________________________________")
                    print("You head deeper into the forest.")
                    loop = (13)
                    wait_for_input()
                    clear_screen()
        while loop == (13):
            if loop == (13):
                print("_________________________________________________________________________________")
                print("You stand at a town entrance.")
                print("Actually, its more like a shopping mall.")
                print("Do you head in?")
                second = input("1 for yes, 2 for no.")
                if second.lower() == ("1"):
                    town()
                if second.lower() == ("2"):
                    loop = (12)
                # __                        ___     ___    __
                #|  \    |   |    /\    /  |       |      /  \     /\    /    /|
                #|   |   |   |   /  \  /   | __    |___  |    |   /  \  /      |
                #|__/    |___|  /    \/    |___|   |___   \__/   /    \/      _|_
                        
        while loop == (-16):
            if loop == (-16):  
                if second.lower() == ("1"):
                    print("_________________________________________________________________________________")
                    print("There is nothing to attack.")
                    wait_for_input()
                    clear_screen()
                if second.lower() == ("2"):
                    print("_________________________________________________________________________________")
                    print("There is a door in front of you. Just walls everywhere else, exept to your left, and steps going back up the hole. in the corner of the room.")
                    wait_for_input()
                    clear_screen()
                elif second.lower() == ("7"):
                    exit(0)
                elif second.lower() == ("6"):
                    print("_________________________________________________________________________________")
                    stats()
                    wait_for_input()
                    clear_screen()
                elif second.lower() == ("3"):
                    print("_________________________________________________________________________________")
                    print("Do you go back up the hole?")
                    print("'8' if yes, and '9' if no.")
                    if second.lower() == ("8"):
                        print("_________________________________________________________________________________")
                        print("You go back up the H O L E.")
                        loop == (5)
                        wait_for_input()
                        clear_screen()
                    elif second.lower() == ("9"):
                        print("_________________________________________________________________________________")
                        print("You don't go.")
                        wait_for_input()
                        clear_screen()
                elif second.lower() == ("5"):
                    print("_________________________________________________________________________________")
                    print_options(options)
                    wait_for_input()
                    clear_screen()
                elif second.lower() == ("4"):
                    print("_________________________________________________________________________________")
                    bag()
                    wait_for_input()
                    clear_screen()
                elif second.lower() == ("w"):
                    print("_________________________________________________________________________________")
                    print("You head into the next room.")
                    loop = (-2)
                    wait_for_input()
                    clear_screen()
                elif second.lower() == ("a"):
                    print("_________________________________________________________________________________")
                    print("You walk the next room")
                    loop = (-1)
                    wait_for_input()
                    clear_screen()
                elif second.lower() == ("s"):
                    print("_________________________________________________________________________________")
                    print("You walk into a wall, onto the cealing, and back around to the opposite door. You head to the next room.")
                    loop = (-2)
                    wait_for_input()
                    clear_screen()
                elif second.lower() == ("d"):
                    print("_________________________________________________________________________________")
                    print("You walk into a wall, onto the cealing, and back around to the opposite door. You head to the next room.")
                    loop = (-1)
                    wait_for_input()
                    clear_screen()
                    
                    
        while loop == (-1):
            if loop == (-1):
                if second.lower() == ("1"):
                    print("_________________________________________________________________________________")
                    print("There is nothing to attack.")
                    wait_for_input()
                    clear_screen()
                if second.lower() == ("2"):
                    print("_________________________________________________________________________________")
                    print("There is a door in front of you. There is also one to your right. Just walls elsewhere.")
                    wait_for_input()
                    clear_screen()
                elif second.lower() == ("7"):
                    exit(0)
                elif second.lower() == ("6"):
                    print("_________________________________________________________________________________")
                    stats()
                    wait_for_input()
                    clear_screen()
                elif second.lower() == ("3"):
                    if rustswordexist == True:
                        print("_________________________________________________________________________________")
                        print("You find a rusty (but still working) sword. It will most likely break ofter a bit. Do you take it?")
                        print("'8' if yes, and '9' if no.")
                        if second.lower() == ("8"):
                            print("_________________________________________________________________________________")
                            print("You take the sword.")
                            rustsword = True
                            rustswordexist = False
                            notes()
                            wait_for_input()
                            clear_screen()
                        elif second.lower() == ("9"):
                            print("_________________________________________________________________________________")
                            print("You don't take it.")
                            wait_for_input()
                            clear_screen()
                    elif rustswordexist == False:
                            print("_________________________________________________________________________________")
                            print("You don't find anything.")
                            wait_for_input()
                            clear_screen()
                           
                elif second.lower() == ("5"):
                    print("_________________________________________________________________________________")
                    print_options(options)
                    wait_for_input()
                    clear_screen()
                elif second.lower() == ("4"):
                    print("_________________________________________________________________________________")
                    bag()
                    wait_for_input()
                    clear_screen()
                elif second.lower() == ("w"):
                    print("_________________________________________________________________________________")
                    print("You head into the next room.")
                    loop = (-3)
                    wait_for_input()
                    clear_screen()
                elif second.lower() == ("a"):
                    print("_________________________________________________________________________________")
                    print("You walk into a wall, onto the cealing, and back around to the opposite door. You head to the next room.")
                    loop = (-16)
                    wait_for_input()
                    clear_screen()
                elif second.lower() == ("s"):
                    print("_________________________________________________________________________________")
                    print("You walk into a wall, onto the cealing, and back around to the opposite door. You head to the next room.")
                    loop = (-3)
                    wait_for_input()
                    clear_screen()
                elif second.lower() == ("d"):
                    print("_________________________________________________________________________________")
                    print("You head into the next room.")
                    loop = (-16)
                    wait_for_input()
                    clear_screen()
                
                
        while loop == (-2):
            if loop == (-2):  
                if second.lower() == ("1"):
                    print("_________________________________________________________________________________")
                    print("There is nothing to attack.")
                    wait_for_input()
                    clear_screen()
                if second.lower() == ("2"):
                    print("_________________________________________________________________________________")
                    print("There is a door to your left and behind you. Just walls elsewhere.")
                    wait_for_input()
                    clear_screen()
                elif second.lower() == ("7"):
                    exit(0)
                elif second.lower() == ("6"):
                    print("_________________________________________________________________________________")
                    stats()
                    wait_for_input()
                    clear_screen()
                elif second.lower() == ("3"):
                    if rustswordexist == True:
                        print("_________________________________________________________________________________")
                        print("You find a wooden (but still working) shield. It will most likely break ofter a bit. Do you take it?")
                        print("'8' if yes, and '9' if no.")
                        if second.lower() == ("8"):
                            print("_________________________________________________________________________________")
                            print("You take the shield.")
                            woodshield = True
                            woodshieldexist = False
                            notes()
                            wait_for_input()
                            clear_screen()
                        elif second.lower() == ("9"):
                            print("_________________________________________________________________________________")
                            print("You don't take it.")
                            wait_for_input()
                            clear_screen()
                    elif woodshieldexist == False:
                            print("_________________________________________________________________________________")
                            print("You don't find anything.")
                            wait_for_input()
                            clear_screen()
                           
                elif second.lower() == ("5"):
                    print("_________________________________________________________________________________")
                    print_options(options)
                    wait_for_input()
                    clear_screen()
                elif second.lower() == ("4"):
                    print("_________________________________________________________________________________")
                    bag()
                    wait_for_input()
                    clear_screen()
                elif second.lower() == ("w"):
                    print("_________________________________________________________________________________")
                    print("You walk into a wall, onto the cealing, and back around to the opposite door. You head to the next room.")
                    loop = (-16)
                    wait_for_input()
                    clear_screen()
                elif second.lower() == ("a"):
                    print("_________________________________________________________________________________")
                    print("You head to the next room.")
                    loop = (-3)
                    wait_for_input()
                    clear_screen()
                elif second.lower() == ("s"):
                    print("_________________________________________________________________________________")
                    print("You head to the next room.")
                    loop = (-16)
                    wait_for_input()
                    clear_screen()
                elif second.lower() == ("d"):
                    print("_________________________________________________________________________________")
                    print("You head up a wall, on the cealing, and to the opposite door. You head into the next room.")
                    loop = (-3)
                    wait_for_input()
                    clear_screen()
                                       
                
        while loop == (-3):
            if loop == (-3):  
                if second.lower() == ("1"):
                    print("_________________________________________________________________________________")
                    print("There is nothing to attack.")
                    wait_for_input()
                    clear_screen()
                if second.lower() == ("2"):
                    print("_________________________________________________________________________________")
                    print("There is a door to your left, behind, and to the right of you.")
                    wait_for_input()
                    clear_screen()
                elif second.lower() == ("7"):
                    exit(0)
                elif second.lower() == ("6"):
                    print("_________________________________________________________________________________")
                    stats()
                    wait_for_input()
                    clear_screen()
                elif second.lower() == ("3"):
                    print("_________________________________________________________________________________")
                    print("You find nothing.")
                    wait_for_input()
                    clear_screen()   
                elif second.lower() == ("5"):
                    print("_________________________________________________________________________________")
                    print_options(options)
                    wait_for_input()
                    clear_screen()
                elif second.lower() == ("4"):
                    print("_________________________________________________________________________________")
                    bag()
                    wait_for_input()
                    clear_screen()
                elif second.lower() == ("w"):
                    print("_________________________________________________________________________________")
                    print("You walk into a wall, onto the cealing, and back around to the opposite door. You head to the next room.")
                    loop = (-1)
                    wait_for_input()
                    clear_screen()
                elif second.lower() == ("a"):
                    print("_________________________________________________________________________________")
                    print("You head to the next room.")
                    loop = (-4)
                    wait_for_input()
                    clear_screen()
                elif second.lower() == ("s"):
                    print("_________________________________________________________________________________")
                    print("You head to the next room.")
                    loop = (-1)
                    wait_for_input()
                    clear_screen()
                elif second.lower() == ("d"):
                    print("_________________________________________________________________________________")
                    print("You head into the next room.")
                    loop = (-2)
                    wait_for_input()
                    clear_screen()
                
        while loop == (-3):
            if loop == (-3):  
                if second.lower() == ("1"):
                    print("_________________________________________________________________________________")
                    print("There is nothing to attack.")
                    wait_for_input()
                    clear_screen()
                if second.lower() == ("2"):
                    print("_________________________________________________________________________________")
                    print("There is a door to your left, right, and behind you, and a wall in front of you.")
                    wait_for_input()
                    clear_screen()
                elif second.lower() == ("7"):
                    exit(0)
                elif second.lower() == ("6"):
                    print("_________________________________________________________________________________")
                    stats()
                    wait_for_input()
                    clear_screen()
                elif second.lower() == ("3"):
                    print("_________________________________________________________________________________")
                    print("You find nothing.")
                    print("You feel as though you are being watched.")
                    wait_for_input()
                    clear_screen()   
                elif second.lower() == ("5"):
                    print("_________________________________________________________________________________")
                    print_options(options)
                    wait_for_input()
                    clear_screen()
                elif second.lower() == ("4"):
                    print("_________________________________________________________________________________")
                    bag()
                    wait_for_input()
                    clear_screen()
                elif second.lower() == ("w"):
                    print("_________________________________________________________________________________")
                    print("You walk into a wall, onto the cealing, and back around to the opposite door. You head to the next room.")
                    loop = (-5)
                    wait_for_input()
                    clear_screen()
                elif second.lower() == ("a"):
                    print("_________________________________________________________________________________")
                    print("You head to the next room.")
                    loop = (-7)
                    wait_for_input()
                    clear_screen()
                elif second.lower() == ("s"):
                    print("_________________________________________________________________________________")
                    print("You head to the next room.")
                    loop = (-5)
                    wait_for_input()
                    clear_screen()
                elif second.lower() == ("d"):
                    print("_________________________________________________________________________________")
                    print("You head into the next room.")
                    loop = (-3)
                    wait_for_input()
                    clear_screen()
                
        while loop == (-5):
            if loop == (-5):  
                if second.lower() == ("1"):
                    print("_________________________________________________________________________________")
                    print("I wouldn't advise that.")
                    wait_for_input()
                    clear_screen()
                if second.lower() == ("2"):
                    print("_________________________________________________________________________________")
                    print("There is a door to your left, right, and behind you, and a wall in front of you.")
                    wait_for_input()
                    clear_screen()
                elif second.lower() == ("7"):
                    exit(0)
                elif second.lower() == ("6"):
                    print("_________________________________________________________________________________")
                    stats()
                    wait_for_input()
                    clear_screen()
                elif second.lower() == ("3"):
                    print("_________________________________________________________________________________")
                    print("There is a gang of shrimp nearby, as well as a lobster.")
                    print("Do you start a fight?.")
                    print("'8' if yes, and '9' if no.")
                    if second.lower() == ("8"):
                            print("_________________________________________________________________________________")
                            print("You start a brawl, and slip past.")
                            loop = (-6)
                            wait_for_input()
                            clear_screen()
                    elif second.lower() == ("9"):
                            print("_________________________________________________________________________________")
                            print("You don't start a fight.")
                            wait_for_input()
                            clear_screen()
                    elif woodshieldexist == False:
                            print("_________________________________________________________________________________")
                            print("You don't find anything.")
                            wait_for_input()
                            clear_screen()
                elif second.lower() == ("5"):
                    print("_________________________________________________________________________________")
                    print_options(options)
                    wait_for_input()
                    clear_screen()
                elif second.lower() == ("4"):
                    print("_________________________________________________________________________________")
                    bag()
                    wait_for_input()
                    clear_screen()
                elif second.lower() == ("w"):
                    print("_________________________________________________________________________________")
                    print("You head to the next room.")
                    loop = (-4)
                    wait_for_input()
                    clear_screen()
                elif second.lower() == ("a"):
                    print("_________________________________________________________________________________")
                    print("You are attacked by the gang.")
                    print("You black out.")
                    print("You wake up outside the dungeon.")
                    loop = (7)
                    wait_for_input()
                    clear_screen()
                elif second.lower() == ("s"):
                    print("_________________________________________________________________________________")
                    print("You walk up the wall, on the cealing, and head to the next room.")
                    loop = (-4)
                    wait_for_input()
                    clear_screen()
                elif second.lower() == ("d"):
                    print("_________________________________________________________________________________")
                    print("You walk up the wall, on the cealing, and are noticed by one of the shrimp.")
                    print("You are attacked by the gang.")
                    print("You black out.")
                    print("You wake up outside the dungeon.")
                    loop = (7)
                    wait_for_input()
                    clear_screen()
        
        while loop == (-7):
            if loop == (-7):  
                if second.lower() == ("1"):
                    if shrimp1exist == (True):
                        print("_________________________________________________________________________________")
                        print("You and a shrimp get into as fight.")
                        wait_for_input()
                        print("You overpower it, and take a scratch as it tries to fight back.")
                        health = (health - 1)
                        wait_for_input()
                        print("You deal the finishing blow, and loot it.")
                        wait_for_input()
                        print("You find some gold!")
                        gold = (gold + 1)
                        shrimp1exist = (False)
                        wait_for_input()
                        clear_screen()
                    elif shrimp1exist == (False):
                        print("_________________________________________________________________________________")
                        print("You find the shrimp and his empty... wallet? But it's under wat.. nevermind.")
                        wait_for_input()
                        clear_screen()
                if second.lower() == ("2"):
                    print("_________________________________________________________________________________")
                    print("There is a door to your left, right, and infront of you, and a wall in behind you.")
                    wait_for_input()
                    clear_screen()
                elif second.lower() == ("7"):
                    exit(0)
                elif second.lower() == ("6"):
                    print("_________________________________________________________________________________")
                    stats()
                    wait_for_input()
                    clear_screen()
                elif second.lower() == ("3"):
                    print("_________________________________________________________________________________")
                    print("A shrimp stares at you angrily, but stands there out of fear. You can attack it, or pass by.")
                    wait_for_input()
                    clear_screen()
                elif second.lower() == ("5"):
                    print("_________________________________________________________________________________")
                    print_options(options)
                    wait_for_input()
                    clear_screen()
                elif second.lower() == ("4"):
                    print("_________________________________________________________________________________")
                    bag()
                    wait_for_input()
                    clear_screen()
                elif second.lower() == ("w"):
                    print("_________________________________________________________________________________")
                    print("You head to the next room.")
                    loop = (-8)
                    wait_for_input()
                    clear_screen()
                elif second.lower() == ("a"):
                    print("_________________________________________________________________________________")
                    print("You head to the next room.")
                    loop = (-11)
                    wait_for_input()
                    clear_screen()
                elif second.lower() == ("s"):
                    print("_________________________________________________________________________________")
                    print("You walk up the wall, on the cealing, and head to the next room.")
                    loop = (-8)
                    wait_for_input()
                    clear_screen()
                elif second.lower() == ("d"):
                    print("_________________________________________________________________________________")
                    print("You head into the next room.")
                    loop = (-4)
                    wait_for_input()
                    clear_screen()
                                       
        
        while loop == (-6):
            if loop == (-6):  
                if second.lower() == ("1"):
                    print("_________________________________________________________________________________")
                    print("You could attack a key that you probably need, but I wouldn't.")
                    wait_for_input()
                    clear_screen()
                if second.lower() == ("2"):
                    print("_________________________________________________________________________________")
                    print("There is a door to your right, and walls elsewhere")
                    wait_for_input()
                    clear_screen()
                elif second.lower() == ("7"):
                    exit(0)
                elif second.lower() == ("6"):
                    print("_________________________________________________________________________________")
                    stats()
                    wait_for_input()
                    clear_screen()
                elif second.lower() == ("3"):
                    print("_________________________________________________________________________________")
                    print("There is a key. Do you take it?.")
                    print("'8' if yes, and '9' if no.")
                    if second.lower() == ("8"):
                            print("_________________________________________________________________________________")
                            print("You take it.")
                            key1 = True
                            wait_for_input()
                            clear_screen()
                    elif second.lower() == ("9"):
                            print("_________________________________________________________________________________")
                            print("You don't take it.")
                            key1 = False
                            wait_for_input()
                            clear_screen()
                    elif key1 == True:
                            print("_________________________________________________________________________________")
                            print("You don't find anything.")
                            wait_for_input()
                            clear_screen()
                elif second.lower() == ("5"):
                    print("_________________________________________________________________________________")
                    print_options(options)
                    wait_for_input()
                    clear_screen()
                elif second.lower() == ("4"):
                    print("_________________________________________________________________________________")
                    bag()
                    wait_for_input()
                    clear_screen()
                elif second.lower() == ("w"):
                    print("_________________________________________________________________________________")
                    print("You walk up the wall, on the cealing, back around again.")
                    loop = (-8)
                    wait_for_input()
                    clear_screen()
                elif second.lower() == ("a"):
                    print("_________________________________________________________________________________")
                    print("You walk up the wall, on the cealing, and into the next room. The brawl has ended but they are about to wake up, do you get out of there.")
                    loop = (-4)
                    wait_for_input()
                    clear_screen()
                elif second.lower() == ("s"):
                    print("_________________________________________________________________________________")
                    print("You walk up the wall, on the cealing, back around again.")
                    loop = (-8)
                    wait_for_input()
                    clear_screen()
                elif second.lower() == ("d"):
                    print("_________________________________________________________________________________")
                    print("You head into the next room. The brawl has ended and you take off before they wake up.")
                    loop = (-4)
                    wait_for_input()
                    clear_screen()
                    
        while loop == (-8):
            if loop == (-8):  
                if second.lower() == ("1"):
                    print("_________________________________________________________________________________")
                    print("You could attack the machinery, but you don't, as someone already brke it.")
                    wait_for_input()
                    clear_screen()
                if second.lower() == ("2"):
                    print("_________________________________________________________________________________")
                    print("There is a door to your right and behind you, and walls elsewhere")
                    wait_for_input()
                    clear_screen()
                elif second.lower() == ("7"):
                    exit(0)
                elif second.lower() == ("6"):
                    print("_________________________________________________________________________________")
                    stats()
                    wait_for_input()
                    clear_screen()
                elif second.lower() == ("3"):
                    print("_________________________________________________________________________________")
                    print("There is a contraption, one tank that opens the door to the next room, and one that doesnt.")
                    print("You can tell, because someone already broke the lock. There are 2 levers.")
                    print("'8' if left, and '9' if right.")
                    if second.lower() == ("8"):
                            print("_________________________________________________________________________________")
                            print("You open the door. It was already open on account of no lock")
                            key1 = True
                            wait_for_input()
                            clear_screen()
                    elif second.lower() == ("9"):
                            print("_________________________________________________________________________________")
                            print("You don't open the door, and are left unsatisfied with your luck.")
                            key1 = False
                            wait_for_input()
                            clear_screen()
                elif second.lower() == ("5"):
                    print("_________________________________________________________________________________")
                    print_options(options)
                    wait_for_input()
                    clear_screen()
                elif second.lower() == ("4"):
                    print("_________________________________________________________________________________")
                    bag()
                    wait_for_input()
                    clear_screen()
                elif second.lower() == ("w"):
                    print("_________________________________________________________________________________")
                    print("You walk up the wall, on the cealing, and into the next room.")
                    loop = (-7)
                    wait_for_input()
                    clear_screen()
                elif second.lower() == ("a"):
                    print("_________________________________________________________________________________")
                    print("You walk up the wall, on the cealing, and into the next room.")
                    loop = (-9)
                    wait_for_input()
                    clear_screen()
                elif second.lower() == ("s"):
                    print("_________________________________________________________________________________")
                    print("You walk into the next room.")
                    loop = (-7)
                    wait_for_input()
                    clear_screen()
                elif second.lower() == ("d"):
                    print("_________________________________________________________________________________")
                    print("You head into the next room.")
                    loop = (-9)
                    wait_for_input()
                    clear_screen()
                
        while loop == (-6):
            if loop == (-6):  
                if second.lower() == ("1"):
                    print("_________________________________________________________________________________")
                    print("You could attack a key that you probably need, but I wouldn't.")
                    wait_for_input()
                    clear_screen()
                if second.lower() == ("2"):
                    print("_________________________________________________________________________________")
                    print("There is a door to your right, and walls elsewhere")
                    wait_for_input()
                    clear_screen()
                elif second.lower() == ("7"):
                    exit(0)
                elif second.lower() == ("6"):
                    print("_________________________________________________________________________________")
                    stats()
                    wait_for_input()
                    clear_screen()
                elif second.lower() == ("3"):
                    print("_________________________________________________________________________________")
                    print("There is a key. Do you take it?.")
                    print("'8' if yes, and '9' if no.")
                    if second.lower() == ("8"):
                            print("_________________________________________________________________________________")
                            print("You take it.")
                            key1 = True
                            wait_for_input()
                            clear_screen()
                    elif second.lower() == ("9"):
                            print("_________________________________________________________________________________")
                            print("You don't take it.")
                            key1 = False
                            wait_for_input()
                            clear_screen()
                    elif key1 == True:
                            print("_________________________________________________________________________________")
                            print("You don't find anything.")
                            wait_for_input()
                            clear_screen()
                elif second.lower() == ("5"):
                    print("_________________________________________________________________________________")
                    print_options(options)
                    wait_for_input()
                    clear_screen()
                elif second.lower() == ("4"):
                    print("_________________________________________________________________________________")
                    bag()
                    wait_for_input()
                    clear_screen()
                elif second.lower() == ("w"):
                    print("_________________________________________________________________________________")
                    print("You walk up the wall, on the cealing, back around again.")
                    loop = (-8)
                    wait_for_input()
                    clear_screen()
                elif second.lower() == ("a"):
                    print("_________________________________________________________________________________")
                    print("You walk up the wall, on the cealing, and into the next room. The brawl has ended but they are about to wake up, do you get out of there.")
                    loop = (-4)
                    wait_for_input()
                    clear_screen()
                elif second.lower() == ("s"):
                    print("_________________________________________________________________________________")
                    print("You walk up the wall, on the cealing, back around again.")
                    loop = (-8)
                    wait_for_input()
                    clear_screen()
                elif second.lower() == ("d"):
                    print("_________________________________________________________________________________")
                    print("You head into the next room. The brawl has ended and you take off before they wake up.")
                    loop = (-4)
                    wait_for_input()
                    clear_screen()
                    
        while loop == (-9):
            if loop == (-9):  
                if second.lower() == ("1"):
                    if lobster1exist == (True):
                        print("_________________________________________________________________________________")
                        print("You fight the lobster in the room with you.")
                        print("You both hit each-other at the same time.")
                        armor = (armor - 2)
                        health = (health - 2)
                        wait_for_input()
                        print("You are both still standing, but it is dazed, and one more hit knocks it over.")
                        print("Being a slave, it has nothing to loot. Ohh, I didn't mention it was a slave?")
                        lobster1exist = (False)
                        wait_for_input()
                        clear_screen()
                    if lobster1exist == (False):
                        print("_________________________________________________________________________________")
                        print("The leftover lobster bits sit on the ground.")
                        wait_for_input()
                        clear_screen()
                if second.lower() == ("2"):
                    print("_________________________________________________________________________________")
                    print("There is a door to your right and left, and walls elsewhere")
                    wait_for_input()
                    clear_screen()
                elif second.lower() == ("7"):
                    exit(0)
                elif second.lower() == ("6"):
                    print("_________________________________________________________________________________")
                    stats()
                    wait_for_input()
                    clear_screen()
                elif second.lower() == ("3"):
                    print("_________________________________________________________________________________")
                    print("There is a lobster in there with you.")
                    wait_for_input()
                    clear_screen()
                elif second.lower() == ("5"):
                    print("_________________________________________________________________________________")
                    print_options(options)
                    wait_for_input()
                    clear_screen()
                elif second.lower() == ("4"):
                    print("_________________________________________________________________________________")
                    bag()
                    wait_for_input()
                    clear_screen()
                elif second.lower() == ("w"):
                    print("_________________________________________________________________________________")
                    print("You walk up the wall, on the cealing, and back around.")
                    loop = (-7)
                    wait_for_input()
                    clear_screen()
                elif second.lower() == ("a"):
                    print("_________________________________________________________________________________")
                    print("You head into the next room.")
                    loop = (-8)
                    wait_for_input()
                    clear_screen()
                elif second.lower() == ("s"):
                    print("_________________________________________________________________________________")
                    print("You walk up the wall, on the cealing, and back around.")
                    loop = (-7)
                    wait_for_input()
                    clear_screen()
                elif second.lower() == ("d"):
                    print("_________________________________________________________________________________")
                    print("You head into the next room.")
                    loop = (-10)
                    wait_for_input()
                    clear_screen()
                    
        while loop == (-10):
            if loop == (-10):  
                if second.lower() == ("1"):
                    if lobster1exist == (True):
                        print("_________________________________________________________________________________")
                        print("Nothing to fight in here.")
                        wait_for_input()
                        clear_screen()
                if second.lower() == ("2"):
                    print("_________________________________________________________________________________")
                    print("There is a door to your left, and walls elsewhere")
                    wait_for_input()
                    clear_screen()
                elif second.lower() == ("7"):
                    exit(0)
                elif second.lower() == ("6"):
                    print("_________________________________________________________________________________")
                    stats()
                    wait_for_input()
                    clear_screen()
                elif second.lower() == ("3"):
                    if health1exist == (True):
                        print("_________________________________________________________________________________")
                        print("You drink the potion")
                        health = (health + 3)
                        health1exist = (False)
                        wait_for_input()
                        clear_screen()
                    if health1exist == (False):
                        print("_________________________________________________________________________________")
                        print("There is nothing else in here.")
                        wait_for_input()
                        clear_screen()
                elif second.lower() == ("5"):
                    print("_________________________________________________________________________________")
                    print_options(options)
                    wait_for_input()
                    clear_screen()
                elif second.lower() == ("4"):
                    print("_________________________________________________________________________________")
                    bag()
                    wait_for_input()
                    clear_screen()
                elif second.lower() == ("w"):
                    print("_________________________________________________________________________________")
                    print("You walk up the wall, on the cealing, and back around.")
                    loop = (-7)
                    wait_for_input()
                    clear_screen()
                elif second.lower() == ("a"):
                    print("_________________________________________________________________________________")
                    print("You head into the next room.")
                    loop = (-9)
                    wait_for_input()
                    clear_screen()
                elif second.lower() == ("s"):
                    print("_________________________________________________________________________________")
                    print("You walk up the wall, on the cealing, and back around.")
                    loop = (-7)
                    wait_for_input()
                    clear_screen()
                elif second.lower() == ("d"):
                    print("_________________________________________________________________________________")
                    print("You walk up the wall, on the cealing, and head into the next room.")
                    loop = (-9)
                    wait_for_input()
                    clear_screen()

        while loop == (-11):
            if loop == (-11):  
                if second.lower() == ("1"):
                    if lobster1exist == (True):
                        print("_________________________________________________________________________________")
                        print("Nothing to fight in here. However, you see the old husk of a dead crab.")
                        wait_for_input()
                        clear_screen()
                if second.lower() == ("2"):
                    print("_________________________________________________________________________________")
                    print("There is a door to your right, but huge doors to your left and behind you, and walls elsewhere")
                    wait_for_input()
                    clear_screen()
                elif second.lower() == ("7"):
                    exit(0)
                elif second.lower() == ("6"):
                    print("_________________________________________________________________________________")
                    stats()
                    wait_for_input()
                    clear_screen()
                elif second.lower() == ("3"):
                    print("_________________________________________________________________________________")
                    print("There is an old, dead husk of a crab.")
                    wait_for_input()
                    clear_screen()
                elif second.lower() == ("5"):
                    print("_________________________________________________________________________________")
                    print_options(options)
                    wait_for_input()
                    clear_screen()
                elif second.lower() == ("4"):
                    print("_________________________________________________________________________________")
                    bag()
                    wait_for_input()
                    clear_screen()
                elif second.lower() == ("w"):
                    print("_________________________________________________________________________________")
                    print("You walk up the wall, on the cealing, down the large door, and back around.")
                    loop = (-7)
                    wait_for_input()
                    clear_screen()
                elif second.lower() == ("a"):
                    print("_________________________________________________________________________________")
                    print("You open the large door.")
                    loop = (-14)
                    wait_for_input()
                    clear_screen()
                elif second.lower() == ("s"):
                    print("_________________________________________________________________________________")
                    print("You open the large door.")
                    loop = (-12)
                    wait_for_input()
                    clear_screen()
                elif second.lower() == ("d"):
                    print("_________________________________________________________________________________")
                    print("You head into the next room.")
                    loop = (-9)
                    wait_for_input()
                    clear_screen()
        while loop == (-12):
            if loop == (-12):  
                if second.lower() == ("1"):
                    if lobster1exist == (True):
                        print("_________________________________________________________________________________")
                        print("There is a chest that is to sturdy to destroy")
                        wait_for_input()
                        clear_screen()
                if second.lower() == ("2"):
                    print("_________________________________________________________________________________")
                    print("There is larg doors in front of and to the left of you, and walls elsewhere")
                    wait_for_input()
                    clear_screen()
                elif second.lower() == ("7"):
                    exit(0)
                elif second.lower() == ("6"):
                    print("_________________________________________________________________________________")
                    stats()
                    wait_for_input()
                    clear_screen()
                elif second.lower() == ("3"):
                    print("_________________________________________________________________________________")
                    print("There is a chest. You try to open it.")
                    if key1 == (True):
                        print("You get a small strength potion.")
                        attack = (attack + 2)
                        key1 = (False)
                        wait_for_input()
                        clear_screen()
                    if key1 == (False):
                        print("It is locked.")
                        wait_for_input()
                        clear_screen()
                elif second.lower() == ("5"):
                    print("_________________________________________________________________________________")
                    print_options(options)
                    wait_for_input()
                    clear_screen()
                elif second.lower() == ("4"):
                    print("_________________________________________________________________________________")
                    bag()
                    wait_for_input()
                    clear_screen()
                elif second.lower() == ("w"):
                    print("_________________________________________________________________________________")
                    print("You go into the next room.")
                    loop = (-11)
                    wait_for_input()
                    clear_screen()
                elif second.lower() == ("a"):
                    print("_________________________________________________________________________________")
                    print("Head into the next room.")
                    loop = (-14)
                    wait_for_input()
                    clear_screen()
                elif second.lower() == ("s"):
                    print("_________________________________________________________________________________")
                    print("You open the large door.")
                    loop = (-12)
                    wait_for_input()
                    clear_screen()
                elif second.lower() == ("d"):
                    print("_________________________________________________________________________________")
                    print("You slip on the wall.")
                    loop = (-9)
                    wait_for_input()
                    clear_screen()
                    
        while loop == (-14):
            if loop == (-14):  
                if second.lower() == ("1"):
                    if lobster1exist == (True):
                        print("_________________________________________________________________________________")
                        print("There is a HUGE DOOR that is too hard to destroy.")
                        wait_for_input()
                        clear_screen()
                if second.lower() == ("2"):
                    print("_________________________________________________________________________________")
                    print("You could turn back, but you won't")
                    wait_for_input()
                    clear_screen()
                elif second.lower() == ("7"):
                    exit(0)
                elif second.lower() == ("6"):
                    print("_________________________________________________________________________________")
                    stats()
                    wait_for_input()
                    clear_screen()
                elif second.lower() == ("3"):
                    print("_________________________________________________________________________________")
                    print("There are giant doors")
                    wait_for_input()
                    clear_screen()
                elif second.lower() == ("5"):
                    print("_________________________________________________________________________________")
                    print_options(options)
                    wait_for_input()
                    clear_screen()
                elif second.lower() == ("4"):
                    print("_________________________________________________________________________________")
                    bag()
                    wait_for_input()
                    clear_screen()
                elif second.lower() == ("w"):
                    print("_________________________________________________________________________________")
                    print("You open the giant doors and enter.")
                    loop = (-15)
                    wait_for_input()
                    clear_screen()
                elif second.lower() == ("a"):
                    print("_________________________________________________________________________________")
                    print("You must go through the doors (w).")
                    wait_for_input()
                    clear_screen()
                elif second.lower() == ("s"):
                    print("_________________________________________________________________________________")
                    print("You must go through the doors (w).")
                    wait_for_input()
                    clear_screen()
                elif second.lower() == ("d"):
                    print("_________________________________________________________________________________")
                    print("You must go through the doors (w).")
                    wait_for_input()
                    clear_screen()
        
        while loop == (-15):
            if loop == (-15):
                evolvingthreat1()
                print("You completed the dungeon!")
                wait_for_input()
                print("Ohh, You want a reward?")
                wait_for_input()
                print("Lets see...")
                wait_for_input()
                print("uhh...")
                wait_for_input()
                print("uhh..")
                wait_for_input()
                print("Ohh!")
                wait_for_input()
                print("You get a new blueprint at the smithy! ")
                smithy = (1)
                wait_for_input()
                print("You leave!")
                wait_for_input()
                dung1comp = True
                loop = (7)
                quest = (2)
                
                
import os
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
        content = (gold + inventory)
           
           # wait for user input (any input)
    def wait_for_input():
        input("press any key and enter (or just enter) when ready to return to the menu ")
            
    def print_options(options):
        # print the choices available
        for choice in options:
            print(choice, options[choice])
        
        
    gold = (0)
    
    
    shealth = (3)
    sarmor = (1)
    sattack = (2)
    sspeed = (4)
    sstealth = (3)
    ssize = (2)
    sperception = (3)    
    
    
    chealth = (1)
    carmor = (7)
    cattack = (0)
    cspeed = (0)
    cstealth = (1)
    csize = (2)
    cperception = (0)
    

    health = (10)
    armor = (5)
    attack = (4)
    speed = (3)
    stealth = (3)
    size = (3)
    perception = (5)
    
    
    shell1 = (1)
    bottle1 = (2)
    shrimp1 = (1)
    clam1 = (1)


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
    print("Before we start, I need to make a text file sisplaying all the items you have.")
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
                        wait_for_input()
                        clear_screen()
                    elif bottle1 == (0):
                        print("_________________________________________________________________________________")
                        print("There is nothing left of the bottle.")
                        wait_for_input()
                        clear_screen()
                elif second.lower() == ("4"):
                    if bag == (0):
                        print("_________________________________________________________________________________")
                        print("Your bag is empty. No gold, nothing.")
                        wait_for_input()
                        clear_screen()
                    elif bag >= (1):
                        print("_________________________________________________________________________________")
                        print("gold: ", + gold)
                        print("items: ", + notes)
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
                    loop = (3)
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
                    if bag == (0):
                        print("_________________________________________________________________________________")
                        print("Your bag is empty. No gold, nothing.")
                        wait_for_input()
                        clear_screen()
                    elif bag >= (1):
                        print("_________________________________________________________________________________")
                        print("gold: ", + gold)
                        print("items: ", + notes)
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
                        print("Your bag is empty. No gold, nothing.")
                        wait_for_input()
                        clear_screen()
                    elif bag >= (1):
                        print("_________________________________________________________________________________")
                        print("gold: ", + gold)
                        print("items: ", + notes)
                        wait_for_input()
                        clear_screen()
                elif second.lower() == ("3"):
                    print("_________________________________________________________________________________")
                    print("Do you look at the right or left side of the pools?.")
                    second = input("1 for right, 2 for left.")
                    if second.lower() == ("1"):
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
                    elif second.lower() == ("w"):
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
                    if bag == (0):
                        print("_________________________________________________________________________________")
                        print("Your bag is empty. No gold, nothing.")
                        wait_for_input()
                        clear_screen()
                    elif bag >= (1):
                        print("_________________________________________________________________________________")
                        print("gold: ", + gold)
                        print("items: ", + notes)
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
            ()
                                        
                                        
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
                    if bag == (0):
                        print("_________________________________________________________________________________")
                        print("Your bag is empty. No gold, nothing.")
                        wait_for_input()
                        clear_screen()
                    elif bag >= (1):
                        print("_________________________________________________________________________________")
                        print("gold: ", + gold)
                        print("items: ", + notes)
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
                    print("You head to the hole.")
                    loop = (7)
                    wait_for_input()
                    clear_screen()
                elif second.lower() == ("a"):
                    print("_________________________________________________________________________________")
                    print("You head to   B O T T L E.")
                    loop = (1)
                    wait_for_input()
                    clear_screen()
                    
        while loop == (7):
            if loop == (7):
                print("_________________________________________________________________________________")
                print("You stand next to a giant hole.")
                print("Do I have to say it?.")
                wait_for_input()
                print("H O L E   I S   L O V E ,   H O L E   I S   L I F E .")
                second = input("What do you do? ")



                if second.lower() == ("2"):
                    print("_________________________________________________________________________________")
                    print("There is reef right, reef forward, ")
                    print("shallows left, and beach behind you.")
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
                    if bag == (0):
                        print("_________________________________________________________________________________")
                        print("Your bag is empty. No gold, nothing.")
                        wait_for_input()
                        clear_screen()
                    elif bag >= (1):
                        print("_________________________________________________________________________________")
                        print("gold: ", + gold)
                        print("items: ", + notes)
                        wait_for_input()
                        clear_screen()
if __name__ == '__main__':
        # clear the screen by printing lines
    def name():
        print (yourname)
        

    def wallet():
        print (gold)
        
    def inventory():
        print (items)
    
    def clear_screen():
        for number in range(24):
            print()
            
            # wait for user input (any input)
    def wait_for_input():
        input("press any key and enter (or just enter) when ready to return to the menu ")
            
    def print_options(options):
        # print the choices available
        for choice in options:
            print(choice, options[choice])
            
    gold = (0)

    items = (0)
    
    yourname = (0)

    options = {
        "1": 'Attack. ',
        "2": "Move up",
        "3": 'Move down',
        "4": "Move left",
        "5": 'Move right',
        "6": 'Look around',
        "7": 'Look at inventory',
        "8": 'Look at wallet',
        "9": 'Print your input keys'
        '10': "Exit program. "
    }
    
    while True:

        print_options(options)
        print('Hello brave adventurer man guy!')
        print('This is my python world for my freshman prodject.')
        print('Explore it well! Above are all the keys you will need to press on your adventure.')
        wait_for_input()
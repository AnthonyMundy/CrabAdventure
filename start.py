if __name__ == '__main__':
        # clear the screen by printing lines

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

    options = {
        "1": 'Attack. ',
        "2": "Move up",
        "3": 'Move down',
        "4": "Move left",
        "5": 'Move right',
        "6": 'Look around',
        "7": 'Look at inventory',
        "8": 'Look at wallet',
        "9": "Exit program. "
    }
    
    while True:

        print_options(options)

        # get the input from the user
        numchoice = input("Enter choice: ")

        # check that the option is valid (is it in the dictionary?)
        if numchoice in options:
            # find out the option used
            if numchoice == '9':
                exit(0)
            
            elif numchoice == '1':
                print ("You picked 1! ")
                wait_for_input()
            
            elif numchoice == '2':
                print ("You picked 2! ")
                wait_for_input()
            
            elif numchoice == '3':
                print ("You picked 3! ")
                wait_for_input()
            
            elif numchoice == '4':
                print ("You picked 4! ")
                wait_for_input()
            
            elif numchoice == '5':
                print ("You picked 5! ")
                wait_for_input()
            
            elif numchoice == '6':
                print ("You picked 6! ")
                wait_for_input()
            
            elif numchoice == '7':
                inventory()
                wait_for_input()
            
            elif numchoice == '8':
                wallet()
                wait_for_input()


        # the option was not in the dictionary, let the user know
        else:
            print("Hey don't do that. ")
            wait_for_input()
        clear_screen()
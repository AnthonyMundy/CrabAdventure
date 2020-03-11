import os
import pyowm
if __name__ == '__main__':

    # preform calculations
    def calc():
        print("you called calc")
        solve = None
        try:
            solve = eval(input("Enter the numbers and things, E/G: '10 + 10'. "))
        except:
            pass
        print(solve)
        wait_for_input()

    # wait for user input (any input)
    def wait_for_input():
        input("press any key and enter (or just enter) when ready to return to the menu ")

    # clear the screen by printing lines
    def clear_screen():
        for number in range(24):
            print()

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

    def print_options(options):
        # print the choices available
        for choice in options:
            print(choice, options[choice])

    def get_weather():
        owm = pyowm.OWM(API_key='1b1fe14c8404008f19f86bfbcc0050be')
        observation = owm.daily_forecast('name')
        print(observation.get_wind())


    def fib(n):
        if n <= 1:
            return n
        else:
            return (fib(n - 1) + fib(n - 2))


    options = {
        "1": 'Pick me. ',
        "2": "Calc",
        "3": 'Notes',
        "4": "Print fibonacci sequence",
        "5": "Exit program. "
    }

    notesoptions = {
        "a": 'View me. ',
        "b": 'Write. ',
        "c": 'Close me. '
    }

    while True:

        print_options(options)

        # get the input from the user
        numchoice = input("Enter choice: ")

        # check that the option is valid (is it in the dictionary?)
        if numchoice in options:
            # find out the option used
            if numchoice == '5':
                exit(0)
            elif numchoice == '1':
                print ("You picked 1! ")
                wait_for_input()

            elif numchoice == '2':
                calc()

            elif numchoice == '3':
                notes()
            elif numchoice == '4':
                try:
                    num = int(input("Enter a number to fib up to: "))
                    for i in range(num):
                        print(i + 1,fib(i))
                    wait_for_input()
                except Exception:
                    print('not a number')

        # the option was not in the dictionary, let the user know
        else:
            print("Hey don't do that. ")
            wait_for_input()
        clear_screen()
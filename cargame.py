# we are going to write a program for the engine of a car
# The program starts when you type 'help' and breaks when you type 'quit'
# If you write anything other than the recommended words the program will not run

# We will create a loop to keep the program running util the user quits
command = ""
started = False

while True:
    command = input("> ").lower()
    if command == "start":
        if started:
            print("Car already started")
        else:
            started = True
            print("Car started..Let's go!")
    elif command == "stop":
        if not started:
            print("Car  already stopped")
        else:
            started = False
            print("Car stopped")
    elif command == "help":
        print("""
    to start - start
    to stop - stop
    to quit - quit
    to get help - help
        """)
    elif command == "quit":
        break
    else:
        print("I don't understand")



























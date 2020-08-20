#Bus game
command = ""
started = False
while True:
    command = input("> ").lower()
    if command == "start":
         if started:
              print("Bus is already started!")
         else:
             started = True
             print("Bus started...")
    elif command == "stop":
          if not started:
               print("Bus is alreay started!")
          else:
               started = False
               print("Bus stopped.")
    elif command == "help":                      
        print("""
    start - to start the Bus
    stop - to stop the Bus
    quit - to quit
        """)
    elif command == "quit":
        break
    else:
        print("sorry, i don't understand that")            
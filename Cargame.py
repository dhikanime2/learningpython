print('Type "help" for how to play')
command = ""
started = False
while True:
    command = input('>').lower()
    if command == "start":
        if started:
            print('car already started!')

        else:
            started = True
            print('car started..')

    elif command == "stop":
        if not started:
            print('car already stopped')
        else:
            started = False
            print('car Stop')
    elif command == "help":
        print("""
        type start  to start
        type stop to stop
        type quit to quit
        """)
    elif command == "quit":
        print('thank you for playing! :) ')
        break
    else:
        print("hey we don't understand this!")
command = ""
started = False
while True:
    command = input("> ").lower()
    if command == "start":
        if started:
           print("car is already started")
        else :
            started = True
            print("car is started")
    elif command == "stop":
        if not started:
            print("car is already started")
        else:
            started = False
            print("car is stopped")
    elif command == "break":
          break

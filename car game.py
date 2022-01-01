


command =""
started = False

while True:
    
    command=input(">").lower()
    
    if command=="start":
        if started :
            print(f"already started")
        else:    
            started=True
            print(f"car started... Ready to go !")
        
    elif command=="stop":
        if not started:
            print(f"car is already stopped...")
        else:
            started=False
            print(f"car stopped")

    elif command=="exit":
        print(f"you quit the game")
        break
    
    elif command=="help":
        print(f"start - to start the car ")
        print(f"stop - to stop the car ")
        print(f"exit - to exit ")
    
    else:
        print("enter valid input")
        break 
    

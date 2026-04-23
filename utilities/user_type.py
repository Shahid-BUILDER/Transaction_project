def choice():
    while True:
        x={1:"go Admin control", 2:"go User",3:"Exit"}
        print("----------------------------------------------------------------------------")
        print("TRANSACTION LOGGER".center(76))
        print("----------------------------------------------------------------------------")
        print("1. Admin control")
        print("2. User")
        print("3. Exit")
        print("----------------------------------------------------------------------------")
        try:
            e = int(input("Enter your choice (1-3): "))
            if e<1 or e>3:
                print("Invalid choice, pls choice as per list.")
            else:
                if e==1:
                    return 1
                elif e==2:
                    return 2
                elif e==3:
                    return 0
        except ValueError:
            print("Invalid input. Please enter a number between 1-3.")
            continue
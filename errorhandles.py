def devfunc():
    x = input("Enter an integer for x: ")
    y = input("Enter an integer for y: ")
    try:
        x = int(x)
        y = int(y)

    except ValueError:
        print("Entered float, trying to convert...")
        x = float(x)
        y = float(y)

    try: 
        print(x / y)

    except ZeroDivisionError:
        print("y cannot be zero! Try again...")
        devfunc()

devfunc()

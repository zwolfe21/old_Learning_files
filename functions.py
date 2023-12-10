"""
Ignoring this part of the code a.t.m. 
Working on error handling and nested 
functions below...
"""
    

def even_odd():
    n = input("Type a Number: ")
    n = int(n)
    if n % 2 == 0:
        print("Your number is even")
    else:
        print("Your number is odd")

# even_odd()


"""
function one takes user input number converts to float
then divides by two and passes it to function two as a
parameter of function two. Returns error and re-input if 
value is a string and not an int or float.

Fails error test after three times of increasing the 
global variable to 3. Requests re-input from user before
then. 
"""
zed = 1


def func_one():
    global zed
    n = input("Type an Integer: ")
    if zed < 3:
        try:
            n = float(n)  # converts datatype input to float. Fails on strings
            n *= 2
            func_two(n)
        except ValueError:
            print("Input is a string!, try again")
            print("")
            zed += 1
            func_one()
    elif zed == 3:
        print("Too many attempts, Closing")
        exit()


"""
Input from integer is moved to function two which divides 
four by the user input. m carries the data type from 
function one.
"""


def func_two(m):
    try:
        result = 4 / m
        print(result)
    except ZeroDivisionError:
        print("Input cannot equal zero, try againi \n") # Forgot about the new line character... don't need print("")
        #print("")
        func_one()

func_one()

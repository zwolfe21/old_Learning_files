x = 1
y = 2
z = x + y

if y % 2 == 0:
    if (x + y) % 2 != 0:
        print("y is even, x +y is odd")

#Another way to write the above nested if statement.

if y % 2 == 0 and (x + y) % 2 !=0:
    print("y is even, x + y is odd")

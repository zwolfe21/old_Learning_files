from math import remainder

x = 10
y = 7

print("")
print("x & y =", x, y)

'''
for i in range(10):
    x += 1
    y -= 1
    print(x, y)
'''

print("Divisor", x / y)
print("Floored Dev.", x // y)
print("Modulo", x % y)
print(" ")
print("Interestingly, the modulo / the denominator, y in this case,")
print("results in the remainder from the float point divisor operator")
print("modulo results / y:", (x % y) / y)
print(" ")
print("Thus, floored quotients + the previous operation results in")
print("the same results as simply dividing out x and y")
print(x // y + (x % y) / y)
print("Using the math.remainder function:", remainder(x,y)) # Creates a float equv. modulo?
    # See https://stackoverflow.com/questions/5584586/find-the-division-remainder-of-a-number for this
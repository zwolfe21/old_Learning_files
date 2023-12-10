def f():
    x = 1
    return x

try:
    print("|", x) # This is VS Code's issue. Calling a local scope variable from global.

except NameError:
    print("Variable X is defined within a function.")
    print("It will not print without calling the function")
    print("The result of function is", f())

print("Calling without except", f())

"""Python and VS Code will throw a problem with trying to
call a variable outside the local scope. Even though this
code will print the assignment to variable x after a 
try/except, it doesn't like the code as written. Bad
practice. It was intentional to use a try/except. Try
fails and defaults to the except on the NameError."""
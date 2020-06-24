# If you can remember how to use help(), you hold the key to understanding most other function.
help(round)
help(abs)
help(round(-2.01))

# Defining functions 
def least_difference (a,b,c):
    diff1=abs(a-b)
    diff2=abs(b-c)
    diff3=abs(a-c)
    return min(diff1, diff2, diff3)
# when python encounters a return statement, it exits the function immediately
print (
    least_difference(1,10,100),
    least_difference(1,10,10),
    least_difference(5,6,7),
)
help(least_difference) # output: least_difference(a, b, c)

# Docstring = a triple-quoted string which goes immediately after the header of the function
# Doctoring should describe what a function does, not how it works.
def least_difference(a, b, c):
    """Return the smallest difference between any two numbers
    among a, b and c.
    
    >>> least_difference(1, 5, -5)
    4
    """
    diff1 = abs(a - b)
    diff2 = abs(b - c)
    diff3 = abs(a - c)
    return min(diff1, diff2, diff3)

# When we call help() on a function, it shows the docstring 

# What if we didn't include the return keyword? > None

print (1,2,3, sep=' < ')
# 1 < 2 < 3

def greet(who="Collin"):
    print ("hello, ", who)

    greet()
    greet(who="Kaggle")
# (In this case, we don't need to specify the name of the argument, because it's unambiguous.)
    greet("world")

def mult_by_five(x):
    return 5*x
def call(fn,arg):
    """Call fn on arg"""
    return fn(arg)
def squared_call(fn,arg):
    """Call on the result of calling fn on arg"""
print(
    call(mult_by_five,1),
    squared_call(mult_by_five,1),
    sep='\n'
)
# > 5 25

def mod_5(x):
""" Return the remainder of x after dividing by 5"""
return x%5
print(
    'Which number is biggest?',
    max(100,51,14),
    'Which number is the biggest modulo 5?',
    max(100,51,14,key=mod_5),
    sep='\n'
)
# Which number is biggest?
# 100
# Which number is the biggest modulo 5?
# 14
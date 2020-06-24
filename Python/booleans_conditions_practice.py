# Booleans
def can_run_for_president(age):
    """Can someone of the given age run for president in the US?"""
    # The US Constitution says you must be at least 35 years old
    return age >=35
print ("Can a 19-year-old run for president?",can_run_for_president(19))  
print ("Can a 45-year-old run for president?",can_run_for_president(45)) 

3.0 == 3
#true

'3' == 3
#false

#checking whether a number is odd or not
def is_odd(n):
    return (n%2) == 1
print ("Is 100 odd?", is_odd(100))
print ("Is -1 is odd?", is_odd(-1))
# Is 100 odd? False
# Is -1 odd? True

#combining Boolean values 
def can_run_for_president(age, is_natural_born_citizen):
    """Can someone of the given age and citizenship status run for president in the US?"""
    # The US Constitution says you must be a natural born citizen *and* at least 35 years old
    return is_natural_born_citizen and (age>=35)

print(can_run_for_president(19, True))
print(can_run_for_president(55, False))
print(can_run_for_president(55, True))

#False
#False
#True

# The order of operations 
# and is evaluated before or 

True or True and False
#True 
#True or True is True
#True and False is False 
#True or False is True

prepared_for_weather = (
    have_umbrella
    or ((rain_level < 5 and have_hood)
    or not (rain_level > 0 and is_workday))
)

#Conditional statements 
# if, elif, else

def inspect(x):
    if x == 0:
        print (x,"is zero")
    elif x>0:
        print (x, "is positive")
    elif x<0:
        print (x, "is negative")
    else:
        print (x, "is unlike anything I've ever seen...")
inspect (0)
inspect (-15)

# 0 is zero
# -15 is negative 

def f(x):
    if x>0:
        print ("Only printed when x is positive; x=",x)
        print ("Also onle printed when x is positive; x=",x)
    print ("Always printed, regardless of x's value; x=",x)
f(1)
f(0)

# Only printed when x is positive; x = 1
# Also only printed when x is positive; x = 1
# Always printed, regardless of x's value; x = 1
# Always printed, regardless of x's value; x = 0

# Boolean conversion 
print(bool(1)) # all numbers are treated as true, except 0
print(bool(0))
print(bool("asf"))  # all strings are treated as true, except the empty string ""
print(bool(""))

#True
#False
#True
#False 

if 0:
    print(0)
elif "spam":
    print("spam")
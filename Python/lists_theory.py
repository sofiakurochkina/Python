# List examples
primes = [2,3,5,7]
planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
hands = [
    ['J', 'Q', 'K'],
    ['2', '2', '2'],
    ['6', 'A', 'K'], # (Comma after the last element is optional)
]
my_favourite_things = [32, 'raindrops on roses', help]

# Indexing 
planets[0]
#Elements at the end of the list can be accessed with negative numbers, starting from -1:
planets [-1] 

# Slicing 
planets[0:3] # the first three planets 
planets [:3] # it assumed the start index to be 0
#If I leave out the end index, it's assumed to be the length of the list.
planets[3:] # "give me all the planets from index 3 onward"
planets [1:-1] # All the planets except the first and last
planets [-3:] # The last three planets 

# Changing Lists 
# Lists are "MUTABLE", meaning they can be modified "in place"
planets[3]="Malacandra"
planets[:3]=['Mur','Vee','Ur']
planets[:4] = ['Mercury', 'Venus', 'Earth', 'Mars',]

# List functions 
len(planets) # 8
sorted(planets) # The planets sorted in alphabetical order

primes=[2,3,5,7]
sum(primes) # 17
max(primes) # 7

# Interlude: objetcs
# Objects carry some things around with them 
# Access the stuff using Python's dot notation
x=12
print(x.imag)
# x is a real number, so its imaginary part is 0.
c=12+3j
print(c.imag)
# 3.0

# A function attached to an object is called a method
x.bit.length() # 4

# List methods
# list.append modifies a list by adding an item to the end:
planets.append('Pluto')
planets.pop() # 'Pluto' removes and returns the last element 

# Searching lists 
planets.index('Earth') #2
# Is Earth a planet?
"Earth" in planets # True
# Is Calbefraques a planet?
"Calbefraques" in planets # False

help(planets) # will tell us about all the list methods

# Tuples are almost the same as lists 
# Parenthesis instead of square brackets 
t = (1,2,3)
t = 1,2,3 # equivalent to above
# they cannot be modified, "IMMUTABLE"

# Tuples are often used for functions that have multiple return values.
x=0.125
x.as_integer_ratio()
# (1,8)

numerator,denominator = x.as_integer_ratio()
print (numerator/denominator)
# 0.125

#Finally we have some insight into the classic Stupid Python Trick™ for swapping two variables!
a=1
b=0
a,b = b,a
print (a,b)
# 0 1
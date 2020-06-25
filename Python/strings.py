# Strings
x="Plyto is a planet"
y='Pluto is a planet'
x == y
# True

print('My dog is named "Pluto"')

'Pluto\'s a planet'
hello = "hello\nworld"
# the newline character

triplequoted_hello = """hello
world"""
# just with enter
triplequoted_hello == hello

# Strings are sequences

#Indexing
planet = 'Pluto'
planet[0]
#P

#Slicing
planet[-3:]
#'uto'

#How long is the string?
len(planet)
#5

#Loop
[char +'!' for char in planet]
['P! ', 'l! ', 'u! ', 't! ', 'o! ']

# IMMUTABLE, cannot modify strings!

# String methods

# ALL CAPS
claim = "pluto is a planet!"
claim.upper()
#'PLUTO IS A PLANET'

# all lowercase
claim.lower()
#'pluto is a planet'

# searching for the first index of a substring
claim.index('plan')
#11

claim.startswith(planet)
#True

claim.endswith('dwarf planet')
#False

# str.split()  turns a string into a list of smaller strings, breaking on whitespace by default.
# This is super useful for taking you from one big string to a list of words.

words=claim.split()
words
# ['Pluto', 'is', 'a', 'planet!']

datestr='1956-01-31'
year, month, day = datestr.split('-')

# str.join() sew a list of strings up into one long string
# using the string it was called on as a separator

'/'.join([month,day,year])
# '01/31/1956'

# unicode magic 
' 👏'.join([word.upper() for word in words])
# 'PLUTO 👏 IS 👏 A 👏 PLANET!'

# .format()
# concatenate strings with the + operator

planet + ' , we miss you'
# 'Pluto, we miss you.'

planet + ", you will always be the " + str(position) + 'th planet to me.'
# "Pluto, you'll always be the 9th planet to me."

"{}, you'll always be the {}th planet to me.".format(planet, position)
# "Pluto, you'll always be the 9th planet to me."

pluto_mass = 1.303 * 10**22
earth_mass = 5.9722 * 10**24
population = 52910390
# 2 decimal points  3 decimal points, format as percent separate with commas
"{} weighs about {:.2} kilograms ({:.3%} of Earth's mass). It is home to {:,} Plutonians.".format(
    planet, pluto_mass, pluto_mass / earth_mass, population,
)
# "Pluto weighs about 1.3e+22 kilograms (0.218% of Earth's mass). It is home to 52,910,390 Plutonians."

# Referring to format() arguments by index, starting from 0
s = """Pluto's a {0}.
No, it's a {1}.
{0}!
{1}!""".format('planet', 'dwarf planet')
print(s)

# Pluto's a planet.
# No, it's a dwarf planet.
# planet!
# dwarf planet!



# Dictionaries

# Dictionaries are a built-in Python data structure for mapping keys to values.
numbers = {'one':1, 'two':2, 'three':3}
# In this case 'one', 'two', and 'three' are the keys, and 1, 2 and 3 are their corresponding values.

numbers['one']
# 1

# add another key
numbers['eleven']=11
numbers
# {'one': 1, 'two': 2, 'three': 3, 'eleven': 11}

# change the value 
numbers['one']='Pluto'
numbers
# {'one': 'Pluto', 'two': 2, 'three': 3, 'eleven': 11}

# dictionary comprehensions 
planets=['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
planet_to_initial = {planet: planet[0] for planet in planets}
planet_to_initial
# {'Mercury': 'M',
# 'Venus': 'V',
# 'Earth': 'E',
# 'Mars': 'M',
# 'Jupiter': 'J',
# 'Saturn': 'S',
# 'Uranus': 'U',
# 'Neptune': 'N'}

# The in operator tells us whether something is a key in the dictionary
'Saturn' in planet_to_initial
# True
'Betelgeuse' in planet_to_initial
# False

# for loop over a dictionary will loop over its keys
for k in numbers:
    print("{}={}".format(k,numbers[k]))
# one = Pluto
# two = 2
# three = 3
# eleven = 11

# access a collection of all the keys and the values with 
# dict.keys() and dict.values() 

# Get all the initials, sort them alphabetically, and put them in a space-separated string.
' '.join(sorted(planet_to_initial.values()))
# 'E J M M N S U V'

# dict.items() method lets us iterate over the keys and values
# item = key

for planet, initial in planet_to_initial.items():
    print("{} begins with \"{}\"".format(planet.rjust(10), initial))

#Mercury begins with "M"
#Venus begins with "V"
#Earth begins with "E"
#Mars begins with "M"
#Jupiter begins with "J"
#Saturn begins with "S"
#Uranus begins with "U"
#Neptune begins with "N"


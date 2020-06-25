# Loops
planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
for planet in planets:
    print(planet, end=' ') # print all on same line

multiplicands = (2,2,2,3,3,5)
product = 1
for mult in multiplicands:
    products = product * mult
product
# 360

# loop through each character in a string:
s = 'steganograpHy is the practicE of conceaLing a file, message, image, or video within another fiLe, message, image, Or video.'
msg = ''
# print all the uppercase letters in s, one at a time
for char in s:
    if char.isupper():
        print(char, end='')
# HELLO

# range()  is a function that returns a sequence of numbers. It turns out to be very useful for writing loops.
# for example if you want to repeat action 5 times

for i in range (5):
    print ("Doing important work. i=", i)
# Doing important work. i = 0
# Doing important work. i = 1
# Doing important work. i = 2
# Doing important work. i = 3
# Doing important work. i = 4

# while loops
i=0
while i<10:
    print (i, end='')
    i+=1
# 0 1 2 3 4 5 6 7 8 9 

# List compregensions 
squares = [n**2 for n in range (10)]
squares
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# the same thing without a list comprehension
squares =[]
for n in range (10):
    squares.append(n**2)
squares

# we can also add an if condition 
short_planets=[planet for planet in planets if len(planet)<6]
short_planets
# ['Venus', 'Earth', 'Mars']

# like a "WHERE" clause from SQL
# str.upper() returns an all-caps version of a string
loud_short_planets=[planets.upper() + '!' for planet in planets if len (planet)<6]
loud_short_planets
# ['VENUS!', 'EARTH!', 'MARS!']

[
    planet.upper() + '!' 
    for planet in planets 
    if len(planet) < 6
]
# Continuing the SQL analogy, you could think of these three lines as SELECT, FROM, and WHERE

[32 for planet in planets]
# [32, 32, 32, 32, 32, 32, 32, 32]

# 1 option 
def count_negatives(nums):
    """Return the number of negative numbers in the given list.
    
    >>> count_negatives([5, -1, -2, 0, 3])
    2
    """
    n_negative = 0
    for num in nums:
        if num < 0:
            n_negative = n_negative + 1
    return n_negative

# Here's a solution using a list comprehension:
# 2 option 
def count_negatives(nums):
    return len([num for num in nums if num < 0])

# 3 option
def count_negatives(nums):
    # Reminder: in the "booleans and conditionals" exercises, we learned about a quirk of 
    # Python where it calculates something like True + True + False + True to be equal to 3.
    return sum([num < 0 for num in nums])

# Solving a problem with less code is always nice, but it's worth keeping in mind the following lines from 
# The Zen of Python by Tim Peters:

# Beautiful is better than ugly.
# Explicit is better than implicit.
# Simple is better than complex.
# Complex is better than complicated.
# Flat is better than nested.
# Sparse is better than dense.
# Readability counts.
# Special cases aren't special enough to break the rules.
# Although practicality beats purity.
# Errors should never pass silently.
# Unless explicitly silenced.
# In the face of ambiguity, refuse the temptation to guess.
# There should be one—and preferably only one—obvious way to do it.
# Although that way may not be obvious at first unless you're Dutch.
# Now is better than never.
# Although never is often better than right now.
# If the implementation is hard to explain, it's a bad idea.
# If the implementation is easy to explain, it may be a good idea.
# Namespaces are one honking great idea—let's do more of those!

# 1 
pi = 3.14159 
diameter = 3
radius= 0.5 * (diameter)
area= pi * (radius**2)

#2
a = [1, 2, 3]
b = [3, 2, 1]
# swap the values to which a and b refer
tmp = a
a = b
b = tmp
# Python magic trick to swap two variables in one line:
a, b = b, a

#3 
#Alice, Bob and Carol have agreed to pool their Halloween candy and split it evenly among themselves.
#For the sake of their friendship, any candies left over will be smashed.For example, if they collectively
#bring home 91 candies, they'll take 30 each and smash 1.

alice_candies = 121
bob_candies = 77
carol_candies = 109

sum= alice_candies + bob_candies + carol_candies
to_smash = sum%3
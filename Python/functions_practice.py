#1 
def round_to_two_places(num):
    """Return the given number rounded to two decimal places. 
    
    >>> round_to_two_places(3.14159)
    3.14
    """
    return round(num,2)

#2
def round_to_negative(num):
    return round(num,-2)
print(round_to_negative(100.789))
# 100.0
# ndigits=-1 rounds to the nearest 10
# ndigits=-2 rounds to the nearest 100 

#3 
# It optionally takes a second argument representing the number of friends the candies are being split between. 
# If no second argument is provided, it should assume 3 friends, as before.
def to_smash(total_candies, n_friends=3):
    return total_candies % n_friends

#4
round_to_two_places(9.9999)
# 10.0

def smallest_abs(a,b):
    # Which of the two variables above has the smallest absolute value?
    i1 = abs(a)
    i2 = abs(b)
    return min(i1,i2)

def f(x):
    y = abs(x)
    return y

print(f(5))
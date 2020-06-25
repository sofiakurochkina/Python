# 1
def sign(x):
    if x > 0:
        return 1
    elif x < 0:
        return -1
    else:
        return 0

# 2 
def to_smash(total_candies):
    """Return the number of leftover candies that must be smashed after distributing
    the given number of candies evenly between 3 friends.
    
    >>> to_smash(91)
    1
    """
    print("Splitting", total_candies, "candy" if total_candies == 1 else "candies")
    return total_candies % 3

# 3
def prepared_for_weather(have_umbrella, rain_level, have_hood, is_workday):
    return have_umbrella or rain_level < 5 and have_hood or (not rain_level > 0 and is_workday)
have_umbrella = False
rain_level = 0.00
have_hood = False
is_workday = False
actual = prepared_for_weather(have_umbrella, rain_level, have_hood, is_workday)

# 4
def is_negative(number):
    if number <0: 
        return True
    else:
        return False

def concise_is_negative(number):
    return number <0

# 5
def onionless(ketchup, mustard, onion):
    """Return whether the customer doesn't want onions.
    """
    return not onion

def wants_all_toppings(ketchup, mustard, onion):
    """Return whether the customer wants "the works" (all 3 toppings)
    """
    return ketchup and mustard and onion

def wants_plain_hotdog(ketchup, mustard, onion):
    """Return whether the customer wants a plain hot dog with no toppings.
    """
    # return not ketchup and not mustard and not onion
    return not (ketchup or mustard or onion)

def exactly_one_sauce(ketchup, mustard, onion):
        """Return whether the customer wants either ketchup or mustard, but not both.
    (You may be familiar with this operation under the name "exclusive or")
    """
    return (ketchup and not mustard) or (mustard and not ketchup)

# 6
def exactly_one_topping(ketchup, mustard, onion):
    """Return whether the customer wants exactly one of the three available toppings
    on their hot dog.
    """
    # return (int(ketchup) + int(mustard) + int(onion)) == 1
    # Python implicitly does the integer conversion
    return (ketchup + mustard + onion) == 1

# 7 blackjack ( aka twenty-one )
def should_hit(player_total, dealer_total, player_aces):
    """Return True if the player should hit (request another card) given the current game
    state,
    or False if the player should stay. player_aces is the number of aces the player has.
    """
    if player_aces > 0:
        return True if player_total <= 17 else False
    else:
        if player_total <= 17 and dealer_total >=7: 
            return True 
        elif dealer_total < 7: 
            return player_total <= 17 
        else: 
            return False 
    return False
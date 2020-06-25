# 1
def select_second(L):
    """Return the second element of the given list. If the list has no second
    element, return None.
    """
    if len(L)<2:
        return None
    return L[1]

# 2
def losing_team_captain(teams):
    """Given a list of teams, where each team is a list of names, return the 2nd player (captain)
    from the last listed team
    """
    return teams[-1][1]

# 3
def purple_shell(racers):
    """Given a list of racers, set the first place racer (at the front of the list) to last
    place and vice versa.
    
    >>> r = ["Mario", "Bowser", "Luigi"]
    >>> purple_shell(r)
    >>> r
    ["Luigi", "Bowser", "Mario"]
    """
    # One slick way to do the swap is x[0], x[-1] = x[-1], x[0].
    temp = racers[0]
    racers[0] = racers[-1]
    racers[-1] = temp

# 4
a = [1, 2, 3]
b = [1, [2, 3]]
c = []
d = [1, 2, 3][1:]

# Put your predictions in the list below. Lengths should contain 4 numbers, the
# first being the length of a, the second being the length of b and so on.
lengths = [3, 2, 0, 2]
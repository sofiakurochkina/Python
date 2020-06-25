# 1
def has_lucky_number(nums):
    """Return whether the given list of numbers is lucky. A lucky list contains
    at least one number divisible by 7.
    """
    return any([num % 7 == 0 for num in nums])

# 2
[1, 2, 3, 4] > 2
# TypeError
# R and Python have some libraries (like numpy and pandas) compare each element of the list to 2
def elementwise_greater_than(L, thresh):
    """Return a list with the same length as L, where the value at index i is 
    True if L[i] is greater than thresh, and False otherwise.
    
    >>> elementwise_greater_than([1, 2, 3, 4], 2)
    [False, False, True, True]
    """
    res = []
    for ele in L:
        res.append(ele > thresh)
    return res

# the list comprehension version :
def elementwise_greater_than(L, thresh):
    return [ele > thresh for ele in L]

# 3
def menu_is_boring(meals):
    """Given a list of meals served over some period of time, return True if the
    same meal has ever been served two days in a row, and False otherwise.
    """
    for i in range (len(meals)-1):
        if meals[i]== meals[i+1]:
            return True
    return False

# 4
# Monte Carlo method
# To estimate the average outcome, we simulate the scenario many times, and return the average result.

def slots_survival_probability(start_balance, n_spins, n_simulations):
    """Return the approximate probability (as a number between 0 and 1) that we can complete the 
    given number of spins of the slot machine before running out of money, assuming we start 
    with the given balance. Estimate the probability by running the scenario the specified number of times.
    
    >>> slots_survival_probability(10.00, 10, 1000)
    1.0
    >>> slots_survival_probability(1.00, 2, 1000)
    .25
    """
    successes = 0
    # A convention in Python is to use '_' to name variables we won't use
    for _ in range(n_simulations):
        balance = start_balance
        spins_left = n_spins
        while balance >= 1 and spins_left:
            # subtract the cost of playing
            balance -= 1
            balance += play_slot_machine()
            spins_left -= 1
        # did we make it to the end?
        if spins_left == 0:
            successes += 1
    return successes / n_simulations
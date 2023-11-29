"""
Example of a recursive function that computes the
number of threes in the decimal form of a number
"""

def number_of_threes(num):
    """
    Takes a non-negative integer num and compute the 
    number of threes in its decimal form
    Returns an integer
    """
    if num == 0:
        return 0
    else:
        unit_digit = num % 10
        threes_in_rest = number_of_threes(num // 10)
        if unit_digit == 3:
            return threes_in_rest + 1
        else:
            return threes_in_rest
    
print(number_of_threes(5))

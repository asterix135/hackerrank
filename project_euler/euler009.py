"""
https://www.hackerrank.com/contests/projecteuler/challenges/euler009
"""

# form a pythagorean triple summing to N
# N = 2n**2 + 2 mn
# a = n**2 - m**2
# b = 2nm
# c = n**2 + m**2

# smallest is 3, 4, 5; N=12, n=1, m=2

"""
https://www.hackerrank.com/contests/projecteuler/challenges/euler009

Need O(n)
"""


def pythagorean_triplet(val1, sum_of_vals):
    """
    takes a sum of values and one test member of a potential pythagorean
    triplet.  Tests to see whether there is a pythagorean triplet that sums
    to the given sum and includes test_val.
    Returns a tuple of (-1, -1, -1) if the condition cannot be met
    or a tuple of 3 integers indicating the 3 triplet members (sum is 3rd)
    """
    pass

# the difference between squares increases/decreases by 2 per +1 in both vals



def max_triplet(num):
    """
    For the given num, checks to see if there is a set of 3 integers
    that make up a pythagorean equation and where the sum of those
    3 integers is num
    Returns the highest product of integers that meet this condition
    or -1 if the condition cannot be met
    """
    max_sum = -1
    for a_num in range(2, num):
        test_num = 0


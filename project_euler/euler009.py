"""
https://www.hackerrank.com/contests/projecteuler/challenges/euler009
Need O(n)
"""

# form a pythagorean triple summing to N
# N = 2n**2 + 2 mn
# a = n**2 - m**2
# b = 2nm
# c = n**2 + m**2

# smallest is 3, 4, 5; N=12, n=1, m=2

import math

# this is not right
def max_triplet(num):
    """
    For the given num, checks to see if there is a set of 3 integers
    that make up a pythagorean equation and where the sum of those
    3 integers is num
    Returns the highest product of integers that meet this condition
    or -1 if the condition cannot be met
    """
    if num < 12:
        return -1
    max_sum = -1
    # test if there is a perfect square
    for n_factor in range(2, math.floor(math.sqrt(num))):
        m_factor = num/(2 * n_factor) - n_factor
        if m_factor == int(m_factor):
            factor_product = ((n_factor**2 + 2 * n_factor * m_factor) *
                              (2 * n_factor * m_factor) *
                              (n_factor**2 + m_factor**2))
            if factor_product > max_sum and factor_product > 0:
                max_sum = int(factor_product)
    return max_sum


for i in range(12, 100):
    print(i)
    print(max_triplet(i))

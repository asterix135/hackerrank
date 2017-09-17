"""
https://www.hackerrank.com/contests/projecteuler/challenges/euler009
Need O(n)
"""

# form a pythagorean triple summing to N (primitives, not all multiples)
# N = 2n**2 + 2 mn
# a = n**2 - m**2
# b = 2nm
# c = n**2 + m**2

# smallest is 3, 4, 5; N=12, n=1, m=2

import math


def max_triplet(num):
    """
    For the given num, checks to see if there is a set of 3 integers
    that make up a pythagorean equation and where the sum of those
    3 integers is num
    Returns the highest product of integers that meet this condition
    or -1 if the condition cannot be met
    :param num: integer
    """
    # Min value of num is 12
    if num < 12:
        return -1

    max_sum = -1
    for n in range(2, math.floor(math.sqrt(num)) + 1):
        for m in range(1, n):
            if num % (2 * n**2 + 2 * m * n) == 0:
                multiplier = num / (2 * n**2 + 2 * m * n)
                a = n**2 - m**2
                b = 2 * n * m
                c = n**2 + m**2
                factor_product = a * b * c * multiplier**3
                if factor_product > max_sum and factor_product > 0:
                    max_sum = int(factor_product)
    return max_sum


def run_battery():
    """
    outer routine to run battery of tests on hackerrank site
    """
    num_tests = int(input())
    all_answers = []
    for idx in range(num_tests):
        test_sum = int(input())
        answer = max_triplet(test_sum)
        print(answer)
        all_answers.append(answer)
    return all_answers


run_battery()

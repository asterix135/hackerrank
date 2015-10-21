"""
https://www.hackerrank.com/contests/projecteuler/challenges/euler001
"""


def mults_3_5_iterative():
    """
    reads in 2 inputs:
    T - number of test cases
    T lines indicating N upper limit of range
    for each line, calculate & print sum of integers below N that are
    multiples of 3 or 5
    return these sums as a list
    This times out - O(n)
    """
    num_tests = int(input())
    all_sums = []
    for idx in range(num_tests):
        limit = int(input())
        test_sum = 0
        for num in range(limit):
            if num % 3 == 0 or num % 5 == 0:
                test_sum += num
        print(test_sum)
        all_sums.append(test_sum)
    return all_sums

def mults_3_5_new():
    """
     reads in 2 inputs:
    T - number of test cases
    T lines indicating N upper limit of range
    for each line, calculate & print sum of integers below N that are
    multiples of 3 or 5
    return these sums as a list
    O(1)
    """
    num_tests = int(input())
    all_sums = []
    for idx in range(num_tests):
        lim = int(input()) - 1
        test_sum = int(3 * ((lim // 3) * ((lim // 3) + 1) // 2 ) +
                       5 * ((lim // 5) * ((lim // 5) + 1) // 2) -
                       15 * ((lim // 15) * ((lim // 15)  + 1) // 2))
        print(test_sum)
        all_sums.append(test_sum)
    return all_sums


mults_3_5_new()

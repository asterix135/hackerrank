"""
https://www.hackerrank.com/contests/projecteuler/challenges/euler008
"""

from collections import deque


def list_product(lst):
    """
    returns product of a list made up of numbers
    """
    prod = 1
    for val in lst:
        prod *= val
    return prod


def find_largest_product(k_digits, num, num_len):
    """
    for a number with num_len digits, finds and returns the largest product
    made up of k digits in that number
    """
    factor_queue = deque()
    exp_val = num_len - 1
    for dummy_val in range(k_digits):
        factor_queue.append(int(str(num // 10 ** exp_val)[-1]))
        exp_val -= 1
    max_product = list_product(factor_queue)
    while exp_val:
        factor_queue.popleft()
        factor_queue.append(int(str(num // 10 ** exp_val)[-1]))
        exp_val -= 1
        test_prod = list_product(factor_queue)
        if test_prod > max_product:
            max_product = test_prod
    return max_product


def run_battery():
    """
    outer routine to run battery of tests on hackerrank site
    """
    num_tests = int(input())
    all_answers = []
    for idx in range(num_tests):
        input_parms = [int(itm) for itm in input().split()]
        num_len, k_val = input_parms[0], input_parms[1]
        num = int(input())
        answer = find_largest_product(k_val, num, num_len)
        print(answer)
        all_answers.append(answer)
    return all_answers


run_battery()

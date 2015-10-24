"""
https://www.hackerrank.com/contests/projecteuler/challenges/euler007
Note that this is designed to optimize for parameters of hackerrank page
where we are not looking for greater than the 10^4th prime.
For higher values, increase the global MULTIPLIER
"""

import math
MULTIPLIER = 11


def find_primes(num):
    """
    Use sieve methods to find all primes between 1 and upper limit
    returns list of primes
    0.17 secs for 10^6
    """
    num_root = int(math.sqrt(num))
    sieve = list(range(num + 1))
    sieve[1] = 0
    for idx in range(2, num_root + 1):
        if sieve[idx] != 0:
            mults = num // idx - idx
            sieve[idx * idx: num+1: idx] = [0] * (mults + 1)
    return [val for val in sieve if val != 0]


def run_prob7():
    """
    outer routine to run battery of tests on hackerrank for 7th Euler problem
    """
    num_tests = int(input())
    input_list = []
    all_answers = []
    for dummy_idx in range(num_tests):
        val = int(input())
        input_list.append(val)
    prime_list = find_primes(max(input_list) * MULTIPLIER)
    for val in input_list:
        answer = prime_list[val-1]
        print(answer)
        all_answers.append(answer)
    return all_answers


run_prob7()

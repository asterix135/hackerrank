"""
https://www.hackerrank.com/contests/projecteuler/challenges/euler010

Key here is to create a lookup table since we'd be doing the same calculation
over and over again
"""

import math

### Biggest prime gap at 10^6 is about 114


def find_primes(num):
    """
    Use sieve methods to find all primes between 1 and upper limit
    returns list of primes
    0.17 secs for 10^6
    :param num: integer
    :return: list of primes
    """
    num_root = int(math.sqrt(num))
    sieve = list(range(num + 1))
    sieve[1] = 0
    for idx in range(2, num_root + 1):
        if sieve[idx] != 0:
            mults = num // idx - idx
            sieve[idx * idx: num+1: idx] = [0] * (mults + 1)
    return [val for val in sieve if val != 0]


def make_prime_sum_lookup(num):
    """
    Creates an ordered list in which the ith element is the sum of the
    primes less than i
    :param num: ingeger
    :return: list of prime sums
    """
    prime_list = find_primes(num + 125)
    prime_idx = 0
    current_sum = 0
    sum_list = []
    for num_idx in range(num + 1):
        if prime_list[prime_idx] <= num_idx:
            current_sum += prime_list[prime_idx]
            prime_idx += 1
        sum_list.append(current_sum)
    return sum_list


def run_battery():
    """
    outer routine to run battery of tests on hackerrank site
    """
    num_tests = int(input())
    all_inputs = []
    for idx in range(num_tests):
        all_inputs.append(int(input()))
    max_input = max(all_inputs)
    all_answers = []
    prime_sums = make_prime_sum_lookup(max_input)
    for num in all_inputs:
        answer = prime_sums[num]
        print(answer)
        all_answers.append(answer)
    return all_answers


run_battery()

"""
https://www.hackerrank.com/contests/projecteuler/challenges/euler005

Method: get a dictionary of primes in range
prime factor each number in range; make sure dictionary value is correct
multiply dictionary keys to power of value
"""

import math


def find_primes(num):
    """
    Use sieve methods to find all primes between 1 and upper limit
    returns dictionary with primes as keys, values as 0
    """
    num_root = int(math.sqrt(num))
    sieve = list(range(num + 1))
    sieve[1] = 0
    for idx in range(2, num_root + 1):
        if sieve[idx] != 0:
            mults = num // idx - idx
            sieve[idx * idx: num+1: idx] = [0] * (mults + 1)
    return {val: 0 for val in sieve if val != 0}
    # return [val for val in sieve if val != 0]


def find_prime_factors(num):
    """
    finds the prime factors of num
    returns as a dictionary
    """
    prime_factors = find_primes(num)
    for prime in prime_factors:
        num_copy = num
        while num_copy % prime == 0:
            num_copy //= prime
            prime_factors[prime] += 1
    return prime_factors


def find_smallest_quotient(num):
    """
    returns the smallest number that is evenly divisible by all the integers
    from 1 to num (inclusive)
    returns that number
    """
    prime_dict = find_primes(num)
    for val in range(2, num + 1):
        val_factors = find_prime_factors(val)
        for factor in val_factors:
            if val_factors[factor] > prime_dict[factor]:
                prime_dict[factor] = val_factors[factor]
    quotient = 1
    for factor in prime_dict:
        quotient *= factor**prime_dict[factor]
    return quotient


def run_battery():
    """
    outer routine to run battery of tests on hackerrank site
    """
    num_tests = int(input())
    all_answers = []
    for idx in range(num_tests):
        num = int(input())
        answer = find_smallest_quotient(num)
        print(answer)
        all_answers.append(answer)
    return all_answers


run_battery()

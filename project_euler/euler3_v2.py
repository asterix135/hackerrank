"""
2nd attempt to solve problem 3 quickly
Method: find primes & test against given number
https://www.hackerrank.com/contests/projecteuler/challenges/euler003
"""

import time
import math


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


def find_largest_prime_factor(num):
    """
    Takes a number as input and returns the largest prime factor
    """
    prime_list = find_primes(int(math.sqrt(num)) + 1)
    max_prime = 0
    for factor in prime_list:
        if num % factor == 0:
            if num // factor > max_prime:
                factor2_lg_prime = find_largest_prime_factor(num // factor)
                if factor2_lg_prime > max_prime:
                    max_prime = num // factor
            elif factor > max_prime:
                max_prime = factor
    if max_prime == 0:
        max_prime = num
    return max_prime


def test_speed(num_its, func):
    """
    check algo time for 10^0 - 10^num_its
    """
    time_results = {}
    for idx in range(num_its):
        start_time = time.time()
        func(10**idx)
        end_time = time.time()
        time_results[idx] = end_time - start_time
    return time_results


def run_battery():
    """
    outer routine to run battery of test on hackerrank site
    """
    num_tests = int(input())
    all_large_prime_factors = []
    for idx in range(num_tests):
        num = int(input())
        prime = find_largest_prime_factor(num)
        print(prime)
        all_large_prime_factors.append(prime)
    return all_large_prime_factors


run_battery()

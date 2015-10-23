"""
https://www.hackerrank.com/contests/projecteuler/challenges/euler005

To solve - find prime factors of each number to N
add factors to a set
multiple set elements together

"""

import math


def find_primes(num):
    """
    Use sieve methods to find all primes between 1 and upper limit
    returns list of primes
    """
    num_root = int(math.sqrt(num))
    sieve = list(range(num + 1))
    sieve[1] = 0
    for idx in range(2, num_root + 1):
        if sieve[idx] != 0:
            mults = num // idx - idx
            sieve[idx * idx: num+1: idx] = [0] * (mults + 1)
    return [val for val in sieve if val != 0]


def find_prime_factors(num):
    """
    finds the prime factors of num
    returns as a set
    """
    prime_factors = set([])
    for prime in find_primes(num):
        if num % prime == 0:
            prime_factors.add(prime)
    return prime_factors


def find_divisible_by(num):
    """
    returns the smallest number that is evenly divisible by all the integers
    from 1 to num (inclusive)
    returns that number
    """
    all_prime_factors = set([])
    for test_num in range(2, num+1):
        all_prime_factors.union(find_prime_factors(test_num))
    answer = 1
    for val in all_prime_factors:
        answer *= val
    return answer


def run_battery():
    """
    outer routine to run battery of tests on hackerrank site
    """
    num_tests = int(input())
    all_answers = []
    for idx in range(num_tests):
        num = int(input())
        answer = find_divisible_by(num)
        print(answer)
        all_answers.append(answer)
    return all_answers


print(find_divisible_by(10))

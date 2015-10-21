"""
https://www.hackerrank.com/contests/projecteuler/challenges/euler003
"""


def find_largest_prime_factor(num):
    """
    for a series of test cases, find and print the largest prime factor
    for each test case
    return list of largest prime factors
    takes too long for large primes O(n)???
    """
    max_prime = 1
    # factor out all 2's
    while num % 2 == 0:
        max_prime = 2
        num //= 2
    test_prime = 3
    while num > 1:
        while num % test_prime == 0:
            if test_prime > max_prime:
                max_prime = test_prime
            num //= test_prime
        test_prime += 2
        if test_prime ^ 2 > num:
            if num > 1 and num > max_prime:
                max_prime = num
                break
    return max_prime


def find_largest_prime2(num):
    """
    for a series of test cases, find and print the largest prime factor
    for each test case
    return list of largest prime factors
    """
    test_prime = 2
    max_prime = 1
    while test_prime ^ 2 <= num:
        if num % test_prime != 0:
            test_prime += [1, 2][test_prime > 2]
        else:
            num //= test_prime
            max_prime = test_prime
    if num > 1:
        max_prime = num
    return max_prime


def run_battery():
    """
    outer routine to run battery of test on hackerrank site
    """
    # import time
    # start_time = time.time()
    num_tests = int(input())
    all_large_prime_factors = []
    for idx in range(num_tests):
        num = int(input())
        prime = find_largest_prime2(num)
        print(prime)
        all_large_prime_factors.append(prime)
    # print('run time: ' + str(time.time() - start_time))
    return all_large_prime_factors


run_battery()

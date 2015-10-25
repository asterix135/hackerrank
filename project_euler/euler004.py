"""
https://www.hackerrank.com/contests/projecteuler/challenges/euler004

note: problem limits input to 6-digit numbers
"""

import math


def find_next_palindrome(num):
    """
    finds first palindromic number less than num and returns it
    """
    test_num = num - 1
    found_palindrome = is_palindrome(test_num)
    while not found_palindrome:
        test_num -= 1
        found_palindrome = is_palindrome(test_num)
    return test_num


def is_palindrome(num):
    """
    Takes an integer as input
    Returns a boolean indicating whether the number is a palindrome
    """
    for idx in range(len(str(num))//2):
        last = str(num // 10**idx)[-1]
        first = str(num // 10**(len(str(num)) - 1 - idx))[-1]
        if last != first:
            return False
    return True


def check_divisibility(num):
    """
    Checks is num is divisible by 2 3-digit numbers
    returns boolean
    """
    for divisor in range(100, int(math.sqrt(num)) + 1):
        if num % divisor == 0 and 99 < num // divisor < 1000:
            return True
    return False


def find_divisible_palindrome(num):
    """
    takes an integer as an input
    returns the next lowest number that is a palindrome
        and is divisible by 2 3-digit numbers
    """
    palin_found = False
    test_num = num
    while not palin_found:
        test_num = find_next_palindrome(test_num)
        palin_found = check_divisibility(test_num)
    return test_num


def run_battery():
    """
    outer routine to run battery of tests on hackerrank site
    """
    num_tests = int(input())
    all_answers = []
    for idx in range(num_tests):
        num = int(input())
        answer = find_divisible_palindrome(num)
        print(answer)
        all_answers.append(answer)
    return all_answers


run_battery()

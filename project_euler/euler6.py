"""
https://www.hackerrank.com/contests/projecteuler/challenges/euler006
"""


def find_square_difference(num):
    """
    Find the difference between (1^2 + 2^2 + ... n^2) and
        (1 + 2 + ... n)^2
    """
    square_of_sums = (num * (num + 1) // 2)**2
    sum_of_squares = (num * (num + 1) * (2 * num + 1)) // 6
    return square_of_sums - sum_of_squares


def run_battery():
    """
    outer routine to run battery of tests on hackerrank site
    """
    num_tests = int(input())
    all_answers = []
    for idx in range(num_tests):
        num = int(input())
        answer = find_square_difference(num)
        print(answer)
        all_answers.append(answer)
    return all_answers


run_battery()

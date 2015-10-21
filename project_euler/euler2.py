"""
https://www.hackerrank.com/contests/projecteuler/challenges/euler002
"""

# every 3rd term is even
# even term E(n)can be expressed as E(n)= 4*E(n-1) + E(n-2)


def fibonacci_even_sum():
    """
    sums even values of fibonacci sequence
    up to provided limits
    prints each value & returns list of all answers
    """
    num_tests = int(input())
    all_sums = []
    for idx in range(num_tests):
        lim = int(input())
        test_sum = 2
        num1 = 1
        num2 = 2
        while num1 + num2 < lim:
            new_num = num1 + num2
            if new_num % 2 == 0:
                test_sum += new_num
            num1 = num2
            num2 = new_num
        print(test_sum)
        all_sums.append(test_sum)
    return all_sums


fibonacci_even_sum()

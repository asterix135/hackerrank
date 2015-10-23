"""
https://www.hackerrank.com/challenges/simple-array-sum
"""


def simple_array_sum():
    """
    add up numbers in an array, with provided array length
    """
    num_lines = int(input())
    num_list = [int(itm) for itm in input().split()]
    return sum(num_list)


print(simple_array_sum())

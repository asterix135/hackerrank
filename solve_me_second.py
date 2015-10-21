"""
Some of the basic i/o stuff
"""


def solve_me_second(c, d):
    return c + d


n = int(input())

for i in range(0, n):
    a, b = input().split()
    a, b = int(a), int(b)
    res = solve_me_second(a, b)
    print(res)

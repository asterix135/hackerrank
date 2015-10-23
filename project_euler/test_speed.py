"""
function to test speed of another function
"""

import time


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

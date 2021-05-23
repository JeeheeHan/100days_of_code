"""Coding practice"""
from typing import DefaultDict
import unittest
import time

class Problem(object):
    def two_sum(self, nums, target):
        """
        Given a list of integers and the target sum, return the indices of the two numbers that add up to the target
        """
        d = {}
        for indice, num in enumerate(nums):
            diff = target - num
            if diff not in d:
                d[num] = indice
            else:
                return [d[diff], indice]

class Test(unittest.TestCase):
    test_cases = [
        ([[1,2,5,8,10], 6], [0.2]),
        ([[1,8,22,8,10], 16],[1,3]),
        ([[1,8,265,9,88], 274],[2,4])
    ]

    def testing_functions(self):
        times_to_run = 1000
        function_runtimes = DefaultDict(float)
        
        for num in range(times_to_run):
            for num_target, expected in self.test_cases:
                test_function = Problem().two_sum
                start = time.perf_counter()
                assert(test_function(num_target[0], num_target[1]) == expected), f"two_sum failed for {num_target}"
                function_runtimes[t.two_sum.__name__] += (
                    time.perf_counter - start
                ) * 1000
        print(f"\nRan{times_to_run} times")

        for function_ran, runtime in function_runtimes.items():
            print(f"{function_ran}:{runtime:.1f} ms")

if __name__ == "__main__":
    unittest.main()
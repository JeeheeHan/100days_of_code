"""Today's whiteboarding session question given by Muna"""
from collections import defaultdict
import unittest
import time

class Problem(object):
    """3 different ways 1 problem"""
    #SOLUTION 1       
    def decoder_using_range(self,text):
        """For loop of range of len(text)"""
        if text == "":
            return text

        answer = ""

        for i in range(len(text)-1):
            if text[i].isdigit():
                steps = int(text[i]) + 1
                answer += text[i + steps]
            
        return answer

    #SOLUTION 2
    def decoder_while(self,text):
        """While i is less than the len(text)"""
        answer = ""
        i = 0

        while i < len(text):
            steps = int(text[i])
            i += steps + 1
            answer += text[i]
            i += 1

        return answer
    
    #SOLUTION 3
    def decoder_enumerate(self,text):
        """Use enumerate to get index, data and use tuple unpacking"""

        answer = ""

        for i, letter in enumerate(text):
            if letter.isdigit():
                steps = int(letter) + 1
                answer += text[i + steps]
        
        return answer

class Test(unittest.TestCase):
    test_cases = [
        ("0h1ae2bcy", "hey"),
        ("0M2abi2bci0n0e", "Miine"),
        ("2abh", "h")
    ]

    function_runtimes = defaultdict(float)
    
    def testing_decoder_using_range(self):
        times_to_run = 100
        test_function = Problem().decoder_using_range

        for num in range(times_to_run):
            for text, expected in self.test_cases:
                start = time.perf_counter()
              
                assert (test_function(text) == expected),\
                    f"{test_function.__name__} failed for {expected}"

                self.function_runtimes[test_function.__name__] += (
                    time.perf_counter() - start
                ) * 1000
        print(f"Testing for {test_function.__name__}")
        print(f"\nRan{times_to_run} times")

    def testing_decoder_while(self):
        times_to_run = 100
        test_function = Problem().decoder_while

        for num in range(times_to_run):
            for text, expected in self.test_cases:
                start = time.perf_counter()
              
                assert (test_function(text) == expected),\
                    f"{test_function.__name__} failed for {expected}"

                self.function_runtimes[test_function.__name__] += (
                    time.perf_counter() - start
                ) * 1000
        print(f"Testing for {test_function.__name__}")
        print(f"\nRan{times_to_run} times")

    def testing_decoder_enumerate(self):
        times_to_run = 100
        test_function = Problem().decoder_enumerate

        for num in range(times_to_run):
            for text, expected in self.test_cases:
                start = time.perf_counter()
              
                assert (test_function(text) == expected),\
                    f"{test_function.__name__} failed for {expected}"

                self.function_runtimes[test_function.__name__] += (
                    time.perf_counter() - start
                ) * 1000
  
        print(f"Testing for {test_function.__name__}")
        print(f"\nRan{times_to_run} times")

    
    def testing_print_runtimes(self):
        for function_ran, runtime in self.function_runtimes.items():
            print(f"{function_ran}:{runtime:.1f} ms")


if __name__ == "__main__":
    unittest.main()

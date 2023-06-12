import unittest
from pythonlang.highest_lowest import high_and_low

class TestFunc(unittest.TestCase):
    def test_assertation(self):

        numbers = "-59 359 -185 250 -916 402 257 333 663 986 962 134 -715 -582 477"
        expectedResult = "986 -916"
    
        result = high_and_low(numbers)
        
        self.assertEqual(result, expectedResult)


if __name__ == '__main__':
    unittest.main()
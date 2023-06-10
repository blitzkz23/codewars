import unittest
from pythonlang.sum_of_numbers import get_sum

class TestFunc(unittest.TestCase):
    def test_assertation(self):
        num1 = 789
        num2 = 45
        
        expectedResult = 310665
        result = get_sum(789, 45)

if __name__ == '__main__':
    unittest.main()
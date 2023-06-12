import unittest
from pythonlang.grasshopper_summation import summation

class TestFunc(unittest.TestCase):
    def test_assertation(self):

        numbers = 22
        expectedResult = 253
    
        result = summation(numbers)
        
        self.assertEqual(result, expectedResult)


if __name__ == '__main__':
    unittest.main()
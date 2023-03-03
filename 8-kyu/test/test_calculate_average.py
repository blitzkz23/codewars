import unittest
from pythonlang.calculate_average import find_average

class TestFunc(unittest.TestCase):
    def test_assertation(self):

        numbers = [1, 2, 3]
        expectedResult = 2
    
        result = find_average(numbers)
        
        self.assertEqual(result, expectedResult)


if __name__ == '__main__':
    unittest.main()
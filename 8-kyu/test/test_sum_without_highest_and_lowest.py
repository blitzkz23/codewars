import unittest
from pythonlang.sum_without_highest_and_lowest import sum_array

class TestFunc(unittest.TestCase):
    def test_assertation(self):

        arr = [6, 2, 1, 8, 10]
        expectedResult = 16
    
        result = sum_array([6, 2, 1, 8, 10])
        
        self.assertEqual(result, expectedResult)


if __name__ == '__main__':
    unittest.main()
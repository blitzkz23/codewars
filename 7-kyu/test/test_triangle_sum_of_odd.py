import unittest
from pythonlang.triangle_sum_of_odd_num import row_sum_odd_numbers

class TestFunc(unittest.TestCase):
    def test_assertation(self):
        
        n = 13
        expectedResult = 2197
    
        result = row_sum_odd_numbers(n)
        
        self.assertEqual(result, expectedResult)


if __name__ == '__main__':
    unittest.main()
import unittest
from pythonlang.count_by_x import count_by

class TestFunc(unittest.TestCase):
    def test_calculate_bmi(self):

        x, n = 50, 5
        expectedResult = [50, 100, 150, 200, 250]
    
        result = count_by(x, n)
        
        self.assertEqual(result, expectedResult)


if __name__ == '__main__':
    unittest.main()
import unittest
from pythonlang.calculate_bmi import bmi

class TestFunc(unittest.TestCase):
    def test_calculate_bmi(self):

        weight, height = 50, 1.80
        expectedResult = 'Underweight'
    
        result = bmi(weight, height)
        
        self.assertEqual(result, expectedResult)


if __name__ == '__main__':
    unittest.main()
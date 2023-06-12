import unittest
from pythonlang.will_you_make_it import zero_fuel

class TestFunc(unittest.TestCase):
    def test_assertation(self):

        dist = 100
        mpg = 50
        fuel_left = 1
        expectedResult = False
    
        result = zero_fuel(dist, mpg, fuel_left)
        
        self.assertEqual(result, expectedResult)


if __name__ == '__main__':
    unittest.main()
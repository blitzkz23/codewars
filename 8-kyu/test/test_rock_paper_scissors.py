import unittest
from pythonlang.transporation_on_vacation import rental_car_cost

class TestFunc(unittest.TestCase):
    def test_assertation(self):

        d = 8
        expectedResult = 270
    
        result = rental_car_cost(d)
        
        self.assertEqual(result, expectedResult)


if __name__ == '__main__':
    unittest.main()
import unittest
from pythonlang.growth_of_a_population import nb_year

class TestFunc(unittest.TestCase):
    def test_growth_of_a_population(self):

        p0, percent, aug, p = 1500000, 0.25, 1000, 2000000
        expectedResult = 94
    
        result = nb_year(p0, percent, aug, p)
        
        self.assertEqual(result, expectedResult)


if __name__ == '__main__':
    unittest.main()
import unittest
from pythonlang.area_or_perimeter import area_or_perimeter

class TestFunc(unittest.TestCase):
    def test_assertation(self):

        l = 6
        w = 10
        expectedResult = 32
    
        result = area_or_perimeter(l, w)
        
        self.assertEqual(result, expectedResult)


if __name__ == '__main__':
    unittest.main()
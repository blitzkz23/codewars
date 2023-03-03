import unittest
from pythonlang.the_feast_of_many_beast import feast

class TestFunc(unittest.TestCase):
    def test_assertation(self):

        beast = "great blue heron"
        dish = "garlic naan"
        expectedResult = True
    
        result = feast(beast, dish)
        
        self.assertEqual(result, expectedResult)


if __name__ == '__main__':
    unittest.main()
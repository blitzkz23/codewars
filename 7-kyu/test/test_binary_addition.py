import unittest
from pythonlang.binary_addition import add_binary

class TestFunc(unittest.TestCase):
    def test_assertation(self):

        a, b = 51, 12
        expectedResult = "111111"
    
        result = add_binary(a, b)
        
        self.assertEqual(result, expectedResult)


if __name__ == '__main__':
    unittest.main()
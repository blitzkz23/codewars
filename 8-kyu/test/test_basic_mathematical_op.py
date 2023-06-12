import unittest
from pythonlang.basic_mathematical_op import basic_op

class TestFunc(unittest.TestCase):
    def test_assertation(self):

        operator = '/'
        value1 = 49
        value2 = 7
        expectedResult = 7
    
        result = basic_op(operator, value1, value2)
        
        self.assertEqual(result, expectedResult)


if __name__ == '__main__':
    unittest.main()
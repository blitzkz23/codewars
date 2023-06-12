import unittest
from pythonlang.even_or_odd import even_or_odd

class TestFunc(unittest.TestCase):
    def test_even_or_odd(self):

        data = 99
        data2 = 80
        expectedResult1 = 'Odd'
        expectedResult2 = 'Even'
    
        result = even_or_odd(data)
        result2 = even_or_odd(data2)
        
        self.assertEqual(result, expectedResult1)
        self.assertEqual(result2, expectedResult2)


if __name__ == '__main__':
    unittest.main()
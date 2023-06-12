import unittest
from pythonlang.odd_or_even import odd_or_even

class TestFunc(unittest.TestCase):
    def test_assertation(self):

        arr = [1023, 1, 2]
    
        expectedResult = 'even'
        result = odd_or_even(arr)
        
        self.assertEqual(result, expectedResult)


if __name__ == '__main__':
    unittest.main()
import unittest
from pythonlang.sum_the_first_nth_series import series_sum

class TestFunc(unittest.TestCase):
    def test_assertation(self):

        n = 24
        expectedResult = '2.10'

        result = series_sum(n)
        
        self.assertEqual(result, expectedResult)


if __name__ == '__main__':
    unittest.main()
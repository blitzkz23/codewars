import unittest
from pythonlang.total_amount_of_points import points

class TestFunc(unittest.TestCase):
    def test_assertation(self):

        games = ['1:0','2:0','3:0','4:0','2:1','3:1','4:1','3:2','4:2','4:3']
        expectedResult = 30

        result = points(games)
        
        self.assertEqual(result, expectedResult)


if __name__ == '__main__':
    unittest.main()
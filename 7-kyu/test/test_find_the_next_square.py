import unittest
from pythonlang.find_the_next_square import find_next_square

class TestFunc(unittest.TestCase):
    def test_assertation(self):

        sq = 144
        expectedResult = 169
    
        result = find_next_square(sq)
        
        self.assertEqual(result, expectedResult)


if __name__ == '__main__':
    unittest.main()
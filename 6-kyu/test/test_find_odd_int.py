import unittest
from pythonlang.find_odd_int import find_it

class TestFunc(unittest.TestCase):
    def test_youre_square(self):

        data = [1,2,2,3,3,3,4,3,3,3,2,2,1]
        expectedResult = 4
    
        result = find_it(data)
        
        self.assertEqual(result, expectedResult)


if __name__ == '__main__':
    unittest.main()

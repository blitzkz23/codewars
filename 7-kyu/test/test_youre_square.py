import unittest
from pythonlang.youre_square import is_square

class TestFunc(unittest.TestCase):
    def test_youre_square(self):

        data = 25
        expectedResult = True
    
        result = is_square(data)
        
        self.assertEqual(result, expectedResult)


if __name__ == '__main__':
    unittest.main()

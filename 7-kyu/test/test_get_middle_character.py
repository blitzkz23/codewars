import unittest
from pythonlang.get_middle_character import get_middle

class TestFunc(unittest.TestCase):
    def test_assertation(self):

        s = 'testing'
        expectedResult = 't'
    
        result = get_middle(s)
        
        self.assertEqual(result, expectedResult)


if __name__ == '__main__':
    unittest.main()
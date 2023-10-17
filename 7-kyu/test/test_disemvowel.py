import unittest
from pythonlang.disemvowel import disemvowel

class TestFunc(unittest.TestCase):
    def test_assertation(self):

        word = 'this website'
        expectedResult = "ths wbst"
    
        result = disemvowel(word)
        
        self.assertEqual(result, expectedResult)


if __name__ == '__main__':
    unittest.main()
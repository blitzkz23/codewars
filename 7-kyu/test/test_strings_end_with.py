import unittest
from pythonlang.string_ends_with import solution

class TestFunc(unittest.TestCase):
    def test_assertation(self):

        text = 'samurai'
        ending = 'ai'
    
        expectedResult = True
        result = solution(text, ending)
        
        self.assertEqual(result, expectedResult)


if __name__ == '__main__':
    unittest.main()
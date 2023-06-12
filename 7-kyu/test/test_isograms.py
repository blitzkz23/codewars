import unittest
from pythonlang.isograms import is_isogram

class TestFunc(unittest.TestCase):
    def test_assertation(self):

        string = "isIsogram"
        expectedResult = False

        result = is_isogram(string)
        
        self.assertEqual(result, expectedResult)


if __name__ == '__main__':
    unittest.main()
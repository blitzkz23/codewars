import unittest
from pythonlang.jaden_casing_strings import to_jaden_case

class TestFunc(unittest.TestCase):
    def test_jaden_casing_strings(self):

        quote = "How can mirrors be real if our eyes aren't real"
        expectedResult = "How Can Mirrors Be Real If Our Eyes Aren't Real"
    
        result = to_jaden_case(quote)
        
        self.assertEqual(result, expectedResult)


if __name__ == '__main__':
    unittest.main()
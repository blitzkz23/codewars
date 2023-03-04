import unittest
from pythonlang.printer_error import printer_error

class TestFunc(unittest.TestCase):
    def test_assertation(self):

        s = "kkkwwwaaaaaaaaaaaaaabbbbbbbbbbbbbbbbbbmmmmmmmmmmmmmmmmmmmxyzuuuuu"
        expectedResult = "11/65"
    
        result = printer_error(s)
        
        self.assertEqual(result, expectedResult)


if __name__ == '__main__':
    unittest.main()
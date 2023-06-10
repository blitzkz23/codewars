import unittest
from pythonlang.remove_first_and_last import remove_char

class TestFunc(unittest.TestCase):
    def test_assertation(self):

        name = 'Eloquent'
        expectedResult = 'loquen'
    
        result = remove_char(name)
        
        self.assertEqual(result, expectedResult)


if __name__ == '__main__':
    unittest.main()
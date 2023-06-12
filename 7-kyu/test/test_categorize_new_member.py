import unittest
from pythonlang.categorize_new_member import open_or_senior

class TestFunc(unittest.TestCase):
    def test_open_or_senior(self):

        data = [(45, 12),(55,21),(19, -2),(104, 20)]
        expectedResult = ['Open', 'Senior', 'Open', 'Senior']
    
        result = open_or_senior(data)
        
        self.assertEqual(result, expectedResult)


if __name__ == '__main__':
    unittest.main()
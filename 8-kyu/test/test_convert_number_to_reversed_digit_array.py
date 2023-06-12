import unittest
from pythonlang.convert_number_to_reversed_digit_array import digitize


class TestFunc(unittest.TestCase):
    def test_digitize(self):
        data = 3521

        expectedResult = [1, 2, 5, 3]
        result = digitize(data)

        self.assertEqual(expectedResult, result)

if __name__ == '__main__':
    unittest.main(exit=False)
    

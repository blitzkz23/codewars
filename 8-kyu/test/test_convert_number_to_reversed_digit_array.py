import unittest
from pythonlang.convert_number_to_reversed_digit_array import digitize


class TestFunc(unittest.TestCase):
    def assertation_test(self):

        data = 3521

        expectedResult = [1, 2, 3, 5]
        result = digitize(data)

        self.assertEqual(result, expectedResult)


if __name__ == '__main__':
    unittest.main()

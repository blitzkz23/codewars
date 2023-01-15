import unittest
from pythonlang.convert_number_to_string import number_to_string


class TestFunc(unittest.TestCase):
    def assertation_test(self):

        data = 12345

        expectedResult = "12345"
        result = number_to_string(data)

        self.assertEqual(result, expectedResult)


if __name__ == '__main__':
    unittest.main()

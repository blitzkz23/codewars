import unittest
from pythonlang.convert_boolean_to_string import boolean_to_string


class TestFunc(unittest.TestCase):
    def assertation_test(self):

        data = True
        data2 = False

        expectedResult = "True"
        expectedResult2 = "False"
        result = boolean_to_string(data)
        result2 = boolean_to_string(data2)

        self.assertEqual(result, expectedResult)
        self.assertEqual(result2, expectedResult2)


if __name__ == '__main__':
    unittest.main()

import unittest
from pythonlang.count_sheep import count_sheeps


class TestCountSheep(unittest.TestCase):
    def test_array_bool(self):
        """"
        Test that it can count number of sheep present in the array
        """
        data = [True,  True,  True,  False,
                True,  True,  True,  True,
                True,  False, True,  False,
                True,  False, False, True,
                True,  True,  True,  True,
                False, False, True,  True]

        expectedResult = 17
        result = count_sheeps(data)
        self.assertEqual(result, expectedResult)


if __name__ == '__main__':
    unittest.main()

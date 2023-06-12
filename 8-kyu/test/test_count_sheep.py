import unittest
from pythonlang.count_sheep import count_sheeps


class TestFunc(unittest.TestCase):
    def test_count_sheeps(self):

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

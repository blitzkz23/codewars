import unittest
from pythonlang.a_needle_in_haystack import find_needle


class TestFunc(unittest.TestCase):
    def test_find_needle(self):

        data = ["hay", "junk", "hay", "hay",
                "moreJunk", "needle", "randomJunk"]
        expectedResult = "found the needle at position 5"
        result = find_needle(data)

        self.assertEqual(result, expectedResult)


if __name__ == '__main__':
    unittest.main()

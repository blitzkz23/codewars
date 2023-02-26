import unittest
from pythonlang.square_sum import square_sum

class TestFunc(unittest.TestCase):
    def test_square_sum(self):
        test_data = [0, 3, 4, 5]
        expected_result = 50
        result = square_sum(test_data)

        self.assertEqual(expected_result, result)

if __name__ == '__main__':
    unittest.main()
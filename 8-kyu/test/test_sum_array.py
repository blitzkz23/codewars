import unittest
from pythonlang.sum_arrays import sum_arrays

class TestFunc(unittest.TestCase):
    def test_sum_arrays(self):
        test_data = [1.1, 2.2, 3.3]
        expected_result = 6.6
        result = sum_arrays(test_data)

        self.assertEqual(expected_result, result)

if __name__ == '__main__':
    unittest.main()
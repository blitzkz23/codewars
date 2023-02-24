import unittest
from pythonlang.invert_values import invert

class TestFunc(unittest.TestCase):
    def test_count_sheep(self):
        test_data = [1,2,3,4,5]
        expected_result = [-1,-2,-3,-4,-5]
        result = invert(test_data)

        self.assertEqual(expected_result, result)



if __name__ == '__main__':
    unittest.main()
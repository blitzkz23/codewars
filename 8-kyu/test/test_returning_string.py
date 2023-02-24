import unittest
from pythonlang.returning_string import greet

class TestFunc(unittest.TestCase):
    def test_greet(self):
        test_data = 'Ryan'
        expected_result = 'Hello, Ryan how are you doing today?'
        result = greet(test_data)

        self.assertEqual(expected_result, result)

if __name__ == '__main__':
    unittest.main()
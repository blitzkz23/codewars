import unittest
from pythonlang.if_you_cant_sleep_just_count_sheep import count_sheep

class TestFunc(unittest.TestCase):
    def test_count_sheep(self):
        test_data = 3
        expected_result = '1 sheep...2 sheep...3 sheep...'
        result = count_sheep(test_data)

        self.assertEqual(expected_result, result)



if __name__ == '__main__':
    unittest.main()
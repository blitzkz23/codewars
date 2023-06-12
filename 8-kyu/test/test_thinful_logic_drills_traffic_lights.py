import unittest
from pythonlang.thinful_logic_drills_traffic_lights import update_light

class TestFunc(unittest.TestCase):
    def test_update_light(self):
        test_data = 'yellow'
        expected_result = 'red'
        result = update_light(test_data)

        self.assertEqual(expected_result, result)

if __name__ == '__main__':
    unittest.main()
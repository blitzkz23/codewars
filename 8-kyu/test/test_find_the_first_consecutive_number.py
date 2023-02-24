import unittest
from pythonlang.find_the_first_consecutive_number import first_non_consecutive

class TestFunc(unittest.TestCase):
    def test_find_non_consecutive(self):
        test_data1 = [4,5,6,7,8,9,11]
        test_data2 = [31, 32]
        
        expectedResult1 = 11
        expectedResult2 = None

        result1 = first_non_consecutive(test_data1)
        result2 = first_non_consecutive(test_data2)

        self.assertEqual(expectedResult1, result1)
        self.assertEqual(expectedResult2, result2)

if __name__ == '__main__':
    unittest.main()

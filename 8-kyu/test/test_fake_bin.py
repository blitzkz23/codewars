import unittest
from pythonlang.fake_bin import fake_bin

class TestFunc(unittest.TestCase):
    def test_assertation(self):

        input = '45385593107843568'
        expectedResult = '01011110001100111'
    
        result = fake_bin(input)
        
        self.assertEqual(result, expectedResult)


if __name__ == '__main__':
    unittest.main()
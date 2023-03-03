import unittest
from pythonlang.is_he_gonna_survive import hero

class TestFunc(unittest.TestCase):
    def test_assertation(self):

        bullets = 1500
        dragon = 751
        expectedResult = False
    
        result = hero(bullets, dragon)
        
        self.assertEqual(result, expectedResult)


if __name__ == '__main__':
    unittest.main()
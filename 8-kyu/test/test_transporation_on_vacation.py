import unittest
from pythonlang.rock_paper_scissors import rps

class TestFunc(unittest.TestCase):
    def test_assertation(self):

        p1 = 'rock'
        p2 = 'paper'
        expectedResult = 'Player 2 won!'
    
        result = rps(p1, p1)
        
        self.assertEqual(result, expectedResult)


if __name__ == '__main__':
    unittest.main()
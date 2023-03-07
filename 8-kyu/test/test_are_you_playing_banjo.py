import unittest
from pythonlang.are_you_playing_banjo import areYouPlayingBanjo

class TestFunc(unittest.TestCase):
    def test_assertation(self):

        name = 'Aldy'
        expectedResult = 'Aldy does not play banjo'
    
        result = areYouPlayingBanjo(name)
        
        self.assertEqual(result, expectedResult)


if __name__ == '__main__':
    unittest.main()
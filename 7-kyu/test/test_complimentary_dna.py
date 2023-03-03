import unittest
from pythonlang.complementary_dna import DNA_strand

class TestFunc(unittest.TestCase):
    def test_assertation(self):

        dna = 'GTGACTGTCTAAAGTG'
        expectedResult = 'CACTGACAGATTTCAC'

        result = DNA_strand(dna)
        
        self.assertEqual(result, expectedResult)


if __name__ == '__main__':
    unittest.main()
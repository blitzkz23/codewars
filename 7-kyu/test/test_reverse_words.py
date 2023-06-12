import unittest
from pythonlang.reverse_words import reverse_words

class TestFunc(unittest.TestCase):
    def test_reverse_words(self):

        data = 'The quick brown fox jumps over the lazy dog.'
        expectedResult = 'ehT kciuq nworb xof spmuj revo eht yzal .god'
    
        
        result = reverse_words(data)
        

        self.assertEqual(result, expectedResult)


if __name__ == '__main__':
    unittest.main()

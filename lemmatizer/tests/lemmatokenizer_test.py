import os
from lemmatizer.lemmatokenizer import LemmaTokenizer
import unittest
import pdb

FIXTURE_DATA_PATH = os.path.join(os.path.dirname(os.path.realpath(__file__)), "fixture-data")

class LemmaTokenizerTestCase(unittest.TestCase):

    def setUp(self):
        sample_file = open(os.path.join(FIXTURE_DATA_PATH, "sample1.txt"), 'r')
        self.sample_data = sample_file.read()
        self.lt = LemmaTokenizer()

    def test_lemma_tokenize(self):
        result = self.lt.lemma_tokenize(self.sample_data)
        print result
        self.assertEqual(result, "Some house have mice. But our house ha wolf .".split(" "))

if __name__=='__main__':
    unittest.main()

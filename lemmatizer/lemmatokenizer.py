from nltk import word_tokenize          
from nltk.stem import WordNetLemmatizer


class LemmaTokenizer(object):
    """Lemmatization uses natural language information to reduce many forms of a word."""

    def __init__(self):
        self.wnl = WordNetLemmatizer()

    def lemma_tokenize(self, doc):
        return [self.wnl.lemmatize(t) for t in word_tokenize(doc)]

from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.svm import LinearSVC
from sklearn.linear_model import LogisticRegression

from nltk.tokenize import TweetTokenizer

from nltk.stem import WordNetLemmatizer 

from nltk.corpus import stopwords

import re

class LemmaTokenizer(object):
    def __init__(self):
        self.wnl = WordNetLemmatizer()
        
    def __call__(self, doc):
        return [self.wnl.lemmatize(t) for t in self.tokenizador(self.normalizador(doc))]
    
    def tokenizador(self,x):
        tkn = TweetTokenizer()
        tokens = tkn.tokenize(x)
        return self.negador(tokens)
    
    def negador(self, tokens):
        stop = set(stopwords.words('spanish')) - set(['no'])
        new_tokens = []
        negate = False
        i = 0
        for token in tokens:
            if token in stop:
                continue
            if token in ['no', 'tampoco']:
                negate = True
                i = 0
            elif (token in ['.', ',', ';', ':', '!', '?']) or (i > 5):
                negate = False
            elif negate:
                token = 'NOT_' + token
                i += 1
            new_tokens.append(token)

        return new_tokens
    
    def normalizador(self,x):
        mentions = r'(?:@[^\s]+)'  # una arroba seguida de uno o más caracteres que no son de espaciado
        urls = r'(?:https?\://t.co/[\w]+)'  # una URL http o https. \w acepta letras, números y '_'.
        x = re.sub(mentions, '', x)
        return re.sub(urls, '', x)
        
classifiers = {
    'maxent': LogisticRegression,
    'mnb': MultinomialNB,
    'svm': LinearSVC,
}


class SentimentClassifier(object):

    def __init__(self, clf='svm'):
        """
        clf -- classifying model, one of 'svm', 'maxent', 'mnb' (default: 'svm').
        """
        self._clf = clf
        print('HOLAAAA')
        
        self._pipeline = pipeline = Pipeline([
            ('vect', CountVectorizer(binary=True, tokenizer=LemmaTokenizer())),
            ('clf', classifiers[clf]()),
        ])

    def fit(self, X, y):
        self._pipeline.fit(X, y)

    def predict(self, X):
        return self._pipeline.predict(X)

        

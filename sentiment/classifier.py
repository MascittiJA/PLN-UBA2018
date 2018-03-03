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
        self.stop = set(stopwords.words('spanish')) - set(['no'])
        
    def __call__(self, doc):
#        return [self.wnl.lemmatize(t) for t in self.tokenizador(self.normalizador(doc))]
#        return [t for t in self.tokenizador(self.normalizador(doc))]
        return [self.wnl.lemmatize(t) for t in self.tokenizador(self.normalizador(doc))]
        
    def tokenizador(self,x):
        tkn = TweetTokenizer()
        tokens = tkn.tokenize(x)
#        return tokens
        return self.negador(tokens)
    
    def negador(self, tokens):
        new_tokens = []
        negate = False
        i = 0
        for token in tokens:
            if token.lower() in self.stop:
                continue
            if token.lower() in ['no', 'tampoco', 'nunca', 'jamas']:
                negate = True
                i = 0
            elif (token in ['.', ',', ';', ':', '!', '?']) or (i > 5):
                negate = False
            elif negate:
                token = 'NOT_' + token.lower()
                i += 1
            
            new_tokens.append(token)

        return new_tokens
    
    def normalizador(self,x):
        mentions = r'(?:@[^\s]+)'  # una arroba seguida de uno o más caracteres que no son de espaciado
        urls = r'(?:https?\://t.co/[\w]+)'  # una URL http o https. \w acepta letras, números y '_'.
        x = re.sub(mentions, '', x)
        x = re.sub(urls, '', x)
        x = self.eliminar_repeticion_vocales(x)
        return x
    
    def eliminar_repeticion_vocales(self, x):
        # Si hay mayúsculas y minúsculas intercaladas no sabri
        # TODO: pasr a un for con las vocales en una lista
        a = r'(aaa+)'
        e = r'(eee+)'
        i = r'(iii+)'
        o = r'(ooo+)'
        u = r'(uuu+)'
        A = r'(AAA+)'
        E = r'(EEE+)'
        I = r'(III+)'
        O = r'(OOO+)'
        U = r'(UUU+)'
        x = re.sub(A, 'AA', x)
        x = re.sub(E, 'EE', x)
        x = re.sub(I, 'II', x)
        x = re.sub(O, 'OO', x)
        x = re.sub(U, 'UU', x)
        x = re.sub(a, 'aa', x)
        x = re.sub(e, 'ee', x)
        x = re.sub(i, 'ii', x)
        x = re.sub(o, 'oo', x)
        x = re.sub(u, 'uu', x)
        return x
        
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
        
        self._pipeline = pipeline = Pipeline([
            ('vect', CountVectorizer(binary=True, tokenizer=LemmaTokenizer())),
            ('clf', classifiers[clf]()),
        ])
        

    def fit(self, X, y):
        self._pipeline.fit(X, y)

    def predict(self, X):
        return self._pipeline.predict(X)
    
        

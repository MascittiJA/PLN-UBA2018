from math import log2
from numpy import exp2

from featureforge.vectorizer import Vectorizer
from sklearn.pipeline import Pipeline
from sklearn.naive_bayes import MultinomialNB
from sklearn.svm import LinearSVC
from sklearn.linear_model import LogisticRegression

from tagging.features import (History, word_lower, prev_tags, word_istitle, word_isupper,
                              word_isdigit, NPrevTags, PrevWord, NextWord)


classifiers = {
    'maxent': LogisticRegression,
    'mnb': MultinomialNB,
    'svm': LinearSVC,
}


class MEMM:

    def __init__(self, n, tagged_sents, clf='svm'):
        """
        n -- order of the model.
        tagged_sents -- list of sentences, each one being a list of pairs.
        clf -- classifying model, one of 'svm', 'maxent', 'mnb' (default: 'svm').
        """
        # 1. build the pipeline
        # WORK HERE!! 
        
        self.n = n
        
        
        #
        #  TENEMOS QUE AGREGAR LOS K FEATURES PARA NEXT Y PREV
        #
        
        
        histories = self.sents_histories(tagged_sents)
        n_prev_tags = NPrevTags(n)        
        features = [word_lower, prev_tags, word_istitle, word_isupper, word_isdigit, n_prev_tags]
        vect = Vectorizer(features)
        
        self._pipeline = pipeline = Pipeline([
            ('vect', vect),
            ('clf', classifiers[clf]())
        ])

        # 2. train it
        print('Training classifier...')
        X = self.sents_histories(tagged_sents)
        y = self.sents_tags(tagged_sents)
        pipeline.fit(list(X), list(y))

        # 3. build known words set
        # WORK HERE!!
        self._known_words = set()
        for sent in tagged_sents:
            for word, tag in sent:
                self._known_words.add(word)

    def sents_histories(self, tagged_sents):
        """
        Iterator over the histories of a corpus.

        tagged_sents -- the corpus (a list of sentences)
        """
        for sent in tagged_sents:
            for h in self.sent_histories(sent):
                yield h

    def sent_histories(self, tagged_sent):
        """
        Iterator over the histories of a tagged sentence.

        tagged_sent -- the tagged sentence (a list of pairs (word, tag)).
        """
        prev_tags = ('<s>',) * (self.n - 1)
        sent = [w for w, _ in tagged_sent]
        for i, (w, t) in enumerate(tagged_sent):
            yield History(sent, prev_tags, i)
            prev_tags = (prev_tags + (t,))[1:]

    def sents_tags(self, tagged_sents):
        """
        Iterator over the tags of a corpus.

        tagged_sents -- the corpus (a list of sentences)
        """
        for sent in tagged_sents:
            for t in self.sent_tags(sent):
                yield t

    def sent_tags(self, tagged_sent):
        """
        Iterator over the tags of a tagged sentence.

        tagged_sent -- the tagged sentence (a list of pairs (word, tag)).
        """
        return (t for _, t in tagged_sent)

    def tag(self, sent):
        """Tag a sentence using beam inference with beam of size 1.

        sent -- the sentence.
        """
        # WORK HERE!!
        tags = []
        prev = ('<s>', '<s>')
        for i, w in enumerate(sent):
            h = History(sent, prev, i)
            tag = self.tag_history(h)
            prev = (prev + (tag,))[1:]
            tags.append(tag)
            
        return tags

    def tag_history(self, h):
        """Tag a history.

        h -- the history.
        """
        # WORK HERE!!
        return self._pipeline.predict([h])[0]

    def unknown(self, w):
        """Check if a word is unknown for the model.

        w -- the word.
        """
        # WORK HERE!!
        return w not in self._known_words

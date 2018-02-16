from collections import defaultdict
import random


class NGramGenerator(object):

    def __init__(self, model):
        """
        model -- n-gram model.
        """
        self._n = model._n

        # compute the probabilities
        probs = defaultdict(dict)
        # WORK HERE!!
        for key in list(count.keys()):
            prev_tokens = key[:-1]
            token = key[-1:]
        #    print(prev_tokens)
        #    print(key)
        #    print(count.get(key))
        #    print(count.get(prev_tokens))
            if len(key) == n:
                probs[prev_tokens][token] = count.get(key)/count.get(prev_tokens)

        self._probs = dict(probs)

        # sort in descending order for efficient sampling
        self._sorted_probs = sorted_probs = defaultdict(list)
        # WORK HERE!!
        for key in probs.keys():

            l = list(probs.get(key).items())
            l.sort(key=lambda x: x[1], reverse=True)
        #    print(l)
            sorted_probs[key] = l

    def generate_sent(self):
        """Randomly generate a sentence."""
        n = self._n

        sent = []
        prev_tokens = ['<s>'] * (n - 1)
        token = self.generate_token(tuple(prev_tokens))
        while token != '</s>':
            # WORK HERE!!
            print('asd')

        return sent

    def generate_token(self, prev_tokens=None):
        """Randomly generate a token, given prev_tokens.

        prev_tokens -- the previous n-1 tokens (optional only if n = 1).
        """
        n = self._n
        if not prev_tokens:
            prev_tokens = ()
        assert len(prev_tokens) == n - 1

        r = random.random()
        probs = self._sorted_probs[prev_tokens]
        # WORK HERE!!

        return token

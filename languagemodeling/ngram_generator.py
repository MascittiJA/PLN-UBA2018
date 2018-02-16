from collections import defaultdict
from random import random


class NGramGenerator(object):

    def __init__(self, model):
        """
        model -- n-gram model.
        """
        self._n = n = model._n
        count = model._count

        # compute the probabilities
        probs = defaultdict(dict)
        # WORK HERE!!
        for key in list(count.keys()):
            if len(key) == n:
                prev_tokens = key[:-1]
                token = key[n-1]
                probs[prev_tokens][token] = model.cond_prob(token, prev_tokens)
                
        self._probs = dict(probs)

        # sort in descending order for efficient sampling
        self._sorted_probs = sorted_probs = defaultdict(list)
        # WORK HERE!!
        for key in probs.keys():
            l = list(probs.get(key).items())
            l.sort(key=lambda x: x[1], reverse=True)
            sorted_probs[key] = l

    def generate_sent(self):
        """Randomly generate a sentence."""
        n = self._n

        sent = []
        prev_tokens = ['<s>'] * (n - 1)
        token = self.generate_token(tuple(prev_tokens))
        while token != '</s>':
            # WORK HERE!!
            sent += list((token,))
            prev_tokens += list((token,))
            prev_tokens = prev_tokens[1:]
            token = self.generate_token(tuple(prev_tokens))

        return sent

    def sample(self,problist):
        r = random()  # entre 0 y 1
        i = 0
        word, prob = problist[0]
        acum = prob
        while r > acum:
            i += 1
            word, prob = problist[i]
            acum += prob
        
        return word

    def generate_token(self, prev_tokens=None):
        """Randomly generate a token, given prev_tokens.

        prev_tokens -- the previous n-1 tokens (optional only if n = 1).
        """
        n = self._n
        if not prev_tokens:
            prev_tokens = ()
        assert len(prev_tokens) == n - 1

        r = random()
        probs = self._sorted_probs[prev_tokens]
        # WORK HERE!!
        token = self.sample(probs)

        return token

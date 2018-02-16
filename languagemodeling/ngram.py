# https://docs.python.org/3/library/collections.html
from collections import defaultdict
import math

class LanguageModel(object):
    
    def sent_prob(self, sent):
        """Probability of a sentence. Warning: subject to underflow problems.

        sent -- the sentence as a list of tokens.
        """
        return 0.0

    def sent_log_prob(self, sent):
        """Log-probability of a sentence.

        sent -- the sentence as a list of tokens.
        """
        return -math.inf

    def log_prob(self, sents):
        result = 0.0
        for i, sent in enumerate(sents):
            lp = self.sent_log_prob(sent)
            if lp == -math.inf:
                return lp
            result += lp
        return result

    def cross_entropy(self, sents):
        log_prob = self.log_prob(sents)
        n = sum(len(sent) + 1 for sent in sents)  # count '</s>' events
        e = - log_prob / n
        return e

    def perplexity(self, sents):
        return math.pow(2.0, self.cross_entropy(sents))


class NGram(LanguageModel):

    def __init__(self, n, sents):
        """
        n -- order of the model.
        sents -- list of sentences, each one being a list of tokens.
        """
        assert n > 0
        self._n = n

        count = defaultdict(int)

        # WORK HERE!!
        for sent in sents:
            sent = self.agregarMarcadores(sent)
            final = len(sent) - n + 1
            for i in range(final):
                ngram = tuple(sent[i:i+n])  # los diccionarios no pueden guardar listas, pero sí tuplas
                count[ngram] += 1
                count[ngram[:-1]] += 1  # Todos menos el ultimo
            
            ngram = tuple(sent[final:])
#            count[ngram] += 1
            
        self._count = dict(count)

    def count(self, tokens):
        """Count for an n-gram or (n-1)-gram.

        tokens -- the n-gram or (n-1)-gram tuple.
        """
        return self._count.get(tokens, 0)

    def cond_prob(self, token, prev_tokens=None):
        """Conditional probability of a token.

        token -- the token.
        prev_tokens -- the previous n-1 tokens (optional only if n = 1).
        """
        if prev_tokens is None:
            prev_tokens = ()
        # WORK HERE!!
        if self.count(prev_tokens) == 0:
            return 0
        else:
            return self.count(prev_tokens + (token,)) / self.count(prev_tokens)
        
        
    def sent_prob(self, sent):
        """Probability of a sentence. Warning: subject to underflow problems.
        sent -- the sentence as a list of tokens.
        """
        # WORK HERE!!
        n = self._n
        sent = self.agregarMarcadores(sent)
        acum = 1
        for i in range(n - 1, len(sent)):
            acum *= self.cond_prob(sent[i], tuple(sent[i - n + 1:i]))
            
        return acum

    def sent_log_prob(self, sent):
        """Log-probability of a sentence.

        sent -- the sentence as a list of tokens.
        """
        # WORK HERE!!
        n = self._n
        acum = 0
        sent = self.agregarMarcadores(sent)
        for i in range(n - 1, len(sent)):
            cond_prob = self.cond_prob(sent[i], tuple(sent[i - n + 1:i]))
            acum += math.log2(cond_prob) if cond_prob != 0 else - math.inf
            
        return acum

    def agregarMarcadores(self,sent):
        n = self._n
        # Agregamos marcadores de comienzo y fin de oracion.
        sent = ["<s>"]*(n-1) + sent + ["</s>"]

        return sent

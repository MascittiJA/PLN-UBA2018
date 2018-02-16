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
        count_prev_tokens = self.count(prev_tokens)
        if count_prev_tokens == 0:
            return 0
        else:
            tokens = prev_tokens + (token,)
            count_tokens = self.count(tokens)
            return count_tokens / count_prev_tokens
        
        
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
    
    
class AddOneNGram(NGram):

    def __init__(self, n, sents):
        """
        n -- order of the model.
        sents -- list of sentences, each one being a list of tokens.
        """
        # call superclass to compute counts
        super().__init__(n, sents)

        # compute vocabulary
        self._voc = voc = set()
        # WORK HERE!!
        voc = self.countWordTypes(sents)

        self._V = len(voc)  # vocabulary size

    def countWordTypes(self, sents):
        word_types = ['</s>']
        for sent in sents:
            for token in sent:
                if token not in word_types:
                    word_types.append(token)

        return word_types

    def V(self):
        """Size of the vocabulary.
        """
        return self._V

    def cond_prob(self, token, prev_tokens=None):
        """Conditional probability of a token.
        token -- the token.
        prev_tokens -- the previous n-1 tokens (optional only if n = 1).
        """
        n = self._n
        if not prev_tokens:
            # if prev_tokens not given, assume 0-uple:
            prev_tokens = ()
        assert len(prev_tokens) == n - 1

        # WORK HERE!!
        count_prev_tokens = self.count(prev_tokens) + self.V()
        if count_prev_tokens == 0:
            return 0
        else:
            tokens = prev_tokens + (token,)
            count_tokens = self.count(tokens) + 1
            return count_tokens / count_prev_tokens
        
class InterpolatedNGram(NGram):

    def __init__(self, n, sents, gamma=None, addone=True):
        """
        n -- order of the model.
        sents -- list of sentences, each one being a list of tokens.
        gamma -- interpolation hyper-parameter (if not given, estimate using
            held-out data).
        addone -- whether to use addone smoothing (default: True).
        """
        assert n > 0
        self._n = n

        if gamma is not None:
            # everything is training data
            train_sents = sents
        else:
            # 90% training, 10% held-out
            m = int(0.9 * len(sents))
            train_sents = sents[:m]
            held_out_sents = sents[m:]

        print('Computing counts...')
        # WORK HERE!!
        # COMPUTE COUNTS FOR ALL K-GRAMS WITH K <= N

        # compute vocabulary size for add-one in the last step
        self._addone = addone
        if addone:
            print('Computing vocabulary...')
            self._voc = voc = set()
            # WORK HERE!!

            self._V = len(voc)

        # compute gamma if not given
        if gamma is not None:
            self._gamma = gamma
        else:
            print('Computing gamma...')
            # use grid search to choose gamma
            min_gamma, min_p = None, float('inf')

            # WORK HERE!! TRY DIFFERENT VALUES BY HAND:
            for gamma in [100 + i * 50 for i in range(10)]:
                self._gamma = gamma
                p = self.perplexity(held_out_sents)
                print('  {} -> {}'.format(gamma, p))

                if p < min_p:
                    min_gamma, min_p = gamma, p

            print('  Choose gamma = {}'.format(min_gamma))
            self._gamma = min_gamma

    def count(self, tokens):
        """Count for an k-gram for k <= n.
        tokens -- the k-gram tuple.
        """
        # WORK HERE!! (JUST A RETURN STATEMENT)

    def cond_prob(self, token, prev_tokens=None):
        """Conditional probability of a token.
        token -- the token.
        prev_tokens -- the previous n-1 tokens (optional only if n = 1).
        """
        n = self._n
        if not prev_tokens:
            # if prev_tokens not given, assume 0-uple:
            prev_tokens = ()
        assert len(prev_tokens) == n - 1

        # WORK HERE!!
        # SUGGESTED STRUCTURE:
        tokens = prev_tokens + (token,)
        prob = 0.0
        cum_lambda = 0.0  # sum of previous lambdas
        for i in range(n):
            # i-th term of the sum
            if i < n - 1:
                # COMPUTE lambdaa AND cond_ml.
                pass
            else:
                # COMPUTE lambdaa AND cond_ml.
                # LAST TERM: USE ADD ONE IF NEEDED!
                pass

            prob += lambdaa * cond_ml
            cum_lambda += lambdaa

        return prob

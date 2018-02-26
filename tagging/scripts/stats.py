"""Print corpus statistics.

Usage:
  stats.py
  stats.py -h | --help

Options:
  -h --help     Show this screen.
"""
from docopt import docopt
from collections import defaultdict
from ancora import SimpleAncoraCorpusReader


class POSStats:
    """Several statistics for a POS tagged corpus.
    """

    def __init__(self, tagged_sents):
        """
        tagged_sents -- corpus (list/iterable/generator of tagged sentences)
        """
        # WORK HERE!!
        # COLLECT REQUIRED STATISTICS INTO DICTIONARIES.
        self.words_dict = words_dict = defaultdict(int)
        self.tags_dict = tags_dict = defaultdict(int)
        
        self.tag_word_count_dict = tag_word_count_dict = defaultdict(lambda: defaultdict(int))
        self.word_tag_count_dict = word_tag_count_dict = defaultdict(lambda: defaultdict(int))

        self.word_tags_dict = word_tags_dict = word_tags_dict = defaultdict(set)
        self.tag_words_dict = tag_words_dict = defaultdict(set)
        
        self.count_sents = 0
        
        for sent in tagged_sents:
            self.count_sents += 1
            for word, tag in sent:
                # contar la palabra:
                words_dict[word] += 1 #Cuento repeticiones de palabras
                tags_dict[tag] += 1 #Cuento repeticiones de tags
                
                tag_word_count_dict[tag][word] += 1 
                word_tag_count_dict [word][tag] += 1

                word_tags_dict[word].add(tag)
                tag_words_dict[tag].add(word)
        
        self.count_words = len(words_dict)  # Cantidad de palabras (word types)
        self.count_tags = count_tags = len(tags_dict)  # Cantidad de tags

        self._token_count = sum(words_dict.values())  # Cantidad de tokens


    def sent_count(self):
        """Total number of sentences."""
        # WORK HERE!!
        return self.count_sents

    def token_count(self):
        """Total number of tokens."""
        # WORK HERE!!
        return self._token_count

    def words(self):
        """Vocabulary (set of word types)."""
        # WORK HERE!!
        return set(self.words_dict.keys())

    def word_count(self):
        """Vocabulary size."""
        # WORK HERE!!
        return self.count_words

    def word_freq(self, w):
        """Frequency of word w."""
        # WORK HERE!!
        return self.words_dict[w]

    def unambiguous_words(self):
        """List of words with only one observed POS tag."""
        # WORK HERE!!
        return self.ambiguous_words(1)

    def ambiguous_words(self, n):
        """List of words with n different observed POS tags.
        n -- number of tags.
        """
        # WORK HERE!!
#        print(list(self.word_tags_dict.items())[:5])
        n_ambiguous_words = set()
        for k, v in self.word_tags_dict.items():
#            print('Word: ', k, ' - Tags: ', v)
            if len(v) == n:
                n_ambiguous_words.add(k)
                
        return list(n_ambiguous_words)

    def tags(self):
        """POS Tagset."""
        # WORK HERE!!
        return set(self.tags_dict.keys())

    def tag_count(self):
        """POS tagset size."""
        # WORK HERE!!
        return self.count_tags

    def tag_freq(self, t):
        """Frequency of tag t."""
        # WORK HERE!!
        return self.tags_dict[t]

    def tag_word_dict(self, t):
        """Dictionary of words and their counts for tag t."""
        return dict(self.tag_word_count_dict[t])


if __name__ == '__main__':
    opts = docopt(__doc__)

    # load the data
    corpus = SimpleAncoraCorpusReader('corpus/ancora-3.0.1es/')
    sents = corpus.tagged_sents()

    # compute the statistics
    stats = POSStats(sents)

    print('Basic Statistics')
    print('================')
    print('sents: {}'.format(stats.sent_count()))
    token_count = stats.token_count()
    print('tokens: {}'.format(token_count))
    word_count = stats.word_count()
    print('words: {}'.format(word_count))
    print('tags: {}'.format(stats.tag_count()))
    print('')

    print('Most Frequent POS Tags')
    print('======================')
    tags = [(t, stats.tag_freq(t)) for t in stats.tags()]
    sorted_tags = sorted(tags, key=lambda t_f: -t_f[1])
    print('tag\tfreq\t%\ttop')
    for t, f in sorted_tags[:10]:
        words = stats.tag_word_dict(t).items()
        sorted_words = sorted(words, key=lambda w_f: -w_f[1])
        top = [w for w, _ in sorted_words[:5]]
        print('{0}\t{1}\t{2:2.2f}\t({3})'.format(t, f, f * 100 / token_count, ', '.join(top)))
    print('')

    print('Word Ambiguity Levels')
    print('=====================')
    print('n\twords\t%\ttop')
    for n in range(1, 10):
        words = list(stats.ambiguous_words(n))
        m = len(words)

        # most frequent words:
        sorted_words = sorted(words, key=lambda w: -stats.word_freq(w))
        top = sorted_words[:5]
        print('{0}\t{1}\t{2:2.2f}\t({3})'.format(n, m, m * 100 / word_count, ', '.join(top)))

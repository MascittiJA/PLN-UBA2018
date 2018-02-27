from collections import defaultdict


class BadBaselineTagger:

    def __init__(self, tagged_sents):
        """
        tagged_sents -- training sentences, each one being a list of pairs.
        """
        pass

    def tag(self, sent):
        """Tag a sentence.

        sent -- the sentence.
        """
        return [self.tag_word(w) for w in sent]

    def tag_word(self, w):
        """Tag a word.

        w -- the word.
        """
        return 'nc0s000'

    def unknown(self, w):
        """Check if a word is unknown for the model.

        w -- the word.
        """
        return True

def inner_default_dict():
    return defaultdict(int)

class BaselineTagger:

    def __init__(self, tagged_sents, default_tag='nc0s000'):
        """
        tagged_sents -- training sentences, each one being a list of pairs.
        default_tag -- tag for unknown words.
        """
        # WORK HERE!!
        self.default_tag = default_tag
        
        self.word_tag_count_dict = word_tag_count_dict = defaultdict(inner_default_dict)
        
        for sent in tagged_sents:
            for word, tag in sent:
                word_tag_count_dict [word][tag] += 1
        
        self.word_mostFrecTag_dict = word_mostFrecTag_dict = defaultdict(str)
        for word, tags in word_tag_count_dict.items():
            tag = max(tags.items(), key=lambda x: x[1])[0]
            word_mostFrecTag_dict[word] = tag
        

    def tag(self, sent):
        """Tag a sentence.
        sent -- the sentence.
        """
        return [self.tag_word(w) for w in sent]

    def tag_word(self, w):
        """Tag a word.
        w -- the word.
        """
        # WORK HERE!!
        if self.unknown(w):
            return self.default_tag
        else:
            return self.word_mostFrecTag_dict[w]

    def unknown(self, w):
        """Check if a word is unknown for the model.
        w -- the word.
        """
        # WORK HERE!!
        return w not in self.word_tag_count_dict

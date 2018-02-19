"""Train an n-gram model.

Usage:
  train.py [-m <model>] -n <n> -o <file>
  train.py -h | --help

Options:
  -n <n>        Order of the model.
  -m <model>    Model to use [default: ngram]:
                  ngram: Unsmoothed n-grams.
                  addone: N-grams with add-one smoothing.
                  inter: N-grams with interpolation smoothing.
  -o <file>     Output model file.
  -h --help     Show this screen.
"""
from docopt import docopt
import pickle

from nltk.corpus import gutenberg

#from languagemodeling.ngram import NGram
from languagemodeling.ngram import NGram, AddOneNGram, InterpolatedNGram


models = {
     'ngram': NGram,
     'addone': AddOneNGram,
     'inter': InterpolatedNGram,
}


if __name__ == '__main__':
    opts = docopt(__doc__)
    
    # load the data
    # WORK HERE!! LOAD YOUR TRAINING CORPUS
    import nltk
    nltk.download('machado')
    from nltk.corpus import machado
    
    sents = machado.sents()
    # 90% training, 10% test
    m = int(0.9 * len(sents))
    train_sents = sents[:m]
    test_sents = list(sents[m:])
    
    # save the test sents
    test_filename = "test.txt"
    # with open(test_filename, "wb") as test_file:
    test_file = open(test_filename, "wb")
    pickle.dump(test_sents, test_file)
    test_file.close()

    # train the model
    n = int(opts['-n'])
    #model = NGram(n, train_sents)
    model_class = models[opts['-m']]
    model = model_class(n, train_sents)

    # save it
    filename = opts['-o']
    f = open(filename, 'wb')
    pickle.dump(model, f)
    f.close()

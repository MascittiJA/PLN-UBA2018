"""Print corpus statistics.

Usage:
  stats.py
  stats.py -h | --help

Options:
  -h --help     Show this screen.
"""
from docopt import docopt
from collections import defaultdict
from sentiment.tass import InterTASSReader
from sentiment.tass import GeneralTASSReader


class SentimentsStats:

    def __init__(self, reader):
        
        self._class = reader.__class__.__name__
        
        self._pol_tweet_dict = pol_tweet_dict = defaultdict(int)
        
        for pol in reader.y():
            pol_tweet_dict[pol] += 1
            
        self._tweet_count = sum(pol_tweet_dict.values())  # Cantidad de tweets

    def tweet_count(self):
        return self._tweet_count
    
    def polarity_dict(self):
        return self._pol_tweet_dict
    
    def print_stats(self):
        print('Basic Statistics ', self._class)
        print('================================')
        print('Tweets: {}'.format(self.tweet_count()))
        print('Sentiment P: {}'.format(self.polarity_dict()['P']))
        print('Sentiment N: {}'.format(self.polarity_dict()['N']))
        print('Sentiment NEU: {}'.format(self.polarity_dict()['NEU']))
        print('Sentiment NONE: {}'.format(self.polarity_dict()['NONE']))
        print('')




if __name__ == '__main__':
    opts = docopt(__doc__)
 
    # load the data
    reader = InterTASSReader('TASS/InterTASS/tw_faces4tassTrain1000rc.xml')
    # compute the statistics
    stats = SentimentsStats(reader)
    
    stats.print_stats()

    reader = GeneralTASSReader('TASS/GeneralTASS/general-tweets-train-tagged.xml')
    # compute the statistics
    stats = SentimentsStats(reader)

    stats.print_stats()

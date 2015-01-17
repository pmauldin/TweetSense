'''.............................
   Creation 2015 by WafflesAtOne
   .............................'''

import Scorer
import Interpolator
#import json

#def analyze(query_phrase, tweets_and_times, target_times):
def analyze(timed_tweets, target_times):
        ''' e.g. ('motors',
                  [('go general motors!', -6.2), ...],
                  [-8.0, -7.9, ..., 0.9, 1.0])   
            where time is measured in days from now'''
        timed_scores = [(time, Scorer.positivity(tweet))
                         for (time, tweet) in timed_tweets]
        return [(t, Interpolator.predict(timed_scores, t))
                for t in target_times]
        

##test:
'''
print(analyze([
               (-7.0, 'death and despair and neglectful abandonment'),
               (-5.0, 'mediocre mustard'),
               (-3.0, 'i am a fan of rainbows'),
               (-1.0, 'yahoo! i love you, most beautiful and happy one!'),
               (1.0, 'very very very very delectable incredibly absorbing frolic')],
        [-2.0, -1.0, 0.0, 1.0, 3.0]))
'''

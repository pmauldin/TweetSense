'''.............................
   Creation 2015 by WafflesAtOne
   .............................'''

import Scorer
import Interpolator
#import json

#def analyze(query_phrase, tweets_and_times, target_times):
def analyze(tweets_and_times, target_times):
        ''' e.g. ('motors',
                  [('go general motors!', -6.2), ...],
                  [-8.0, -7.9, ..., 0.9, 1.0])   
            where time is measured in days from now'''
        scores_and_times = [(Scorer.positivity(tweet), time)
                            for (tweet, time) in tweets_and_times]
        return [(t, Interpolator.interpolate(scores_and_times, t))
                for t in target_times]
        

'''
print(analyze([('i am a fan of rainbows', -7.0),
         ('death and despair and neglectful abandonment', -5.0),
         ('yahoo! i love you, most beautiful and happy one!', -3.0)],
        [-2.0, -1.0, 0.0, 1.0]))
'''

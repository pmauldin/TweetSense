'''.............................
   Creation 2015 by WafflesAtOne
   .............................'''

from Sampy import invert
from math import *

def closeness(x, query, tau):
      return exp(-(x-query)**2/(2*tau))
   
def predict(datapoints, target_time, tau=2.0):
   '''e.g. if datapoints==[(0.0, 1.0), (2.0, 2.0), (4.0, 3.0), (6.0, 4.0)]
               and query==1.2, then should return (1.2, 1.6);
      tau controls duration of context:
      if tau is small, it'll guess based on closest datapoints (nearest neighbor), at risk of overfitting;
      if tau is large, it'll take into account the whole history (unweighted regression), at risk of oversimplifying.'''
   ## get at least 5 neighbors:
   if len(datapoints)<5:
      print('need at least 5 datapoints!'); return
   neighbors = None
   while True:
      max_distance = sqrt(tau)*5
      neighbors = [(t, y) for (t, y) in datapoints if abs(t-target_time)<max_distance]
      if len(neighbors) < 5:
         tau *= 1.1
      else:
         break
   
   ## locally linear regress:
   ins = [[1, t] for (t, y) in neighbors]
   kernel = lambda t: closeness(t, target_time, tau)
   kappa = [kernel(t) for (t, y) in neighbors]
   sni_kappa_ins = [  [sum(ins[k][i]*kappa[k]*ins[k][j]
                           for k in range(len(kappa)))
                       for j in range(2)]
					for i in range(2)]
   pseudo_inverse = invert(sni_kappa_ins)
   
   outs = [y for (t, y) in neighbors]
   sni_kappa_outs = [sum(ins[k][i]*kappa[k]*outs[k]
                         for k in range(len(neighbors)))
                     for i in range(2)]
   
   weights = [sum(pseudo_inverse[i][k]*sni_kappa_outs[k]
                  for k in range(2))
              for i in range(2)]
   return sum(weights[k]*[1, target_time][k]
                  for k in range(2))   



'''
datapoints = [(0.0, 1.0),
              (1.0, 2.0),
              (2.0, 3.0),
              (3.0, 3.0),
              (4.0, 4.0),
              (5.0, 2.0),
              (6.0, 1.0)]
for x in range(0, 70):
   print(predict(datapoints, float(x)/10))
while True:
   print(predict(datapoints, float(input()))
'''

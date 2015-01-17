'''.............................
   Creation 2015 by WafflesAtOne
   .............................'''

from numpy.linalg import *
from numpy import *
from math import *

def closeness(x, query, tau): ## tau==0 => nearest neighbor; 
      return exp(-(x-query)**2/(2*tau)) ## tau==infinity => unweighted regression
   
def predict(datapoints, target_time, tau=2.0):
   '''e.g. if datapoints==[(0.0, 1.0), (2.0, 2.0), (4.0, 3.0), (6.0, 4.0)]
               and query==1.2, then should return (1.2, 1.6);
      tau controls duration of context; if tau is small, it'll guess based
      on closest datapoints, at risk of overfitting; if tau is large, it'll
      take into account the whole history, at risk of oversimplifying.'''
   neighbors = None
   while True:
      max_distance = sqrt(tau)*5
      neighbors = [(t, y) for (t, y) in datapoints if abs(t-target_time)<max_distance]
      if len(neighbors) < 5:
         tau *= 1.1
      else:
         break
   
   phi = array([[1, t] for (t, y) in neighbors])
   ys = array([[y] for (t, y) in neighbors])
   N = len(neighbors)
   kernel = lambda t: closeness(t, target_time, tau)
   kappa = array(  [  [kernel(neighbors[i][0]) if i==j else 0.0
                       for j in range(N)]
                    for i in range(N)])
   phi_t = transpose(phi)

   weights = dot(dot(dot(inv(dot(dot(phi_t,kappa),phi)),  phi_t), kappa), ys)
   return dot(transpose(weights), array([[1], [target_time]]))[0][0]

def interpolate_frequency(times, target_time, tau=1.0):
   kernel = lambda t: closeness(t, target_time, tau)/sqrt(2*pi*tau) ## normalized
   return sum(kernel(t) for t in times)

def extrapolate_frequency(times, target_time, tau=1.0):
   begin = min(times); end = max(times)
   duration = end-begin
   begin += 0.1*duration; end -= 0.1*duration ## shrink from edges, since edge smoothfrequencies
                                              ## will be cut off and hence inaccurately small
   grid = [begin + (end-begin)*1.0*i/len(times) for i in range(len(times)+1)] ## [begin, ..., end]
   frequencies = [(t, log(interpolate_frequency(times, t))) for t in grid]
   return exp(predict(frequencies, target_time, tau=tau))


times = [-2.0,
         -1.0,
         0.0,
         1.0, 1.1, 1.2, 1.3, 1.4,
         1.48, 1.49, 1.5, 1.51, 1.52,
         1.6, 1.7, 1.8, 1.9, 1.9, 2.0,
         3.0,
         4.0,
         5.0,
         6.0,
         7.0,
         8.0,
         10.0,
         14.0,
         22.0,
         26.0,
         28.0,
         29.0,
         29.5,
         29.75]
# for x in range(-50, 350):
   # print(extrapolate_frequency(times, float(x)/10, tau=0.25))


'''
## testing:
datapoints = [(0.0, 1.0),
              (1.0, 2.0),
              (2.0, 3.0),
              (3.0, 3.0),
              (4.0, 4.0),
              (5.0, 2.0),
              (6.0, 1.0)]
for x in range(0, 70):
   print(interpolate(datapoints, float(x)/10))
while True:
   print(interpolate(datapoints, float(input())))
'''

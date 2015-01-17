from numpy.linalg import *
from numpy import *
from math import *

def interpolate(datapoints, query):
   '''e.g. if datapoints==[(0.0, 1.0), (2.0, 2.0), (4.0, 3.0), (6.0, 4.0)]
               and query==1.2, then should return (1.2, 1.6)'''
   phi = array([[1, x] for (x, y) in datapoints])
   t = array([[y] for (x, y) in datapoints])
   def closeness(x, tau=1.0): ## tau==0 => nearest neighbor; 
      return exp(-(x-query)**2/(2*tau))## tau==infinity => unweighted regression
   N = len(datapoints)
   kappa = array(  [  [closeness(datapoints[i][0]) if i==j else 0.0
                       for j in range(N)]
                    for i in range(N)])
   phi_t = transpose(phi)

   weights = dot(dot(dot(inv(dot(dot(phi_t,kappa),phi)),  phi_t), kappa), t)
   #print(weights)
   return dot(transpose(weights), array([[1], [query]]))[0][0]


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


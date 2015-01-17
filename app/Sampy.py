'''.............................
   Creation 2015 by WafflesAtOne
   .............................'''

def determinant(M):
   return M[0][0]*M[1][1] - \
          M[0][1]*M[1][0]

def invert(M):
   '''e.g. invert([[1, 0], [0, 2]]) == [[1.0, 0.0], [0.0, 0.5]]'''
   det = float(determinant(M))
   return [[ M[1][1]/det,-M[0][1]/det],
           [-M[1][0]/det, M[0][0]/det]]



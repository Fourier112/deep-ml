import numpy as np

def matrixmul(a:list[list[int|float]],
              b:list[list[int|float]])-> list[list[int|float]]:
              mat1 = np.array(a)
              mat2 = np.array(b)
              if mat1.shape[1] == mat2.shape[0]:
                return np.dot(mat1, mat2)
              else:
                return -1
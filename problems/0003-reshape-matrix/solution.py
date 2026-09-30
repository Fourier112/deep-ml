import numpy as np
import math

def reshape_matrix(a: list[list[int|float]], new_shape: tuple[int, int]) -> list[list[int|float]]:
	#Write your code here and return a python list after reshaping by using numpy's tolist() method
	x = np.array(a)
	if x.size == math.prod(new_shape):
		return x.reshape(new_shape).tolist()
	else:
		return []
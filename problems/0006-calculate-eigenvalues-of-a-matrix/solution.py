import numpy as np

def calculate_eigenvalues(matrix: list[list[float|int]]) -> list[float]:
	x = np.array(matrix)
	
	#The trace and determinant of the (2×2) matrix are calculated.
	trace = x[0, 0] + x[1, 1]
	det = (x[0, 0] * x[1, 1]) - (x[0, 1] * x[1, 0])

	#The discriminant of the characteristic equation is calculated.
	disc = (trace ** 2) - (4 * det)

	if disc >= 0:
		r1, r2 = (trace + np.sqrt(disc)) / 2, (trace - np.sqrt(disc)) / 2
	else:
		return -1

	if r1 < r2:
		return [r2, r1]
	else:
		return [r1, r2]

	
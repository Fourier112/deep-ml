import numpy as np

def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:
	x = np.array(matrix)
	if mode == 'row':
		return x.mean(axis=1)
	elif mode == 'column':
		return x.mean(axis=0)
	else:
		return 'Invalid mode.'
	
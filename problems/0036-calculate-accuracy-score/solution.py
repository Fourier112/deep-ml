import numpy as np

def accuracy_score(y_true, y_pred):
	tally = 0
	for a, b in zip(y_true, y_pred):
		if a == b:
			tally += 1
	return tally / y_true.size
			
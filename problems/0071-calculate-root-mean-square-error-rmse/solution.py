
import numpy as np

def rmse(y_true, y_pred):
	sq_errors = (y_true - y_pred) ** 2
	mse = np.sum(sq_errors) / y_true.size
	rmse_res = np.sqrt(mse)
	return round(rmse_res,3)

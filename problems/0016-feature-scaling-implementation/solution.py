import numpy as np
from sklearn.preprocessing import StandardScaler, MinMaxScaler

def feature_scaling(data: np.ndarray) -> (np.ndarray, np.ndarray):
	std_scaler = StandardScaler()
	min_max_scaler = MinMaxScaler()
	standardized_data = std_scaler.fit_transform(data)
	normalized_data = min_max_scaler.fit_transform(data)
	return standardized_data, normalized_data
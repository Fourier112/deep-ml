import numpy as np

def min_max(x: list[float]) -> list[float]:
    """
    Perform Min-Max normalization to scale values to [0, 1].
    
    Args:
        x: A list of numerical values
    
    Returns:
        A new list with values normalized to [0, 1]
    """
    arr = np.array(x)
    arr_min = arr.min()
    arr_max = arr.max()
    return ((arr - arr_min) / (arr_max - arr_min)).tolist()
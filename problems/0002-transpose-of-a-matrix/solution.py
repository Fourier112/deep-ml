import numpy as np
def transpose_matrix(a: list[list[int|float]]) -> list[list[int|float]]:
    """
    Transpose a 2D matrix by swapping rows and columns.
    
    Args:
        a: A 2D matrixing of shape (m, n)
    
    Returns:
        The transposed matrix of shape (n, m)
    """
    x = np.array(a)
    return x.T
    
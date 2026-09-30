import numpy as np

def inverse_2x2(matrix: list[list[float]]) -> list[list[float]] | None:
    """
    Calculate the inverse of a 2x2 matrix.
    
    Args:
        matrix: A 2x2 matrix represented as [[a, b], [c, d]]
    
    Returns:
        The inverse matrix as a 2x2 list, or None if the matrix is singular
        (i.e., determinant equals zero)
    """
    mat = np.array(matrix)
    mat_copy = mat.copy().tolist()
    determinant = (mat[0, 0] * mat[1, 1]) - (mat[0, 1] * mat[1, 0])

    if determinant == 0:
        return None
    else:
        mat_copy[0][0] = mat[1, 1]
        mat_copy[0][1] = -1 * mat[0, 1]
        mat_copy[1][0] = -1 * mat[1, 0]
        mat_copy[1][1] = mat[0, 0]

        x = np.array(mat_copy)
        return (1 / determinant) * x
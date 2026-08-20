import numpy as np

def matrix_transpose(A: list) -> np.ndarray:
    """
    Return the transpose of matrix A (swap rows and columns).
    """
    A = np.asarray(A)
    rows,col = A.shape
    result = np.empty((col,rows),dtype=A.dtype)

    for i in range(rows):
        for j in range(col):
            result[j,i]=A[i,j]

    return result
            
     

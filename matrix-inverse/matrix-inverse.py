import numpy as np

def matrix_inverse(A: list) -> np.ndarray | None:
    """
    Returns the inverse as a NumPy array, or None.
    """
    A=np.asarray(A)
    
    try:
        return np.linalg.inv(A)
    except np.linalg.LinAlgError:
        return None
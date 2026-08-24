import numpy as np

def covariance_matrix(X: list) -> np.ndarray:
    """
    Returns the covariance matrix as a NumPy array.
    """
    X=np.asarray(X)
    return np.atleast_2d(np.cov(X,rowvar=False))
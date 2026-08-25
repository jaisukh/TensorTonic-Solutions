import numpy as np

def pearson_correlation(X: list) -> np.ndarray:
    """
    Returns the correlation matrix as a NumPy array.
    """
    X=np.asarray(X)
    covariance=np.cov(X,rowvar=False)
    std=np.std(X,axis=0,ddof=1)

    denominator=np.outer(std,std)

    return np.divide(
        covariance,
        denominator,
        out=np.full_like(covariance,np.nan),
        where=denominator != 0
    )
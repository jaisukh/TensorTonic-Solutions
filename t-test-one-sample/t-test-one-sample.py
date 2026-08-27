import numpy as np

def t_test_one_sample(x: list, mu0: float) -> float:
    """
    Returns the t-statistic as a float.
    """
    x=np.asarray(x)
    mean=np.mean(x)
    s=np.std(x,ddof=1)
    n=len(x)
    return float((mean-mu0)/(s/np.sqrt(n)))
    
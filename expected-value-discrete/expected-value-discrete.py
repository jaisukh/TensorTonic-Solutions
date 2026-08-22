import numpy as np

def expected_value_discrete(x: list, p: list) -> float:
    """
    Return the expected value of the discrete distribution.
    """
    x=np.asarray(x)
    p=np.asarray(p)
    return float(np.sum(x*p))
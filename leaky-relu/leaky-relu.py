import numpy as np

def leaky_relu(x, alpha=0.01):
    """
    Vectorized Leaky ReLU implementation.
    """
    x=np.asarray(x,dtype=np.float64)
    return np.maximum(alpha*x,x)
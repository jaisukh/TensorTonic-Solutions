import numpy as np
from collections import Counter

def mean_median_mode(x):
    """
    Compute mean, median, and mode.
    """
    x=np.asarray(x)
    mean=float(np.mean(x))
    median=float(np.median(x))
    values,counts=np.unique(x,return_counts=True)
    max_count=counts.max()
    mode=float(values[counts==max_count].min())
    
    return (mean,median,mode)
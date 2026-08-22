import numpy as np

def sample_var_std(x: list) -> dict:
    """Return unbiased sample variance and standard deviation."""
    x=np.asarray(x)
    mean=np.mean(x)
    var=np.sum((x-mean)**2)/(len(x)-1)
    s_d=np.sqrt(var)

    return {
        "variance":float(var),
        "standard_deviation":float(s_d)
    }
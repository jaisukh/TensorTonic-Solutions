import numpy as np

def bernoulli_pmf_and_moments(x: list, p: float) -> dict:
    """Return the Bernoulli PMF, mean, and variance."""
    x=np.asarray(x)

    pmf=p**x*(1-p)**(1-x)
    var=p*(1-p)
    return{
        "pmf":pmf,
        "mean":float(p),
        "variance":float(var)
    }

    
import numpy as np

def pair_metric(rates, natural_rates):
    metric = -np.sum(rates.rates*(natural_rates.rates+1e-8))
    return metric

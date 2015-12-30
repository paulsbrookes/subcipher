import numpy as np

def pair_metric_generator(natural_text):
    def pair_metric(ciphertext):
        ciphertext.pair_frequencies()
        difference = abs(natural_text.rates[0] - ciphertext.rates[0])
        difference = np.absolute(difference) + 1e-6
        metric = -np.sum(1/difference)
        return metric
    return pair_metric

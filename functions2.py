import numpy as np
from key import Key
import itertools

default_alpha = 'abcdefghijklmnopqrstuvwxyz '

def pair_metric(ciphertext, natural_text):
    ciphertext.pair_frequencies()
    difference = abs(natural_text.rates[0] - ciphertext.rates[0])
    difference = np.absolute(difference) + 1e-6
    metric = -np.sum(1/difference)
    return metric

def pair_metric2(ciphertext, natural_text):
    ciphertext.pair_frequencies2()
    metric = 0
    for i in range(ciphertext.rates[1].shape[0]):
        metric += 1/(natural_text.rates[0][ciphertext.rates[1][i,0],ciphertext.rates[1][i,1]]+1e-6)
    return metric

def pair_metric_generator(natural_text):
    def pair_metric(ciphertext):
        ciphertext.pair_frequencies()
        difference = abs(natural_text.rates[0] - ciphertext.rates[0])
        difference = np.absolute(difference) + 1e-6
        metric = -np.sum(1/difference)
        return metric
    return pair_metric


def remove_duplicates(values):
    map_list = [x.map_record for x in values]
    list_form.sort()
    filtered_list = list(list_form for list_form,_ in itertools.groupby(list_form))
    filtered_arrays = [np.array(x) for x in filtered_list]
    return filtered_arrays

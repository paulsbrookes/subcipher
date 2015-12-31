from functions2 import rm_duplicate_arrays
import numpy as np

class Map(object):
    def __init__(self, map=None):
        self.map = map

    def invert(self):
        inverted_map = np.zeros(self.map.size)
        for x in range(self.map.size):
            inverted_map[self.map[x]] = x
        self.map = inverted_map

    def proliferate(self, proliferation_functions):
        new_maps = [self.map]
        for function in proliferation_functions:
            new_maps += function(self.map)
        new_maps = rm_duplicate_arrays(new_maps)
        return new_maps

    def freq_key(self, ciphertext, natural_sample):
        if np.all(ciphertext.rates[0] == None):
            ciphertext.group_frequencies(1)
        if np.all(natural_sample.rates[0] == None):
            natural_sample.group_frequencies(1)
        ciphertext_ranking = np.argsort(ciphertext.rates[0])
        natural_ranking = np.argsort(natural_sample.rates[0])
        self.map = np.zeros(len(ciphertext.rates[0]), dtype=np.int32)
        for i, x in enumerate(ciphertext_ranking):
            self.map[x] = natural_ranking[i]

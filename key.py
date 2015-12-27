import numpy as np
import random
default_alpha = 'abcdefghijklmnopqrstuvwxyz '

class Key(object):
    def __init__(self, map=[]):
        self.map = map

    def substitute(self, new_map):
        map_out = np.zeros(self.map.shape[0])
        for x in range(self.map.shape[0]):
            map_out[x] = new_map[self.map[x]]
        return Key(map_out)

    def invert(self):
        inverted_map = np.zeros(self.map.shape[0], dtype = np.int8)
        for x in range(self.map.size):
            inverted_map[self.map[x]] = x
        return Key(inverted_map)

    def obtain_key(self, alpha, beta):
        key = np.zeros(len(beta))
        for x in range(len(beta)):
            key[x] = alpha.find(beta[x])
        return Key(key)

    def random_key(self, alpha = default_alpha):
        self.map = np.array(range(len(alpha)))
        random.shuffle(self.map)

    def frequency_key(self, natural_frequencies, observed_frequencies):
        natural_indices_sorted = np.argsort(natural_frequencies)
        observed_indices_sorted = np.argsort(observed_frequencies)
        frequency_key = np.zeros(natural_frequencies.size, dtype = np.int8)
        for i, x in natural_indices_sorted:
            frequency_key[x] = observed_indices_sorted[i]
        self.map = frequency_key

import numpy as np
import random
default_alpha = 'abcdefghijklmnopqrstuvwxyz '

class Key(object):
    def __init__(self, map=[]):
        self.map = map

    def substitute(self, new_map):
        map_out = np.zeros(self.map.shape[0], dtype = np.int8)
        for x in range(self.map.shape[0]):
            map_out[x] = new_map.map[self.map[x]]
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
        for i, x in enumerate(natural_indices_sorted):
            frequency_key[x] = observed_indices_sorted[i]
        self.map = frequency_key

    def dictionary(self, alpha = default_alpha):
        letter_map = np.zeros([2, len(alpha)], dtype = '|S1')
        for i, x in enumerate(alpha):
            letter_map[0, i] = x
            letter_map[1, i] = alpha[self.map[i]]
        return letter_map

    def swap(self, i):
        swap_map = np.copy(self.map)
        if i == swap_map.size - 1:
            swap_map[i], swap_map[0] = self.map[0], self.map[i]
        elif i not in range(swap_map.size):
            pass
        else:
            swap_map[i], swap_map[i + 1] = self.map[i + 1], self.map[i]
        return Key(swap_map)

    def array_swap3(self):
        return [self.swap3(i) for i in range(self.map.size)]

    def array_swap(self):
        return [self.swap(i) for i in range(self.map.size)]

    def swap2(self, i):
        swap_map = np.copy(self.map)
        if i == swap_map.size - 1:
            swap_map[i], swap_map[0] = self.map[0], self.map[i]
        else:
            swap_map[i], swap_map[i + 1] = self.map[i + 1], self.map[i]
        return swap_map

    def array_swap2(self):
        return [self.swap2(i) for i in range(self.map.size)]

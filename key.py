import numpy as np
import random

class Key(object):
    def __init__(self, map=[]):
        self.map = map

    def substitute(self, new_map):
        map_out = np.zeros(self.map.shape[0])
        for x in range(self.map.shape[0]):
            map_out[x] = new_map[self.map[x]]
        return Key(map_out)

    def invert(self):
        inverted_map = np.zeros(self.map.shape[0])
        for x in range(self.map.shape[0]):
            inverted_map[self.map[x]] = x
        return Key(inverted_map)

    def obtain_key(self, alpha, beta):
        key = np.zeros(len(beta))
        for x in range(len(beta)):
            key[x] = alpha.find(beta[x])
        return Key(key)

    def random_key(self, alpha):
        self.map = np.array(range(len(alpha)))
        random.shuffle(self.map)

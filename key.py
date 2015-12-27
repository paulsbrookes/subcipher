import numpy as np
import random

class Key(object):
    def __init__(self, key=[]):
        self.key = key

    def substitute(self, mapping):
        new_key = np.zeros(self.key.shape[0])
        for x in range(self.key.shape[0]):
            new_key[x] = mapping[self.key[x]]
        return new_key

    def invert(self):
        inverted_key = np.zeros(self.key.shape[0])
        for x in range(self.key.shape[0]):
            inverted_key[self.key[x]] = x
        return inverted_key

    def obtain_key(self, alpha, beta):
        key = np.zeros(len(beta))
        for x in range(len(beta)):
            key[x] = alpha.find(beta[x])
        return key

    def random_key(self, alpha):
        self.key = np.array(range(len(alpha)))
        random.shuffle(self.key)

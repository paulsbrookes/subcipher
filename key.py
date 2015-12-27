import numpy as np

class Key(object):
    def __init__(self,key):
        Key.key = key

    def substitute(self,mapping):
        new_key = np.zeros(Key.key.shape[0])
        for x in range(Key.key.shape[0]):
            new_key[x] = mapping[Key.key[x]]
        return new_key

    def invert(self):
        inverted_key = np.zeros(Key.key.shape[0])
        for x in range(Key.key.shape[0]):
            inverted_key[Key.key[x]] = x
        return inverted_key

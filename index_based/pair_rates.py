import numpy as np
from ciphertext import Ciphertext
def_alpha = ' etaoinshrdlcumwfgypbvkjxqz'

class Pair_Rates(object):
    def __init__(self, rates=None, alpha=def_alpha, map_record=None):
        self.rates = rates
        self.alpha = alpha
        self.map_record = map_record

    def text_in(self, text, alpha=def_alpha):
        ciphertext = Ciphertext()
        ciphertext.text_in(text, alpha)
        ciphertext.pair_frequencies()
        self.rates = ciphertext.rates[1]
        self.alpha = alpha
        self.map_record = np.arange(len(self.alpha))

    def map(self, new_map):
        new_map_record = np.dot(new_map,self.map_record)
        new_rates = np.dot(new_map,np.dot(self.rates,np.transpose(new_map)))
        return Pair_Rates(new_rates, new_map_record)

    def substitute(self, new_map):
        self.map_record = np.dot(new_map,self.map_record)
        self.rates = np.dot(new_map,np.dot(self.rates,np.transpose(new_map)))

import numpy as np
from functions import remove_duplicates
from key import Key
import time

class Key_Group(object):
    def __init__(self, keys, cipher_text, natural_sample):
        self.keys = keys
        self.cipher_text = cipher_text
        self.natural_sample = natural_sample

    def advance(self, proliferation_functions, metric_function, number_retained=10):
        metric_results = []
        new_keys = []
        if number_retained > len(self.keys):
            number_retained = len(self.keys)
        for function in proliferation_functions:
            new_keys += function(self.keys[0:number_retained])
        new_maps = [key.map for key in new_keys]
        new_maps_filtered = remove_duplicates(new_maps)
        new_keys_filtered = [Key(map) for map in new_maps_filtered]
        for key in new_keys_filtered:
            decryption_attempt = self.cipher_text.map(key)
            metric = metric_function(decryption_attempt, self.natural_sample)
            metric_results.append(metric)
        ranking = np.argsort(metric_results)
        best_keys = [new_keys_filtered[x] for x in ranking]
        self.keys = best_keys

    def proliferate(self, proliferation_functions, number_carried=10):
        new_keys = []
        for function in proliferation_functions:
            new_keys += function(self.keys[0:number_carried])
        new_maps = [key.map for key in new_keys]
        new_maps_filtered = remove_duplicates(new_maps)
        new_keys_filtered = [Key(map) for map in new_maps_filtered]
        self.keys = new_keys_filtered

    def rank(self, metric_function):
        metric_results = np.zeros(len(self.keys))
        for i, key in enumerate(self.keys):
            decryption_attempt = self.cipher_text.map(key)
            metric = metric_function(decryption_attempt, self.natural_sample)
            metric_results[i] = metric
        ranking = np.argsort(metric_results)
        ranked_keys = [self.keys[x] for x in ranking]
        self.keys = ranked_keys

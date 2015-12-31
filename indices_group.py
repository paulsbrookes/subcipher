import numpy as np
from functions2 import rm_duplicate_ciphertexts
from functions2 import rm_duplicate_ciphertexts3

class Indices_Group(object):
    def __init__(self, ciphertexts, natural_text):
        self.ciphertexts = ciphertexts
        self.natural_text = natural_text

    def proliferate(self, proliferation_maps, number_carried=10):
        new_ciphertexts = []
        for ciphertext in self.ciphertexts[0:number_carried]:
            new_ciphertexts += [ciphertext.map(map) for map in proliferation_maps]
        self.ciphertexts = new_ciphertexts

    def rank(self, metric_function, number_retained=10):
        metric_results = np.zeros(len(self.ciphertexts))
        for i, text in enumerate(self.ciphertexts):
            metric = metric_function(text, self.natural_text)
            metric_results[i] = metric
        ranking = np.argsort(metric_results)
        ranked_texts = [self.ciphertexts[x] for x in ranking]
        filtered_ranked_texts = rm_duplicate_ciphertexts3(ranked_texts, number_retained)
        self.ciphertexts = filtered_ranked_texts

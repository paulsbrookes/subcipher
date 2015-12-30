import numpy as np

class Indices_Group(object):
    def __init__(self, ciphertexts, natural_text):
        self.ciphertexts = ciphertexts
        self.natural_text = natural_text

    def proliferate(self, proliferation_maps, number_carried = 10):
        new_ciphertexts = []
        for ciphertext in self.ciphertexts[0:number_carried]:
            new_ciphertexts += [ciphertext.map(map) for map in proliferation_maps]
        self.ciphertexts = new_ciphertexts

    def rank(self, metric_function):
        metric_results = np.zeros(len(self.ciphertexts))
        for i, text in enumerate(self.ciphertexts):
            metric = metric_function(text, self.natural_text)
            metric_results[i] = metric
        ranking = np.argsort(metric_results)
        ranked_texts = [self.ciphertexts[x] for x in ranking]
        self.ciphertexts = ranked_texts

import numpy as np
import random
def_alpha = ' etaoinshrdlcumwfgypbvkjxqz'
from filter import filter

class Ciphertext(object):
    def __init__(self, text_indices=np.zeros(0), map_record=0, alpha=def_alpha):
        if np.all(map_record == 0):
            map_record = np.arange(len(alpha))
        self.map_record = map_record
        self.text_indices = text_indices
        self.rates = [None for i in range(6)]
        self.alpha = alpha

    def text_in(self, text, alpha=0):
        if alpha != 0:
            self.alpha = alpha
        filtered_text = filter(text, self.alpha)
        character_index_list = [self.alpha.find(x) for x in filtered_text]
        self.text_indices = np.array(character_index_list)
        self.map_record = np.arange(len(self.alpha))
        return None

    def text_out(self, alpha=0):
        if alpha == 0:
            alpha = self.alpha
        text = ''
        for i in self.text_indices:
            text += alpha[i]
        return text

    def map(self, new_map):
        new_text_indices = np.zeros(self.text_indices.size, dtype=np.int32)
        new_map_record = np.zeros(self.map_record.size, dtype=np.int32)
        for i, x in enumerate(self.text_indices):
            new_text_indices[i] = new_map[x]
        for i, x in enumerate(self.map_record):
            new_map_record[i] = new_map[x]
        return Ciphertext(new_text_indices, new_map_record)

    def substitute(self, new_map):
        for i, x in enumerate(self.text_indices):
            self.text_indices[i] = new_map[x]
        for i, x in enumerate(self.map_record):
            self.map_record[i] = new_map[x]

    def randomise(self):
        random_map = np.arange(len(self.alpha))
        random.shuffle(random_map)
        self.substitute(random_map)

    def pair_shuffle(self):
        new_map = np.arange(len(self.alpha))
        [i, j] = random.sample(new_map)
        self.pair_swap(i, j)

    def pair_swap(self, i, j):
        new_map = np.arange(len(self.alpha))
        i = random.randint(0, new_map.size - 1)
        if i == new_map.size - 1:
            new_map[i], new_map[0] = new_map[0], new_map[i]
        else:
            new_map[i], new_map[i + 1] = new_map[i + 1], new_map[i]
        self.substitute(new_map)

    def group_frequencies(self, number):
        counts = np.zeros([len(self.alpha) for i in range(number)])
        for i in range(len(self.text_indices)-number):
            indices = tuple(self.text_indices[i:i+number])
            counts[indices] += 1
        rates = counts/(len(self.text_indices)+1-number)
        self.rates[number-1] = rates
        return None

    def pair_frequencies(self):
        counts = np.zeros([len(self.alpha), len(self.alpha)])
        for i in range(len(self.text_indices)-1):
            counts[self.text_indices[i],self.text_indices[i+1]] += 1
        rates = counts/(len(self.text_indices)-1)
        self.rates[1] = rates
        return None

    def triplet_frequencies(self):
        counts = np.zeros([len(self.alpha) for i in range(3)])
        for i in range(len(self.text_indices)-2):
            counts[self.text_indices[i],self.text_indices[i+1], \
                self.text_indices[i+2]] += 1
        rates = counts/(len(self.text_indices)-2)
        self.rates[2] = rates
        return None

    def quadruplet_frequencies(self):
        counts = np.zeros([len(self.alpha) for i in range(4)])
        for i in range(len(self.text_indices)-3):
            counts[self.text_indices[i],self.text_indices[i+1], \
                self.text_indices[i+2],self.text_indices[i+3]] += 1
        rates = counts/(len(self.text_indices)-3)
        self.rates[3] = rates
        return None

    def pair_frequencies2(self):
        record = np.zeros([len(self.text_indices)-1, 2])
        for i in range(len(self.text_indices)-1):
            record[i,i:i+1] = self.text_indices[i:i+1]
        self.rates[1] = record
        return None

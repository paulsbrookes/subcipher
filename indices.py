import numpy as np
import random

class Indices(object):
    def __init__(self, text_indices=np.zeros(0), alpha='abcdefghijklmnopqrstuvwxyz '):
        self.text_indices = text_indices
        self.rates = [None for i in range(3)]
        self.alpha = alpha
        self.map_record = np.arange(len(alpha))

    def text_in(self, text):
        def filter(text_in, alpha):
            filtered_text = ''
            for x in text_in.lower():
                if x in alpha:
                    filtered_text += x
            return filtered_text
        filtered_text = filter(text, self.alpha)
        character_index_list = [self.alpha.find(x) for x in filtered_text]
        self.text_indices = np.array(character_index_list)
        return None

    def filter(self, alpha=0):
        if alpha == 0:
            alpha = self.alpha
        filtered_message = ''
        for x in self.text.lower():
            if x in alpha:
                filtered_message += x
        return Message(filtered_message, self.alpha)

    def map(self, new_map):
        new_text_indices = np.zeros(self.text_indices.size)
        for i, x in enumerate(self.text_indices):
            new_text_indices[i] = new_map[x]
        return Indices(new_text_indices)
        for i, x in enumerate(self.map_record):
            self.map_record[i] = new_map[x]
        return Indices(new_text_indices)

    def substitute(self, new_map):
        for i, x in enumerate(self.text_indices):
            self.text_indices[i] = new_map[x]
        for i, x in enumerate(self.map_record):
            self.map_record[i] = new_map[x]

    def text_out(self):
        text = ''
        for i in self.text_indices:
            text += self.alpha[i]
        return text

    def randomise(self):
        random_map = np.arange(len(self.alpha))
        random.shuffle(random_map)
        self.substitute(random_map)

    def pair_shuffle(self):
        new_map = np.arange(len(self.alpha))
        i = random.randint(0, new_map.size - 1)
        if i == new_map.size - 1:
            new_map[i], new_map[0] = new_map[0], new_map[i]
        else:
            new_map[i], new_map[i + 1] = new_map[i + 1], new_map[i]
        self.substitute(new_map)

    def group_frequencies(self, number):
        counts = np.zeros([len(self.alpha) for i in range(number)])
        for i in range(len(self.text_indices)+1-number):
            indices = tuple(self.text_indices[i:i+number])
            counts[indices] += 1
        rates = counts/(len(self.text)+1-number)
        self.rates[number-2] = rates
        return None

    def pair_frequencies(self):
        counts = np.zeros([len(self.alpha), len(self.alpha)])
        for i in range(len(self.text_indices)-1):
            counts[self.text_indices[i],self.text_indices[i+1]] += 1
        rates = counts/(len(self.text_indices)-1)
        self.rates[0] = rates
        return None

    def pair_frequencies2(self):
        record = np.zeros([len(self.text_indices)-1, 2])
        for i in range(len(self.text_indices)-1):
            record[i,i:i+1] = self.text_indices[i:i+1]
        self.rates[1] = record
        return None

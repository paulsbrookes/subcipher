import numpy as np

class Message(object):
    def __init__(self, text, alpha = ' etaoinshrdlcumwfgypbvkjxqz'):
        self.text = text
        self.alpha = alpha
        self.rates = [None for i in range(5)]

    def map(self, key):
        new_message = ''
        for x in self.text:
            x_index = self.alpha.find(x)
            if x_index == -1:
                new_message += x
            else:
                mapped_to = self.alpha[key.map[x_index]]
                new_message += mapped_to
        return Message(new_message)

    def frequencies(self, alpha=0):
        if alpha == 0:
            alpha = self.alpha
        counts = np.zeros([len(alpha)])
        for i, x in enumerate(alpha):
            counts[i] = self.text.count(x)
        rates = counts/len(self.text)
        return rates

    def filter(self, alpha=0):
        if alpha == 0:
            alpha = self.alpha
        filtered_message = ''
        for x in self.text.lower():
            if x in alpha:
                filtered_message += x
        return Message(filtered_message, self.alpha)

    def triplet_frequencies(self, alpha=0):
        if alpha == 0:
            alpha = self.alpha
        counts = np.zeros([len(alpha), len(alpha), len(alpha)])
        for i in range(len(self.text)-2):
            x = self.alpha.find(self.text[i])
            y = self.alpha.find(self.text[i+1])
            z = self.alpha.find(self.text[i+2])
            counts[x,y,z] += 1
        rates = counts/(len(self.text)-2)
        self.rates[1] = rates
        return None

    def triplet_frequency_dictionary(self):
        self.rate_dictionary = {}
        for i in range(len(self.text)-2):
            group = self.text[i:i+3]
            self.rate_dictionary[group] = self.text.count(group)

    def quadruplet_frequency_dictionary(self):
        self.rate_dictionary = {}
        for i in range(len(self.text)-3):
            group = self.text[i:i+4]
            self.rate_dictionary[group] = self.text.count(group)

    def frequency_dictionary(self, number):
        self.rate_dictionary = {}
        for i in range(len(self.text)+1-number):
            group = self.text[i:i+number]
            self.rate_dictionary[group] = self.text.count(group)

    def quadruplet_frequencies(self, alpha=0):
        if alpha == 0:
            alpha = self.alpha
        counts = np.zeros([len(alpha),len(alpha),len(alpha),len(alpha)])
        for i in range(len(self.text)-3):
            w = alpha.find(self.text[i])
            x = alpha.find(self.text[i+1])
            y = alpha.find(self.text[i+2])
            z = alpha.find(self.text[i+3])
            counts[w,x,y,z] += 1
        rates = counts/(len(self.text)-3)
        self.rates[2] = rates
        return None

    def group_frequencies(self, number, alpha=0):
        if alpha == 0:
            alpha = self.alpha
        counts = np.zeros([len(alpha) for i in range(number)])
        for i in range(len(self.text)+1-number):
            group = self.text[i:i+number]
            indices = tuple([self.alpha.find(group[i]) for i in range(number)])
            counts[indices] += 1
        rates = counts/(len(self.text)+1-number)
        self.rates[number-2] = rates
        return None

    def alt_frequencies(self, alpha=0):
        if alpha == 0:
            alpha = self.alpha
        count_dictionary = {}
        counts = np.zeros([len(alpha) for i in range(3)])
        for i in range(len(self.text)-2):
            group = self.text[i:i+3]
            count_dictionary[group] = self.text.count(group)
        for key in count_dictionary:
            indices = tuple([self.alpha.find(key[i]) for i in range(3)])
            counts[indices] = count_dictionary[key]
        return None

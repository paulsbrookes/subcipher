import numpy as np

class Message(object):
    def __init__(self, text, alpha = 'abcdefghijklmnopqrstuvwxyz '):
        self.text = text
        self.alpha = alpha

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

    def frequencies(self, alpha = 0):
        if alpha == 0:
            alpha = self.alpha
        counts = np.zeros([len(alpha)])
        for i, x in enumerate(alpha):
            counts[i] = self.text.count(x)
        rates = counts/len(self.text)
        return rates

    def filter(self, alpha = 0):
        if alpha == 0:
            alpha = self.alpha
        filtered_message = ''
        for x in self.text.lower():
            if x in alpha:
                filtered_message += x
        return Message(filtered_message, self.alpha)

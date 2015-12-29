import numpy as np
import random
default_alpha = 'abcdefghijklmnopqrstuvwxyz '

class Key(object):
    def __init__(self, map=[]):
        self.map = map

    def substitute(self, new_map):
        map_out = np.zeros(self.map.shape[0], dtype = np.int8)
        for x in range(self.map.shape[0]):
            map_out[x] = new_map.map[self.map[x]]
        return Key(map_out)

    def invert(self):
        inverted_map = np.zeros(self.map.shape[0], dtype = np.int8)
        for x in range(self.map.size):
            inverted_map[self.map[x]] = x
        return Key(inverted_map)

    def obtain_key(self, alpha, beta):
        key = np.zeros(len(beta))
        for x in range(len(beta)):
            key[x] = alpha.find(beta[x])
        return Key(key)

    def random_key(self, alpha = default_alpha):
        self.map = np.array(range(len(alpha)))
        random.shuffle(self.map)

    def frequency_key(self, natural_frequencies, observed_frequencies):
        natural_indices_sorted = np.argsort(natural_frequencies)
        observed_indices_sorted = np.argsort(observed_frequencies)
        frequency_key = np.zeros(natural_frequencies.size, dtype = np.int8)
        for i, x in enumerate(natural_indices_sorted):
            frequency_key[x] = observed_indices_sorted[i]
        self.map = frequency_key

    def dictionary(self, alpha = default_alpha):
        letter_map = np.zeros([2, len(alpha)], dtype = '|S1')
        for i, x in enumerate(alpha):
            letter_map[0, i] = x
            letter_map[1, i] = alpha[self.map[i]]
        return letter_map

    def swap(self,i,j):
        swap_map = np.copy(self.map)
        swap_map[i], swap_map[j] = self.map[j], self.map[i]
        return Key(swap_map)

    def array_swap(self):
        return [self.swap(i,j) for i in range(self.map.size) for j in range(self.map.size)]

    def cycle(self,i,direction):
        swap_map = np.copy(self.map)
        if i in range(swap_map.size-2):
            if direction == 0:
                swap_map[i], swap_map[i+1], swap_map[i+2],\
                    = self.map[i+1], self.map[i+2], self.map[i]
            elif direction == 1:
                swap_map[i], swap_map[i+1], swap_map[i+2],\
                    = self.map[i+2], self.map[i], self.map[i+1]
            else:
                pass
        else:
            pass
        return Key(swap_map)

    def array_cycle(self, number):
        return [self.cycle(i, number, j) for i in range(self.map.size + 1 - number) for j in range(2)]

    def swap2(self, i):
        swap_map = np.copy(self.map)
        if i == swap_map.size - 1:
            swap_map[i], swap_map[0] = self.map[0], self.map[i]
        else:
            swap_map[i], swap_map[i + 1] = self.map[i + 1], self.map[i]
        return swap_map

    def array_swap2(self):
        return [self.swap2(i) for i in range(self.map.size)]

    def pair_scramble(self):
        i = random.randint(0, self.map.size - 1)
        if i == self.map.size - 1:
            self.map[i], self.map[0] = self.map[0], self.map[i]
        else:
            self.map[i], self.map[i + 1] = self.map[i + 1], self.map[i]

    def cycle(self, i, number, direction):
        swap_map = np.copy(self.map)
        if i in range(swap_map.size + 1 - number):
            if direction == 0:
                for j in range(number):
                    swap_map[i+j] = self.map[i+(j+1)%number]
            elif direction == 1:
                for j in range(number):
                    swap_map[i+j] = self.map[i+(j-1)%number]
            else:
                pass
        else:
            pass
        return Key(swap_map)

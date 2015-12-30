import numpy as np
from key import Key
import itertools

default_alpha = 'abcdefghijklmnopqrstuvwxyz '

def pair_metric(ciphertext, natural_text):
    ciphertext.pair_frequencies()
    difference = abs(natural_text.rates[0] - ciphertext.rates[0])
    difference = np.absolute(difference) + 1e-6
    metric = -np.sum(1/difference)
    return metric

def pair_metric2(ciphertext, natural_text):
    ciphertext.pair_frequencies2()
    metric = 0
    for i in range(ciphertext.rates[1].shape[0]):
        metric += 1/(natural_text.rates[0][ciphertext.rates[1][i,0],ciphertext.rates[1][i,1]]+1e-6)
    return metric

def pair_metric_generator(natural_text):
    def pair_metric(ciphertext):
        ciphertext.pair_frequencies()
        difference = abs(natural_text.rates[0] - ciphertext.rates[0])
        difference = np.absolute(difference) + 1e-6
        metric = -np.sum(1/difference)
        return metric
    return pair_metric

def remove_duplicates(values):
    map_list = [x.map_record for x in values]
    list_form.sort()
    filtered_list = list(list_form for list_form,_ in itertools.groupby(list_form))
    filtered_arrays = [np.array(x) for x in filtered_list]
    return filtered_arrays

def rm_duplicate_arrays(values):
    list_form = [x.tolist() for x in values]
    list_form.sort()
    filtered_list = list(list_form for list_form,_ in itertools.groupby(list_form))
    filtered_arrays = [np.array(x) for x in filtered_list]
    return filtered_arrays

def cycle(map, i, number, direction):
    new_map = np.copy(map)
    if direction == 0:
        for j in range(number):
            new_map[(i+j)%map.size] = map[(i+(j+1)%number)%map.size]
    elif direction == 1:
        for j in range(number):
            new_map[(i+j)%map.size] = map[(i+(j-1)%number)%map.size]
    else:
        pass
    return new_map

def cycle_list(map, number):
    return [cycle(map, i, number, j) for i in range(map.size + 1 - number) for j in range(2)]

def cycle_list_gen(number):
    def cycle_list(map):
        return [cycle(map, i, number, j) for i in range(map.size + 1 - number) for j in range(2)]
    return cycle_list

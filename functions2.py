import numpy as np
from key import Key
import itertools

default_alpha = ' etaoinshrdlcumwfgypbvkjxqz'

def pair_metric(ciphertext, natural_text):
    ciphertext.pair_frequencies()
    difference = abs(natural_text.rates[1] - ciphertext.rates[1])
    difference = np.absolute(difference) + 1e-6
    metric = -np.sum(1/difference)
    return metric

def pair_metric2(ciphertext, natural_text):
    ciphertext.pair_frequencies2()
    metric = 0
    for i in range(ciphertext.rates[1].shape[0]):
        metric += 1/(natural_text.rates[1][ciphertext.rates[1][i,0],ciphertext.rates[1][i,1]]+1e-6)
    return metric

def pair_metric3(ciphertext, natural_text):
    ciphertext.pair_frequencies()
    metric = -np.sum(ciphertext.rates[1]*(natural_text.rates[1]+1e-8))
    return metric

def pair_metric4(ciphertext, natural_text):
    ciphertext.pair_frequencies()
    metric = np.sum(abs(natural_text.rates[1] - ciphertext.rates[1]))
    return metric

def pair_metric_generator(natural_text):
    def pair_metric(ciphertext):
        ciphertext.pair_frequencies()
        difference = abs(natural_text.rates[1] - ciphertext.rates[1])
        difference = np.absolute(difference) + 1e-6
        metric = -np.sum(1/difference)
        return metric
    return pair_metric

def triplet_metric(ciphertext, natural_text):
    ciphertext.triplet_frequencies()
    difference = abs(natural_text.rates[2] - ciphertext.rates[2])
    difference = np.absolute(difference) + 1e-10
    metric = -np.sum(1/difference)
    return metric

def triplet_metric2(ciphertext, natural_text):
    ciphertext.triplet_frequencies()
    metric = -np.sum(ciphertext.rates[2]*(natural_text.rates[2]+1e-8))
    return metric

def triplet_metric2(ciphertext, natural_text):
    ciphertext.triplet_frequencies()
    metric = -np.sum(ciphertext.rates[2]*(natural_text.rates[2]+1e-8))
    return metric

def quadruplet_metric(ciphertext, natural_text):
    ciphertext.quadruplet_frequencies()
    difference = abs(natural_text.rates[3] - ciphertext.rates[3])
    difference = np.absolute(difference) + 1e-10
    metric = -np.sum(1/difference)
    return metric

def rm_duplicate_ciphertexts2(values):
    map_list = [x.map_record for x in values]
    list_form.sort()
    filtered_list = list(list_form for list_form,_ in itertools.groupby(list_form))
    filtered_arrays = [np.array(x) for x in filtered_list]
    indices = [map_list.find(x) for x in filtered_arrays]
    filtered_ciphertexts = [Indices(values[0].text_indices, values[0].map_record)]
    return filtered_arrays

def rm_duplicate_ciphertexts(values, number_retained):
    map_list = [x.map_record.tolist() for x in values]
    added = []
    filtered_ciphertexts = []
    for i, x in enumerate(map_list):
        if x not in added:
            added.append(x)
            filtered_ciphertexts.append(values[i])
            if len(filtered_ciphertexts) >= number_retained:
                return filtered_ciphertexts
    return filtered_ciphertexts

def rm_duplicate_ciphertexts3(ciphertexts, number_retained=0):
    if number_retained == 0:
        number_retained = len(ciphertexts)
    added = []
    number_added = 0
    filtered_ciphertexts = []
    for i, x in enumerate(ciphertexts):
        map = x.map_record.tolist()
        if map not in added:
            number_added += 1
            added.append(map)
            filtered_ciphertexts.append(ciphertexts[i])
            if number_added == number_retained:
                return filtered_ciphertexts
    return filtered_ciphertexts

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
    new_maps = [cycle(map, i, number, j) for i in range(map.size + 1 - number) for j in range(2)]
    new_maps = rm_duplicate_arrays(new_maps)
    return new_maps

def cycle_list_gen(number):
    def cycle_list(map):
        new_maps = [cycle(map, i, number, j) for i in range(map.size + 1 - number) for j in range(2)]
        new_maps = rm_duplicate_arrays(new_maps)
        return new_maps
    return cycle_list

def swap(map, i, j):
    new_map = np.copy(map)
    new_map[i], new_map[j] = map[j], map[i]
    return new_map

def swap_list(map):
    new_maps = [swap(map, i, j) for i in range(len(map)) for j in range(len(map))]
    new_maps = rm_duplicate_arrays(new_maps)
    return new_maps

def swap_list_gen(distance):
    def swap_list(map):
        new_maps = [swap(map, i%26, (i+j)%26) for i in range(len(map)) for j in range(-distance,distance)]
        new_maps = rm_duplicate_arrays(new_maps)
        return new_maps
    return swap_list

def repeat_indices(rates):
    added = []
    indices = []
    repeated_elements = []
    for x in rates:
        if (x not in added and x !=0):
            added.append(x)
            indices.append(np.where(rates==x)[0])
    for x in indices:
        if len(x) != 1:
            repeated_elements.append(x)
    return repeated_elements

def perm_maps(indices):
    perms = itertools.permutations(indices)
    maps = [np.array([indices,x]) for x in perms]
    return maps

def substitute(map, subs):
    new_map = np.copy(map)
    for i, x in enumerate(subs[0]):
        new_map[x] = subs[1][i]
    return new_map

def permute(old_maps, indices):
    shuffle_maps = perm_maps(indices)
    permuted_maps = []
    for o_map in old_maps:
        for s_map in shuffle_maps:
            permuted_maps.append(substitute(o_map, s_map))
    return permuted_maps

def grand_permute(map, rates):
    maps = [map]
    indices = repeat_indices(rates)
    for index_set in indices:
        maps = permute(maps, index_set)
    return maps
